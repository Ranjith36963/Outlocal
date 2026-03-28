"""Background scheduler for automated pipeline operations.

Uses APScheduler for recurring tasks: follow-up checks,
daily counter resets, IMAP polling, batch enrichment.
"""

import logging
from collections.abc import Callable, Coroutine
from typing import Any

from apscheduler.schedulers.asyncio import AsyncIOScheduler

logger = logging.getLogger(__name__)


class PipelineScheduler:
    """Background scheduler for automated pipeline operations."""

    def __init__(self) -> None:
        self._scheduler = AsyncIOScheduler()
        self._jobs: dict[str, str] = {}

    def add_interval_job(
        self,
        func: Callable[..., Coroutine[Any, Any, None]],
        job_id: str,
        minutes: int = 5,
        **kwargs: Any,
    ) -> None:
        """Add a recurring job that runs every N minutes."""
        self._scheduler.add_job(
            func,
            "interval",
            minutes=minutes,
            id=job_id,
            replace_existing=True,
            **kwargs,
        )
        self._jobs[job_id] = f"every {minutes} min"
        logger.info("Scheduled job %s: every %d minutes", job_id, minutes)

    def add_daily_job(
        self,
        func: Callable[..., Coroutine[Any, Any, None]],
        job_id: str,
        hour: int = 0,
        minute: int = 0,
        **kwargs: Any,
    ) -> None:
        """Add a job that runs daily at a specific time."""
        self._scheduler.add_job(
            func,
            "cron",
            hour=hour,
            minute=minute,
            id=job_id,
            replace_existing=True,
            **kwargs,
        )
        self._jobs[job_id] = f"daily at {hour:02d}:{minute:02d}"
        logger.info("Scheduled job %s: daily at %02d:%02d", job_id, hour, minute)

    def start(self) -> None:
        """Start the scheduler."""
        if not self._scheduler.running:
            self._scheduler.start()
            logger.info("Scheduler started with %d jobs", len(self._jobs))

    def shutdown(self) -> None:
        """Gracefully shutdown the scheduler."""
        if self._scheduler.running:
            self._scheduler.shutdown(wait=False)
            logger.info("Scheduler stopped")

    def get_status(self) -> dict[str, Any]:
        """Get scheduler status and job list."""
        return {
            "running": self._scheduler.running,
            "jobs": self._jobs,
        }
