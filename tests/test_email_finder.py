"""Tests for email finder and validation (F006)."""

import pytest
from unittest.mock import AsyncMock, patch

from src.outlocal.enrichment.email_finder import EmailFinder


@pytest.fixture
def finder():
    return EmailFinder()


class TestEmailPermutations:
    """Tests for email permutation generation."""

    def test_generates_permutations(self, finder):
        perms = finder.generate_permutations("John", "Doe", "example.com")
        assert len(perms) > 0
        assert "john@example.com" in perms
        assert "john.doe@example.com" in perms

    def test_permutations_include_common_patterns(self, finder):
        perms = finder.generate_permutations("Jane", "Smith", "test.co.uk")
        expected = [
            "jane@test.co.uk",
            "jane.smith@test.co.uk",
            "j.smith@test.co.uk",
            "jsmith@test.co.uk",
            "smith@test.co.uk",
        ]
        for email in expected:
            assert email in perms, f"Expected {email} in permutations"

    def test_permutations_with_first_name_only(self, finder):
        perms = finder.generate_permutations("Joe", None, "example.com")
        assert "joe@example.com" in perms
        assert len(perms) >= 2

    def test_all_permutations_lowercase(self, finder):
        perms = finder.generate_permutations("JOHN", "DOE", "Example.COM")
        for email in perms:
            assert email == email.lower()


class TestEmailValidation:
    """Tests for email syntax and domain validation."""

    def test_valid_email_syntax(self, finder):
        assert finder.validate_syntax("test@example.com") is True

    def test_invalid_email_syntax(self, finder):
        assert finder.validate_syntax("not-an-email") is False
        assert finder.validate_syntax("@example.com") is False
        assert finder.validate_syntax("test@") is False

    @pytest.mark.asyncio
    async def test_check_mx_records(self, finder):
        """MX check should return True for domains with MX records."""
        with patch.object(finder, "_resolve_mx", new_callable=AsyncMock, return_value=True):
            result = await finder.check_mx("example.com")
        assert result is True

    @pytest.mark.asyncio
    async def test_check_mx_fails_for_invalid_domain(self, finder):
        with patch.object(finder, "_resolve_mx", new_callable=AsyncMock, return_value=False):
            result = await finder.check_mx("nonexistent-domain-xyz.com")
        assert result is False


class TestDisposableFiltering:
    """Tests for disposable email domain filtering."""

    def test_detects_disposable_domain(self, finder):
        assert finder.is_disposable("user@mailinator.com") is True
        assert finder.is_disposable("user@guerrillamail.com") is True

    def test_allows_legitimate_domain(self, finder):
        assert finder.is_disposable("user@gmail.com") is False
        assert finder.is_disposable("user@company.co.uk") is False


class TestBestCandidate:
    """Tests for best email candidate selection."""

    @pytest.mark.asyncio
    async def test_find_best_returns_result(self, finder):
        with patch.object(finder, "check_mx", new_callable=AsyncMock, return_value=True):
            result = await finder.find_best("John", "Doe", "example.com")
        assert "email" in result
        assert "confidence" in result

    @pytest.mark.asyncio
    async def test_find_best_confidence_score(self, finder):
        with patch.object(finder, "check_mx", new_callable=AsyncMock, return_value=True):
            result = await finder.find_best("John", "Doe", "example.com")
        assert 0 <= result["confidence"] <= 1.0
