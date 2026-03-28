"""Email finder — generate and validate email candidates.

Given a name and domain, generates email permutations,
validates syntax and MX records, filters disposable domains.
"""

import logging
import re
from typing import Any

import dns.resolver
from email_validator import validate_email, EmailNotValidError

logger = logging.getLogger(__name__)

# Common disposable email domains
_DISPOSABLE_DOMAINS = frozenset({
    "mailinator.com", "guerrillamail.com", "tempmail.com", "throwaway.email",
    "yopmail.com", "sharklasers.com", "guerrillamailblock.com", "grr.la",
    "dispostable.com", "trashmail.com", "fakeinbox.com", "maildrop.cc",
    "10minutemail.com", "temp-mail.org", "getnada.com", "mohmal.com",
    "burnermail.io", "mailnesia.com", "tempr.email", "discard.email",
})


class EmailFinder:
    """Generate and validate email candidates from name + domain."""

    def generate_permutations(
        self,
        first_name: str,
        last_name: str | None,
        domain: str,
    ) -> list[str]:
        """Generate common email permutations from name and domain.

        Returns list of lowercase email candidates.
        """
        first = first_name.lower().strip()
        domain = domain.lower().strip()
        permutations = [f"{first}@{domain}"]

        if last_name:
            last = last_name.lower().strip()
            first_initial = first[0] if first else ""
            permutations.extend([
                f"{first}.{last}@{domain}",
                f"{first}{last}@{domain}",
                f"{first_initial}.{last}@{domain}",
                f"{first_initial}{last}@{domain}",
                f"{last}@{domain}",
                f"{last}.{first}@{domain}",
                f"{first}_{last}@{domain}",
                f"{first}-{last}@{domain}",
            ])
        else:
            permutations.extend([
                f"info@{domain}",
                f"contact@{domain}",
                f"hello@{domain}",
            ])

        return list(dict.fromkeys(permutations))  # Deduplicate preserving order

    def validate_syntax(self, email: str) -> bool:
        """Check if an email has valid syntax."""
        try:
            validate_email(email, check_deliverability=False)
            return True
        except EmailNotValidError:
            return False

    async def check_mx(self, domain: str) -> bool:
        """Check if a domain has MX records."""
        return await self._resolve_mx(domain)

    async def _resolve_mx(self, domain: str) -> bool:
        """Resolve MX records for a domain."""
        try:
            dns.resolver.resolve(domain, "MX")
            return True
        except Exception:
            return False

    def is_disposable(self, email: str) -> bool:
        """Check if an email uses a disposable domain."""
        domain = email.lower().split("@")[-1]
        return domain in _DISPOSABLE_DOMAINS

    async def find_best(
        self,
        first_name: str,
        last_name: str | None,
        domain: str,
    ) -> dict[str, Any]:
        """Find the best email candidate for a person at a domain.

        Generates permutations, validates, and returns best candidate
        with confidence score.
        """
        permutations = self.generate_permutations(first_name, last_name, domain)

        # Check MX first — if domain has no MX, no point checking emails
        has_mx = await self.check_mx(domain)
        if not has_mx:
            return {
                "email": permutations[0] if permutations else None,
                "confidence": 0.1,
                "reason": "Domain has no MX records",
            }

        # Filter valid syntax and non-disposable
        valid = [
            e for e in permutations
            if self.validate_syntax(e) and not self.is_disposable(e)
        ]

        if not valid:
            return {
                "email": None,
                "confidence": 0.0,
                "reason": "No valid candidates",
            }

        # Best candidate: first.last pattern has highest confidence
        best = valid[0]
        confidence = 0.4  # Base confidence for MX-valid domain

        # Boost for common patterns
        if last_name and f"{first_name.lower()}.{last_name.lower()}" in best:
            confidence = 0.7
        elif last_name and f"{first_name[0].lower()}.{last_name.lower()}" in best:
            confidence = 0.6

        return {
            "email": best,
            "confidence": confidence,
            "candidates": valid[:5],
        }
