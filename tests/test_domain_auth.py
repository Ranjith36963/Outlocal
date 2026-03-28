"""Tests for domain authentication checker — SPF/DKIM/DMARC (F011)."""

import pytest
from unittest.mock import AsyncMock, patch, MagicMock

from src.outlocal.email_sender.domain_auth import DomainAuthChecker


@pytest.fixture
def checker():
    return DomainAuthChecker()


class TestDomainAuthChecker:
    """Tests for SPF, DKIM, DMARC checking."""

    @pytest.mark.asyncio
    async def test_check_returns_all_three(self, checker):
        """Result should include SPF, DKIM, DMARC checks."""
        with patch.object(checker, "_check_spf", new_callable=AsyncMock, return_value={"exists": True, "valid": True, "record": "v=spf1 include:_spf.google.com ~all"}):
            with patch.object(checker, "_check_dkim", new_callable=AsyncMock, return_value={"exists": True, "valid": True}):
                with patch.object(checker, "_check_dmarc", new_callable=AsyncMock, return_value={"exists": True, "policy": "reject", "record": "v=DMARC1; p=reject"}):
                    result = await checker.check_domain("example.com")

        assert "spf" in result
        assert "dkim" in result
        assert "dmarc" in result

    @pytest.mark.asyncio
    async def test_spf_check_structure(self, checker):
        with patch.object(checker, "_check_spf", new_callable=AsyncMock, return_value={"exists": True, "valid": True, "record": "v=spf1"}):
            with patch.object(checker, "_check_dkim", new_callable=AsyncMock, return_value={"exists": False}):
                with patch.object(checker, "_check_dmarc", new_callable=AsyncMock, return_value={"exists": False}):
                    result = await checker.check_domain("example.com")

        assert "exists" in result["spf"]

    @pytest.mark.asyncio
    async def test_overall_pass_when_all_valid(self, checker):
        with patch.object(checker, "_check_spf", new_callable=AsyncMock, return_value={"exists": True, "valid": True, "record": "v=spf1"}):
            with patch.object(checker, "_check_dkim", new_callable=AsyncMock, return_value={"exists": True, "valid": True}):
                with patch.object(checker, "_check_dmarc", new_callable=AsyncMock, return_value={"exists": True, "policy": "reject", "record": "v=DMARC1"}):
                    result = await checker.check_domain("example.com")

        assert result["overall"] == "pass"

    @pytest.mark.asyncio
    async def test_overall_warn_when_missing(self, checker):
        with patch.object(checker, "_check_spf", new_callable=AsyncMock, return_value={"exists": True, "valid": True, "record": "v=spf1"}):
            with patch.object(checker, "_check_dkim", new_callable=AsyncMock, return_value={"exists": False}):
                with patch.object(checker, "_check_dmarc", new_callable=AsyncMock, return_value={"exists": False}):
                    result = await checker.check_domain("example.com")

        assert result["overall"] in ("warn", "fail")

    @pytest.mark.asyncio
    async def test_remediation_advice_provided(self, checker):
        with patch.object(checker, "_check_spf", new_callable=AsyncMock, return_value={"exists": False}):
            with patch.object(checker, "_check_dkim", new_callable=AsyncMock, return_value={"exists": False}):
                with patch.object(checker, "_check_dmarc", new_callable=AsyncMock, return_value={"exists": False}):
                    result = await checker.check_domain("example.com")

        assert "advice" in result
        assert len(result["advice"]) > 0
