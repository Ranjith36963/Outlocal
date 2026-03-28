"""Tests for async SMTP email sender (F010)."""

from datetime import UTC, datetime
from unittest.mock import AsyncMock, patch

import pytest
from src.outlocal.email_sender.sender import EmailSender, SendResult


@pytest.fixture
def sender():
    return EmailSender(
        host="smtp.test.com",
        port=587,
        username="test@test.com",
        password="secret",
        from_email="sender@test.com",
        from_name="Test Sender",
        unsubscribe_url="https://test.com/unsubscribe",
        business_address="123 Test St, London, UK",
    )


class TestEmailSender:
    """Tests for email sending."""

    @pytest.mark.asyncio
    async def test_send_returns_send_result(self, sender):
        with patch("src.outlocal.email_sender.sender.aiosmtplib.send", new_callable=AsyncMock):
            result = await sender.send(
                to_email="recipient@example.com",
                subject="Test Subject",
                body="Test body content",
            )
        assert isinstance(result, SendResult)

    @pytest.mark.asyncio
    async def test_send_success_status(self, sender):
        with patch("src.outlocal.email_sender.sender.aiosmtplib.send", new_callable=AsyncMock):
            result = await sender.send(
                to_email="recipient@example.com",
                subject="Test",
                body="Body",
            )
        assert result.status == "sent"
        assert result.sent_at is not None

    @pytest.mark.asyncio
    async def test_send_failure_status(self, sender):
        with patch(
            "src.outlocal.email_sender.sender.aiosmtplib.send",
            new_callable=AsyncMock,
            side_effect=Exception("SMTP connection failed"),
        ):
            result = await sender.send(
                to_email="recipient@example.com",
                subject="Test",
                body="Body",
            )
        assert result.status == "failed"
        assert "SMTP connection failed" in result.error

    @pytest.mark.asyncio
    async def test_send_includes_unsubscribe_header(self, sender):
        with patch(
            "src.outlocal.email_sender.sender.aiosmtplib.send", new_callable=AsyncMock
        ) as mock_send:
            await sender.send(
                to_email="recipient@example.com",
                subject="Test",
                body="Body",
            )
        # Check the message object passed to send
        call_args = mock_send.call_args
        message = call_args.kwargs.get("message") or call_args.args[0]
        assert "List-Unsubscribe" in str(message)

    @pytest.mark.asyncio
    async def test_send_includes_physical_address_in_body(self, sender):
        with patch(
            "src.outlocal.email_sender.sender.aiosmtplib.send", new_callable=AsyncMock
        ) as mock_send:
            await sender.send(
                to_email="recipient@example.com",
                subject="Test",
                body="Hello there",
            )
        call_args = mock_send.call_args
        message = call_args.kwargs.get("message") or call_args.args[0]
        # Physical address should be in the email content
        payload = message.get_payload()
        if isinstance(payload, list):
            text_parts = [p.get_payload() for p in payload]
            full_text = " ".join(str(t) for t in text_parts)
        else:
            full_text = str(payload)
        assert "123 Test St" in full_text


class TestRateLimiting:
    """Tests for send rate limiting."""

    @pytest.mark.asyncio
    async def test_rate_limit_respected(self, sender):
        """Should track send count for rate limiting."""
        sender._rate_limit_per_minute = 2
        with patch("src.outlocal.email_sender.sender.aiosmtplib.send", new_callable=AsyncMock):
            result1 = await sender.send("a@b.com", "Test 1", "Body")
            result2 = await sender.send("c@d.com", "Test 2", "Body")
        assert result1.status == "sent"
        assert result2.status == "sent"

    def test_send_result_has_required_fields(self):
        result = SendResult(
            status="sent",
            sent_at=datetime.now(UTC),
        )
        assert result.status == "sent"
        assert result.sent_at is not None
        assert result.error is None
