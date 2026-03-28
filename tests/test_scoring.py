"""Tests for lead scoring engine (F007)."""

import pytest

from src.outlocal.scoring.scorer import LeadScorer


@pytest.fixture
def scorer():
    return LeadScorer()


class TestLeadScorer:
    """Tests for rule-based lead scoring."""

    def test_score_range_0_to_100(self, scorer):
        """Score must always be 0-100."""
        result = scorer.score({
            "business_name": "Test",
            "town": "London",
        })
        assert 0 <= result["score"] <= 100

    def test_full_contact_info_scores_higher(self, scorer):
        """Leads with more contact info should score higher."""
        minimal = scorer.score({
            "business_name": "Test Biz",
            "town": "London",
        })
        rich = scorer.score({
            "business_name": "Test Biz",
            "town": "London",
            "email": "test@example.com",
            "phone": "+44 20 1234 5678",
            "owner_name": "Jane Smith",
            "website": "https://testbiz.co.uk",
        })
        assert rich["score"] > minimal["score"]

    def test_website_quality_signals(self, scorer):
        """Website quality signals should affect score."""
        with_ssl = scorer.score({
            "business_name": "Test",
            "town": "London",
            "website": "https://example.com",
            "website_has_ssl": True,
        })
        without_ssl = scorer.score({
            "business_name": "Test",
            "town": "London",
            "website": "http://example.com",
            "website_has_ssl": False,
        })
        assert with_ssl["score"] >= without_ssl["score"]

    def test_business_signals_rating(self, scorer):
        """Higher-rated businesses should score higher."""
        high_rated = scorer.score({
            "business_name": "Great Biz",
            "town": "London",
            "rating": 4.5,
            "review_count": 50,
        })
        low_rated = scorer.score({
            "business_name": "Poor Biz",
            "town": "London",
            "rating": 2.0,
            "review_count": 3,
        })
        assert high_rated["score"] > low_rated["score"]

    def test_negative_signals_reduce_score(self, scorer):
        """No website and very low rating should produce low score."""
        bad_lead = scorer.score({
            "business_name": "Bad Lead",
            "town": "London",
            "rating": 1.5,
            "review_count": 1,
        })
        assert bad_lead["score"] < 30

    def test_score_returns_breakdown(self, scorer):
        """Score result should include component breakdown."""
        result = scorer.score({
            "business_name": "Test",
            "town": "London",
            "email": "test@example.com",
        })
        assert "score" in result
        assert "breakdown" in result
        assert isinstance(result["breakdown"], dict)

    def test_score_perfect_lead(self, scorer):
        """A perfect lead should score near maximum."""
        result = scorer.score({
            "business_name": "Premium Restaurant",
            "town": "Bristol",
            "owner_name": "John Smith",
            "email": "john@premium.co.uk",
            "phone": "+44 117 123 4567",
            "website": "https://premium.co.uk",
            "website_has_ssl": True,
            "website_is_mobile_friendly": True,
            "rating": 4.8,
            "review_count": 200,
            "has_social_media": True,
        })
        assert result["score"] >= 70

    def test_score_clamped_to_100(self, scorer):
        """Score should never exceed 100 even with all positive signals."""
        result = scorer.score({
            "business_name": "Best Biz Ever",
            "town": "London",
            "owner_name": "Owner",
            "email": "owner@best.co.uk",
            "phone": "+44 20 1234 5678",
            "website": "https://best.co.uk",
            "website_has_ssl": True,
            "website_is_mobile_friendly": True,
            "rating": 5.0,
            "review_count": 500,
            "has_social_media": True,
        })
        assert result["score"] <= 100
