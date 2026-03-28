"""Website crawler for extracting emails, phones, social links, and tech stack.

Crawls business websites to enrich lead data with contact info
and technology detection.
"""

import asyncio
import logging
import re
from typing import Any
from urllib.parse import urljoin, urlparse

import aiohttp
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

_EMAIL_REGEX = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
_UK_PHONE_REGEX = re.compile(r"(?:\+44|0)\s*\d{2,4}[\s.-]?\d{3,4}[\s.-]?\d{3,4}")
_SOCIAL_PATTERNS = {
    "facebook": re.compile(r"https?://(?:www\.)?facebook\.com/[^\s\"'>]+"),
    "instagram": re.compile(r"https?://(?:www\.)?instagram\.com/[^\s\"'>]+"),
    "twitter": re.compile(r"https?://(?:www\.)?(?:twitter|x)\.com/[^\s\"'>]+"),
    "linkedin": re.compile(r"https?://(?:www\.)?linkedin\.com/[^\s\"'>]+"),
}
_TECH_SIGNATURES = {
    "wordpress": ["wp-content", "wp-includes", "wordpress"],
    "wix": ["wix.com", "wixsite.com", "_wix_browser_sess"],
    "squarespace": ["squarespace.com", "sqsp.net"],
    "shopify": ["shopify.com", "cdn.shopify"],
}


class WebsiteCrawler:
    """Crawl websites to extract contact info and tech stack."""

    def __init__(self, max_depth: int = 3, timeout: int = 10) -> None:
        self._max_depth = max_depth
        self._timeout = aiohttp.ClientTimeout(total=timeout)

    async def crawl(self, url: str) -> dict[str, Any]:
        """Crawl a website and extract enrichment data.

        Returns dict with emails, phones, social_links, tech_stack,
        has_ssl, is_mobile_friendly.
        """
        if not url.startswith("http"):
            url = f"https://{url}"

        result: dict[str, Any] = {
            "url": url,
            "emails": [],
            "phones": [],
            "social_links": {},
            "tech_stack": [],
            "has_ssl": url.startswith("https"),
            "pages_crawled": 0,
        }

        visited: set[str] = set()
        domain = urlparse(url).netloc

        try:
            await self._crawl_page(url, domain, visited, result, depth=0)
        except Exception as e:
            logger.error("Crawl failed for %s: %s", url, e)
            result["error"] = str(e)

        # Deduplicate
        result["emails"] = list(set(result["emails"]))
        result["phones"] = list(set(result["phones"]))

        return result

    async def _crawl_page(
        self,
        url: str,
        domain: str,
        visited: set[str],
        result: dict[str, Any],
        depth: int,
    ) -> None:
        """Crawl a single page and extract data."""
        if depth >= self._max_depth or url in visited:
            return
        if urlparse(url).netloc != domain:
            return

        visited.add(url)
        result["pages_crawled"] += 1

        try:
            async with aiohttp.ClientSession(timeout=self._timeout) as session:
                async with session.get(url, ssl=False) as response:
                    if response.status != 200:
                        return
                    content_type = response.headers.get("content-type", "")
                    if "text/html" not in content_type:
                        return
                    html = await response.text()
        except Exception as e:
            logger.debug("Failed to fetch %s: %s", url, e)
            return

        soup = BeautifulSoup(html, "lxml")
        page_text = soup.get_text()
        page_html = str(soup)

        # Extract emails
        emails = _EMAIL_REGEX.findall(page_text)
        result["emails"].extend(e for e in emails if not e.endswith((".png", ".jpg", ".gif")))

        # Extract phones
        phones = _UK_PHONE_REGEX.findall(page_text)
        result["phones"].extend(phones)

        # Extract social links
        for platform, pattern in _SOCIAL_PATTERNS.items():
            matches = pattern.findall(page_html)
            if matches and platform not in result["social_links"]:
                result["social_links"][platform] = matches[0]

        # Detect tech stack
        html_lower = page_html.lower()
        for tech, signatures in _TECH_SIGNATURES.items():
            if any(sig in html_lower for sig in signatures):
                if tech not in result["tech_stack"]:
                    result["tech_stack"].append(tech)

        # Follow internal links (next depth)
        if depth < self._max_depth - 1:
            links = soup.find_all("a", href=True)
            internal_links = []
            for link in links[:10]:  # Limit to 10 links per page
                href = urljoin(url, link["href"])
                if urlparse(href).netloc == domain and href not in visited:
                    internal_links.append(href)

            for link_url in internal_links[:5]:
                await self._crawl_page(link_url, domain, visited, result, depth + 1)

    async def check_robots_txt(self, url: str) -> bool:
        """Check if crawling is allowed by robots.txt."""
        parsed = urlparse(url)
        robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
        try:
            async with aiohttp.ClientSession(timeout=self._timeout) as session:
                async with session.get(robots_url, ssl=False) as response:
                    if response.status == 200:
                        text = await response.text()
                        # Basic check: if Disallow: / for all agents, skip
                        if "Disallow: /" in text and "User-agent: *" in text:
                            return False
            return True
        except Exception:
            return True  # If robots.txt fails, assume allowed
