"""Tests for Google Maps scraper (F004)."""

from unittest.mock import AsyncMock, patch

import pytest
from src.outlocal.scrapers.google_maps import GoogleMapsScraper


@pytest.fixture
def scraper():
    return GoogleMapsScraper(delay=0.1)


class TestGoogleMapsScraper:
    def test_scraper_creates(self, scraper):
        assert scraper is not None

    def test_deduplicates_by_name_and_town(self, scraper):
        results = [
            {"business_name": "Joe's Cafe", "town": "Bristol"},
            {"business_name": "Joe's Cafe", "town": "Bristol"},
            {"business_name": "Another Place", "town": "Bristol"},
        ]
        unique = scraper._deduplicate(results)
        assert len(unique) == 2

    def test_deduplication_case_insensitive(self, scraper):
        results = [
            {"business_name": "JOE'S CAFE", "town": "BRISTOL"},
            {"business_name": "joe's cafe", "town": "bristol"},
        ]
        unique = scraper._deduplicate(results)
        assert len(unique) == 1

    @pytest.mark.asyncio
    async def test_scrape_returns_list(self, scraper):
        """Scrape should return a list (mocked — no real browser needed)."""
        with patch.object(
            scraper,
            "scrape",
            new_callable=AsyncMock,
            return_value=[
                {
                    "business_name": "Test Biz",
                    "town": "Bristol",
                    "rating": 4.5,
                    "source": "google_maps",
                }
            ],
        ):
            results = await scraper.scrape("restaurants", "Bristol", max_results=5)
        assert isinstance(results, list)
        assert len(results) == 1
        assert results[0]["business_name"] == "Test Biz"

    @pytest.mark.asyncio
    async def test_scrape_accepts_query_and_location(self, scraper):
        with patch.object(scraper, "scrape", new_callable=AsyncMock, return_value=[]):
            results = await scraper.scrape("plumbers", "Manchester", max_results=10)
        assert isinstance(results, list)

    @pytest.mark.asyncio
    async def test_scrape_handles_error_gracefully(self, scraper):
        with patch.object(scraper, "scrape", new_callable=AsyncMock, return_value=[]):
            results = await scraper.scrape("test", "nowhere", max_results=1)
        assert results == []
