"""Fetch Google Scholar statistics and write static JSON for the homepage."""

from __future__ import annotations

import json
import os
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


OUTPUT_DIR = Path(__file__).resolve().parents[1] / "google-scholar-stats"
SERPAPI_ENDPOINT = "https://serpapi.com/search.json"


def normalize_title(title: str) -> str:
    """Create a stable lookup key for matching Scholar and homepage titles."""
    normalized = unicodedata.normalize("NFKD", title).casefold()
    return re.sub(r"[^a-z0-9]+", "", normalized)


def extract_serpapi_metric(table: list[dict], name: str) -> tuple[int, int]:
    values = next((row[name] for row in table if name in row), {})
    recent = next((value for key, value in values.items() if key != "all"), 0)
    return int(values.get("all", 0)), int(recent)


def request_serpapi(params: dict[str, str | int]) -> dict:
    request = Request(
        f"{SERPAPI_ENDPOINT}?{urlencode(params)}",
        headers={"User-Agent": "liang-zhengyang.github.io citation updater"},
    )
    try:
        with urlopen(request, timeout=30) as response:
            data = json.load(response)
    except HTTPError as error:
        raise RuntimeError(f"SerpApi request failed with HTTP {error.code}") from None
    except URLError as error:
        raise RuntimeError(f"SerpApi request failed: {error.reason}") from None

    if data.get("error"):
        raise RuntimeError(f"SerpApi request failed: {data['error']}")
    return data


def fetch_with_serpapi(scholar_id: str, api_key: str) -> dict:
    params: dict[str, str | int] = {
        "engine": "google_scholar_author",
        "author_id": scholar_id,
        "api_key": api_key,
        "hl": "en",
        "num": 100,
        "start": 0,
    }
    articles = []
    first_page = None

    while True:
        page = request_serpapi(params)
        if first_page is None:
            first_page = page
        batch = page.get("articles", [])
        articles.extend(batch)
        if len(batch) < 100 or not page.get("serpapi_pagination", {}).get("next"):
            break
        params["start"] = int(params["start"]) + 100

    if first_page is None:
        raise RuntimeError("SerpApi returned no author data")

    table = first_page.get("cited_by", {}).get("table", [])
    citedby, citedby5y = extract_serpapi_metric(table, "citations")
    hindex, hindex5y = extract_serpapi_metric(table, "h_index")
    i10index, i10index5y = extract_serpapi_metric(table, "i10_index")

    publications = [
        {
            "author_pub_id": article.get("citation_id", ""),
            "bib": {
                "title": article.get("title", ""),
                "author": article.get("authors", ""),
                "citation": article.get("publication", ""),
            },
            "num_citations": article.get("cited_by", {}).get("value", 0),
        }
        for article in articles
    ]
    return {
        "name": first_page.get("author", {}).get("name", ""),
        "scholar_id": scholar_id,
        "citedby": citedby,
        "citedby5y": citedby5y,
        "hindex": hindex,
        "hindex5y": hindex5y,
        "i10index": i10index,
        "i10index5y": i10index5y,
        "publications": publications,
        "source": "serpapi",
    }


def fetch_with_scholarly(scholar_id: str) -> dict:
    from scholarly import scholarly

    author = scholarly.search_author_id(scholar_id)
    author = scholarly.fill(
        author,
        sections=["basics", "indices", "counts", "publications"],
    )
    author["source"] = "scholarly"
    return author


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
        "source": author.get("source", "google_scholar"),
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

    serpapi_key = os.environ.get("SERPAPI_KEY", "").strip()
    if serpapi_key:
        print("Fetching Google Scholar data via SerpApi.")
        author = fetch_with_serpapi(scholar_id, serpapi_key)
    else:
        print("SERPAPI_KEY is not configured; using scholarly fallback.")
        author = fetch_with_scholarly(scholar_id)
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
