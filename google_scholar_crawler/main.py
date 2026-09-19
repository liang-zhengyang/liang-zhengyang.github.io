"""Fetch Google Scholar statistics and write static JSON for the homepage."""

from __future__ import annotations

import json
import os
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

from scholarly import scholarly


OUTPUT_DIR = Path(__file__).resolve().parents[1] / "google-scholar-stats"


def normalize_title(title: str) -> str:
    """Create a stable lookup key for matching Scholar and homepage titles."""
    normalized = unicodedata.normalize("NFKD", title).casefold()
    return re.sub(r"[^a-z0-9]+", "", normalized)


def build_payload(author: dict) -> dict:
    publications = {}
    publications_by_title = {}

    for publication in author.get("publications", []):
        publication_id = publication.get("author_pub_id")
        if publication_id:
            publications[publication_id] = publication

        title = publication.get("bib", {}).get("title", "")
        if title:
            publications_by_title[normalize_title(title)] = {
                "title": title,
                "author_pub_id": publication_id,
                "num_citations": publication.get("num_citations", 0),
            }

    return {
        "name": author.get("name", ""),
        "scholar_id": author.get("scholar_id", ""),
        "citedby": author.get("citedby", 0),
        "citedby5y": author.get("citedby5y", 0),
        "hindex": author.get("hindex", 0),
        "hindex5y": author.get("hindex5y", 0),
        "i10index": author.get("i10index", 0),
        "i10index5y": author.get("i10index5y", 0),
        "updated": datetime.now(timezone.utc).isoformat(),
        "publications": publications,
        "publications_by_title": publications_by_title,
    }


def write_json(path: Path, data: dict) -> None:
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
    if not scholar_id:
        raise RuntimeError("GOOGLE_SCHOLAR_ID is required")

    author = scholarly.search_author_id(scholar_id)
    author = scholarly.fill(
        author,
        sections=["basics", "indices", "counts", "publications"],
    )
    payload = build_payload(author)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    write_json(OUTPUT_DIR / "gs_data.json", payload)
    write_json(
        OUTPUT_DIR / "gs_data_shieldsio.json",
        {
            "schemaVersion": 1,
            "label": "citations",
            "message": str(payload["citedby"]),
        },
    )
    print(
        f"Fetched {len(payload['publications'])} publications and "
        f"{payload['citedby']} citations for {payload['name']}."
    )


if __name__ == "__main__":
    main()
