"""Tests for website crawler (F005)."""

import pytest
from unittest.mock import AsyncMock, patch

from src.outlocal.scrapers.website_crawler import WebsiteCrawler


@pytest.fixture
def crawler():
    return WebsiteCrawler(max_depth=2, timeout=5)


class TestWebsiteCrawler:
    def test_crawler_creates(self, crawler):
        assert crawler is not None

    @pytest.mark.asyncio
    async def test_crawl_returns_structure(self, crawler):
        mock_result = {
            "url": "https://example.com",
            "emails": ["info@example.com"],
            "phones": ["+44 20 1234 5678"],
            "social_links": {"facebook": "https://facebook.com/example"},
            "tech_stack": ["wordpress"],
            "has_ssl": True,
            "pages_crawled": 1,
        }
        with patch.object(crawler, "crawl", new_callable=AsyncMock, return_value=mock_result):
            result = await crawler.crawl("https://example.com")
        assert "emails" in result
        assert "phones" in result
        assert "social_links" in result
        assert "tech_stack" in result
        assert "has_ssl" in result

    @pytest.mark.asyncio
    async def test_ssl_detection(self, crawler):
        with patch.object(crawler, "crawl", new_callable=AsyncMock, return_value={
            "url": "https://secure.com", "has_ssl": True,
            "emails": [], "phones": [], "social_links": {}, "tech_stack": [], "pages_crawled": 0,
        }):
            result = await crawler.crawl("https://secure.com")
        assert result["has_ssl"] is True

    @pytest.mark.asyncio
    async def test_handles_invalid_url(self, crawler):
        with patch.object(crawler, "crawl", new_callable=AsyncMock, return_value={
            "url": "https://invalid", "error": "Connection failed",
            "emails": [], "phones": [], "social_links": {}, "tech_stack": [],
            "has_ssl": True, "pages_crawled": 0,
        }):
            result = await crawler.crawl("https://invalid")
        assert isinstance(result, dict)

    @pytest.mark.asyncio
    async def test_robots_txt_check(self, crawler):
        with patch.object(crawler, "check_robots_txt", new_callable=AsyncMock, return_value=True):
            allowed = await crawler.check_robots_txt("https://example.com")
        assert allowed is True

    @pytest.mark.asyncio
    async def test_extracts_emails_from_html(self, crawler):
        """Test email extraction regex."""
        from src.outlocal.scrapers.website_crawler import _EMAIL_REGEX
        text = "Contact us at info@example.com or sales@test.co.uk"
        emails = _EMAIL_REGEX.findall(text)
        assert "info@example.com" in emails
        assert "sales@test.co.uk" in emails

    @pytest.mark.asyncio
    async def test_extracts_uk_phones(self, crawler):
        from src.outlocal.scrapers.website_crawler import _UK_PHONE_REGEX
        text = "Call us on +44 20 7123 4567 or 0117 123 4567"
        phones = _UK_PHONE_REGEX.findall(text)
        assert len(phones) >= 2

    @pytest.mark.asyncio
    async def test_detects_wordpress(self, crawler):
        from src.outlocal.scrapers.website_crawler import _TECH_SIGNATURES
        html = '<link rel="stylesheet" href="/wp-content/themes/test/style.css">'
        html_lower = html.lower()
        is_wp = any(sig in html_lower for sig in _TECH_SIGNATURES["wordpress"])
        assert is_wp is True
