"""Run with: python -m unittest discover -s google_scholar_crawler."""

import unittest
from unittest.mock import patch

from google_scholar_crawler.main import build_payload, fetch_with_serpapi


class ScholarPayloadTests(unittest.TestCase):
    def test_pagination_keeps_newest_and_oldest_publications(self):
        def article(index):
            return {
                "title": f"Paper {index}",
                "citation_id": f"profile:{index}",
                "authors": "Z Liang, A Author",
                "publication": "Example Conference",
                "year": "2026" if index == 0 else "2024",
                "cited_by": {"value": 0},
            }

        first_page = {
            "author": {"name": "Zhengyang Liang"},
            "articles": [article(index) for index in range(100)],
            "serpapi_pagination": {"next": "next-page"},
            "cited_by": {"table": [{"citations": {"all": 100, "since_2021": 90}}]},
        }
        pages = [first_page, {"articles": [article(100)]}]
        offsets = []

        def request(params):
            offsets.append(params["start"])
            return pages.pop(0)

        with patch("google_scholar_crawler.main.request_serpapi", side_effect=request):
            payload = build_payload(fetch_with_serpapi("profile", "test-key"))
        self.assertEqual(offsets, [0, 100])
        self.assertEqual(len(payload["publication_list"]), 101)
        self.assertEqual(payload["publication_list"][0]["year"], "2026")
        self.assertEqual(payload["publication_list"][-1]["author_pub_id"], "profile:100")
        self.assertEqual(payload["publication_list"][0]["num_citations"], 0)
        self.assertEqual(payload["citedby"], 100)
        self.assertEqual(payload["citedby5y"], 90)

    def test_scholarly_metadata_and_missing_year_are_supported(self):
        payload = build_payload({
            "name": "Zhengyang Liang",
            "scholar_id": "profile",
            "publications": [{
                "author_pub_id": "profile:paper",
                "bib": {"title": "A Renamed Paper", "venue": "Journal", "author": "Z Liang"},
                "num_citations": 3,
            }],
        })
        paper = payload["publication_list"][0]
        self.assertEqual(paper["venue"], "Journal")
        self.assertEqual(paper["year"], "")
        self.assertIn("citation_for_view=profile%3Apaper", paper["scholar_url"])
        self.assertEqual(paper["url"], paper["scholar_url"])
        self.assertEqual(payload["publications_by_title"]["arenamedpaper"]["num_citations"], 3)
        self.assertEqual(payload["publications"]["profile:paper"]["bib"]["title"], "A Renamed Paper")

    def test_invalid_or_empty_scrapes_cannot_replace_previous_snapshot(self):
        for author in [{}, {"name": "Someone"}, {
            "name": "Zhengyang Liang", "scholar_id": "profile", "publications": [],
        }]:
            with self.subTest(author=author), self.assertRaises(RuntimeError):
                build_payload(author)


if __name__ == "__main__":
    unittest.main()
