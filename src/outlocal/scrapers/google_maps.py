"""Google Maps business scraper for OUTLOCAL.

Scrapes Google Maps search results for local businesses
using Playwright headless browser. Extracts business name,
address, phone, website, rating, and review count.
"""

import asyncio
import logging
import re
from typing import Any
from urllib.parse import quote_plus

logger = logging.getLogger(__name__)


class GoogleMapsScraper:
    """Scrape local businesses from Google Maps search results."""

    def __init__(self, delay: float = 2.0) -> None:
        self._delay = delay

    async def scrape(
        self,
        query: str,
        location: str,
        max_results: int = 20,
    ) -> list[dict[str, Any]]:
        """Scrape Google Maps for businesses matching query + location.

        Args:
            query: Business type (e.g., "restaurants", "plumbers")
            location: UK town/city (e.g., "Bristol", "Manchester")
            max_results: Maximum businesses to scrape

        Returns:
            List of dicts with business data.
        """
        from playwright.async_api import async_playwright

        search_term = f"{query} in {location}"
        url = f"https://www.google.com/maps/search/{quote_plus(search_term)}"

        results: list[dict[str, Any]] = []

        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                page = await browser.new_page()

                await page.goto(url, wait_until="networkidle", timeout=30000)
                await asyncio.sleep(self._delay)

                # Accept cookies if prompted
                try:
                    accept_btn = page.locator("button:has-text('Accept all')")
                    if await accept_btn.count() > 0:
                        await accept_btn.click()
                        await asyncio.sleep(1)
                except Exception:
                    pass

                # Scroll the results panel to load more
                results_panel = page.locator('[role="feed"]')
                if await results_panel.count() > 0:
                    for _ in range(3):  # Scroll 3 times
                        await results_panel.evaluate("el => el.scrollTop = el.scrollHeight")
                        await asyncio.sleep(self._delay)

                # Extract business cards
                cards = page.locator('[class*="Nv2PK"]')
                count = await cards.count()

                for i in range(min(count, max_results)):
                    try:
                        card = cards.nth(i)
                        business = await self._extract_card_data(card)
                        if business and business.get("business_name"):
                            business["source"] = "google_maps"
                            business["town"] = location
                            results.append(business)
                    except Exception as e:
                        logger.debug("Failed to extract card %d: %s", i, e)
                        continue

                await browser.close()

        except Exception as e:
            logger.error("Google Maps scrape failed: %s", e)

        return self._deduplicate(results)

    async def _extract_card_data(self, card: Any) -> dict[str, Any]:
        """Extract business data from a Google Maps result card."""
        data: dict[str, Any] = {}

        # Business name
        try:
            name_el = card.locator('[class*="fontHeadlineSmall"]')
            if await name_el.count() > 0:
                data["business_name"] = await name_el.first.inner_text()
        except Exception:
            pass

        # Rating and review count
        try:
            rating_el = card.locator('[class*="MW4etd"]')
            if await rating_el.count() > 0:
                rating_text = await rating_el.first.inner_text()
                data["rating"] = float(rating_text)

            review_el = card.locator('[class*="UY7F9"]')
            if await review_el.count() > 0:
                review_text = await review_el.first.inner_text()
                numbers = re.findall(r"\d+", review_text.replace(",", ""))
                if numbers:
                    data["review_count"] = int(numbers[0])
        except Exception:
            pass

        # Website and phone from aria labels or data attributes
        try:
            text_content = await card.inner_text()
            # Extract phone (UK format)
            phone_match = re.search(r"(\+44[\d\s]+|0\d{2,4}[\d\s]{6,})", text_content)
            if phone_match:
                data["phone"] = phone_match.group(1).strip()
        except Exception:
            pass

        # Address
        try:
            addr_els = card.locator('[class*="W4Efsd"]')
            if await addr_els.count() > 1:
                addr_text = await addr_els.nth(1).inner_text()
                data["address"] = addr_text.strip()
        except Exception:
            pass

        return data

    def _deduplicate(self, results: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Remove duplicate businesses by name + town."""
        seen: set[str] = set()
        unique: list[dict[str, Any]] = []
        for r in results:
            key = f"{r.get('business_name', '').lower()}|{r.get('town', '').lower()}"
            if key not in seen:
                seen.add(key)
                unique.append(r)
        return unique
