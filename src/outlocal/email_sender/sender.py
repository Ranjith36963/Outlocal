"""Async SMTP email sender for OUTLOCAL.

Sends cold emails with rate limiting, CAN-SPAM compliance headers,
and error handling.
"""

import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from email.message import EmailMessage

import aiosmtplib

logger = logging.getLogger(__name__)


@dataclass
class SendResult:
    """Result of an email send attempt."""

    status: str  # "sent", "failed", "bounced", "rate_limited"
    sent_at: datetime | None = None
    error: str | None = None


class EmailSender:
    """Async SMTP email sender with rate limiting and CAN-SPAM compliance."""

    def __init__(
        self,
        host: str,
        port: int = 587,
        username: str | None = None,
        password: str | None = None,
        from_email: str = "",
        from_name: str = "",
        unsubscribe_url: str = "",
        business_address: str = "",
        rate_limit_per_minute: int = 2,
    ) -> None:
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._from_email = from_email
        self._from_name = from_name
        self._unsubscribe_url = unsubscribe_url
        self._business_address = business_address
        self._rate_limit_per_minute = rate_limit_per_minute
        self._send_count_this_minute = 0

    def _build_message(
        self,
        to_email: str,
        subject: str,
        body: str,
        unsubscribe_token: str | None = None,
    ) -> EmailMessage:
        """Build an email message with CAN-SPAM compliance headers."""
        msg = EmailMessage()
        msg["From"] = f"{self._from_name} <{self._from_email}>"
        msg["To"] = to_email
        msg["Subject"] = subject

        # CAN-SPAM: Unsubscribe header
        unsub_url = self._unsubscribe_url
        if unsubscribe_token:
            unsub_url = f"{unsub_url}/{unsubscribe_token}"
        msg["List-Unsubscribe"] = f"<{unsub_url}>"
        msg["List-Unsubscribe-Post"] = "List-Unsubscribe=One-Click"

        # CAN-SPAM: Physical address in footer
        footer = (
            f"\n\n---\n"
            f"{self._business_address}\n"
            f"Unsubscribe: {unsub_url}"
        )
        full_body = body + footer
        msg.set_content(full_body)

        return msg

    async def send(
        self,
        to_email: str,
        subject: str,
        body: str,
        unsubscribe_token: str | None = None,
    ) -> SendResult:
        """Send an email via SMTP.

        Returns SendResult with status and timestamp.
        """
        msg = self._build_message(to_email, subject, body, unsubscribe_token)

        try:
            await aiosmtplib.send(
                message=msg,
                hostname=self._host,
                port=self._port,
                username=self._username,
                password=self._password,
                start_tls=True,
            )
            self._send_count_this_minute += 1
            logger.info("Email sent to %s: %s", to_email, subject)

            return SendResult(
                status="sent",
                sent_at=datetime.now(timezone.utc),
            )
        except Exception as e:
            logger.error("Failed to send to %s: %s", to_email, e)
            return SendResult(
                status="failed",
                error=str(e),
            )
