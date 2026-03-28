"""Tests for core data models and database schema (F001)."""

import pytest
from datetime import datetime, timezone
from pydantic import ValidationError

from src.outlocal.core.models import (
    Lead,
    LeadStatus,
    Campaign,
    CampaignStatus,
    Email,
    EmailStatus,
    Reply,
    ReplyClassification,
)


class TestLeadModel:
    """Tests for the Lead Pydantic model."""

    def test_lead_creation_with_required_fields(self):
        lead = Lead(
            business_name="Joe's Fish & Chips",
            town="Bristol",
            source="google_maps",
        )
        assert lead.business_name == "Joe's Fish & Chips"
        assert lead.town == "Bristol"
        assert lead.source == "google_maps"
        assert lead.status == LeadStatus.NEW

    def test_lead_creation_with_all_fields(self):
        lead = Lead(
            business_name="The Crown Pub",
            owner_name="James Wilson",
            email="james@crownpub.co.uk",
            phone="+44 117 123 4567",
            website="https://crownpub.co.uk",
            town="Bath",
            source="google_maps",
            score=75,
            status=LeadStatus.ENRICHED,
        )
        assert lead.owner_name == "James Wilson"
        assert lead.email == "james@crownpub.co.uk"
        assert lead.score == 75
        assert lead.status == LeadStatus.ENRICHED

    def test_lead_score_must_be_0_to_100(self):
        with pytest.raises(ValidationError):
            Lead(
                business_name="Test",
                town="London",
                source="manual",
                score=150,
            )

    def test_lead_score_negative_rejected(self):
        with pytest.raises(ValidationError):
            Lead(
                business_name="Test",
                town="London",
                source="manual",
                score=-1,
            )

    def test_lead_default_status_is_new(self):
        lead = Lead(business_name="Test", town="London", source="manual")
        assert lead.status == LeadStatus.NEW

    def test_lead_optional_fields_default_none(self):
        lead = Lead(business_name="Test", town="London", source="manual")
        assert lead.owner_name is None
        assert lead.email is None
        assert lead.phone is None
        assert lead.website is None
        assert lead.score is None

    def test_lead_statuses_exist(self):
        assert LeadStatus.NEW == "new"
        assert LeadStatus.ENRICHED == "enriched"
        assert LeadStatus.SCORED == "scored"
        assert LeadStatus.CONTACTED == "contacted"
        assert LeadStatus.REPLIED == "replied"
        assert LeadStatus.INTERESTED == "interested"
        assert LeadStatus.CONVERTED == "converted"
        assert LeadStatus.LOST == "lost"
        assert LeadStatus.UNSUBSCRIBED == "unsubscribed"


class TestCampaignModel:
    """Tests for the Campaign Pydantic model."""

    def test_campaign_creation(self):
        campaign = Campaign(
            name="Bristol Restaurants Q1",
            target_criteria={"town": "Bristol", "business_type": "restaurant"},
        )
        assert campaign.name == "Bristol Restaurants Q1"
        assert campaign.status == CampaignStatus.DRAFT
        assert campaign.target_criteria == {"town": "Bristol", "business_type": "restaurant"}

    def test_campaign_with_template(self):
        campaign = Campaign(
            name="Test Campaign",
            template="intro_email",
            target_criteria={"town": "London"},
        )
        assert campaign.template == "intro_email"

    def test_campaign_created_at_auto_set(self):
        campaign = Campaign(name="Test", target_criteria={})
        assert campaign.created_at is not None
        assert isinstance(campaign.created_at, datetime)

    def test_campaign_statuses_exist(self):
        assert CampaignStatus.DRAFT == "draft"
        assert CampaignStatus.ACTIVE == "active"
        assert CampaignStatus.PAUSED == "paused"
        assert CampaignStatus.COMPLETED == "completed"


class TestEmailModel:
    """Tests for the Email Pydantic model."""

    def test_email_creation(self):
        email = Email(
            lead_id=1,
            campaign_id=1,
            subject="Quick question about Crown Pub's website",
            body="Hi James, I noticed your website...",
            provider="groq",
        )
        assert email.lead_id == 1
        assert email.subject == "Quick question about Crown Pub's website"
        assert email.status == EmailStatus.DRAFT

    def test_email_with_timestamps(self):
        now = datetime.now(timezone.utc)
        email = Email(
            lead_id=1,
            campaign_id=1,
            subject="Test",
            body="Test body",
            provider="groq",
            status=EmailStatus.SENT,
            sent_at=now,
        )
        assert email.sent_at == now
        assert email.opened_at is None
        assert email.clicked_at is None

    def test_email_statuses_exist(self):
        assert EmailStatus.DRAFT == "draft"
        assert EmailStatus.SENT == "sent"
        assert EmailStatus.FAILED == "failed"
        assert EmailStatus.BOUNCED == "bounced"

    def test_email_requires_lead_and_campaign(self):
        with pytest.raises(ValidationError):
            Email(
                subject="Test",
                body="Test",
                provider="groq",
            )


class TestReplyModel:
    """Tests for the Reply Pydantic model."""

    def test_reply_creation(self):
        reply = Reply(
            email_id=1,
            raw_text="Yes, I'd love to hear more about your services.",
        )
        assert reply.email_id == 1
        assert reply.raw_text == "Yes, I'd love to hear more about your services."
        assert reply.classification is None
        assert reply.classified_at is None

    def test_reply_with_classification(self):
        now = datetime.now(timezone.utc)
        reply = Reply(
            email_id=1,
            raw_text="Not interested, thanks.",
            classification=ReplyClassification.NOT_INTERESTED,
            classified_at=now,
        )
        assert reply.classification == ReplyClassification.NOT_INTERESTED
        assert reply.classified_at == now

    def test_reply_classifications_exist(self):
        assert ReplyClassification.INTERESTED == "interested"
        assert ReplyClassification.NOT_INTERESTED == "not_interested"
        assert ReplyClassification.OUT_OF_OFFICE == "out_of_office"
        assert ReplyClassification.WRONG_PERSON == "wrong_person"
        assert ReplyClassification.UNSUBSCRIBE == "unsubscribe"
