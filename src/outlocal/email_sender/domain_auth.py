"""Domain authentication checker for SPF, DKIM, and DMARC.

Checks DNS records to verify email sending authentication
is properly configured before sending cold emails.
"""

import logging
from typing import Any

import dns.resolver

logger = logging.getLogger(__name__)


class DomainAuthChecker:
    """Check SPF, DKIM, and DMARC records for a sending domain."""

    async def check_domain(self, domain: str) -> dict[str, Any]:
        """Check all authentication records for a domain.

        Returns dict with spf, dkim, dmarc results, overall status, and advice.
        """
        spf = await self._check_spf(domain)
        dkim = await self._check_dkim(domain)
        dmarc = await self._check_dmarc(domain)

        # Determine overall status
        all_exist = spf.get("exists") and dkim.get("exists") and dmarc.get("exists")
        any_exist = spf.get("exists") or dkim.get("exists") or dmarc.get("exists")

        if all_exist:
            overall = "pass"
        elif any_exist:
            overall = "warn"
        else:
            overall = "fail"

        # Generate remediation advice
        advice: list[str] = []
        if not spf.get("exists"):
            advice.append("Add SPF record: v=spf1 include:your-esp.com ~all")
        if not dkim.get("exists"):
            advice.append("Configure DKIM signing with your email provider")
        if not dmarc.get("exists"):
            advice.append(
                "Add DMARC record: v=DMARC1; p=quarantine; rua=mailto:dmarc@yourdomain.com"
            )

        return {
            "domain": domain,
            "spf": spf,
            "dkim": dkim,
            "dmarc": dmarc,
            "overall": overall,
            "advice": advice,
        }

    async def _check_spf(self, domain: str) -> dict[str, Any]:
        """Check SPF TXT record."""
        try:
            answers = dns.resolver.resolve(domain, "TXT")
            for rdata in answers:
                txt = rdata.to_text().strip('"')
                if txt.startswith("v=spf1"):
                    return {"exists": True, "valid": True, "record": txt}
            return {"exists": False}
        except Exception:
            return {"exists": False}

    async def _check_dkim(self, domain: str, selector: str = "default") -> dict[str, Any]:
        """Check DKIM TXT record for a given selector."""
        try:
            dkim_domain = f"{selector}._domainkey.{domain}"
            answers = dns.resolver.resolve(dkim_domain, "TXT")
            for rdata in answers:
                txt = rdata.to_text().strip('"')
                if "v=DKIM1" in txt or "p=" in txt:
                    return {"exists": True, "valid": True, "selector": selector}
            return {"exists": False}
        except Exception:
            return {"exists": False}

    async def _check_dmarc(self, domain: str) -> dict[str, Any]:
        """Check DMARC TXT record."""
        try:
            dmarc_domain = f"_dmarc.{domain}"
            answers = dns.resolver.resolve(dmarc_domain, "TXT")
            for rdata in answers:
                txt = rdata.to_text().strip('"')
                if txt.startswith("v=DMARC1"):
                    # Extract policy
                    policy = "none"
                    for part in txt.split(";"):
                        part = part.strip()
                        if part.startswith("p="):
                            policy = part[2:]
                    return {"exists": True, "policy": policy, "record": txt}
            return {"exists": False}
        except Exception:
            return {"exists": False}
