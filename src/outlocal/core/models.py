"""Core data models for OUTLOCAL.

Pydantic v2 models for leads, campaigns, emails, and replies.
These define the data contract — all data flowing through the pipeline
must conform to these models.
"""

from datetime import UTC, datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field


class LeadStatus(StrEnum):
    """Lead lifecycle statuses."""

    NEW = "new"
    ENRICHED = "enriched"
    SCORED = "scored"
    CONTACTED = "contacted"
    REPLIED = "replied"
    INTERESTED = "interested"
    CONVERTED = "converted"
    LOST = "lost"
    UNSUBSCRIBED = "unsubscribed"


class CampaignStatus(StrEnum):
    """Campaign lifecycle statuses."""

    DRAFT = "draft"
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"


class EmailStatus(StrEnum):
    """Email delivery statuses."""

    DRAFT = "draft"
    PENDING = "pending"
    SENT = "sent"
    FAILED = "failed"
    BOUNCED = "bounced"


class ReplyClassification(StrEnum):
    """Reply intent classifications."""

    INTERESTED = "interested"
    NOT_INTERESTED = "not_interested"
    OUT_OF_OFFICE = "out_of_office"
    WRONG_PERSON = "wrong_person"
    UNSUBSCRIBE = "unsubscribe"


class Lead(BaseModel):
    """A business lead scraped from Google Maps or other sources."""

    id: int | None = None
    business_name: str
    owner_name: str | None = None
    email: str | None = None
    phone: str | None = None
    website: str | None = None
    town: str
    source: str
    score: int | None = Field(default=None, ge=0, le=100)
    status: LeadStatus = LeadStatus.NEW
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class Campaign(BaseModel):
    """A cold outreach campaign targeting a set of leads."""

    id: int | None = None
    name: str
    status: CampaignStatus = CampaignStatus.DRAFT
    template: str | None = None
    target_criteria: dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class Email(BaseModel):
    """An email generated and sent to a lead."""

    id: int | None = None
    lead_id: int
    campaign_id: int
    subject: str
    body: str
    provider: str
    status: EmailStatus = EmailStatus.DRAFT
    sent_at: datetime | None = None
    opened_at: datetime | None = None
    clicked_at: datetime | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class Reply(BaseModel):
    """A reply received from a lead."""

    id: int | None = None
    email_id: int
    raw_text: str
    classification: ReplyClassification | None = None
    classified_at: datetime | None = None
    received_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class AuditLogEntry(BaseModel):
    """An audit log entry tracking actions on entities."""

    id: int | None = None
    entity_type: str
    entity_id: int
    action: str
    details: str | None = None
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))
