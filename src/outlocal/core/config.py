"""Configuration management for OUTLOCAL.

Loads settings from environment variables via pydantic-settings.
Provider configs for the free LLM failover chain.
"""

from functools import lru_cache
from typing import Any

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # App
    app_env: str = "development"
    app_port: int = 8000
    app_host: str = "0.0.0.0"

    # Database
    database_url: str = "sqlite:///./outlocal.db"

    # AI Providers (all free, no credit card)
    groq_api_key: str | None = None
    openrouter_api_key: str | None = None
    gemini_api_key: str | None = None

    # SMTP
    smtp_host: str | None = None
    smtp_port: int = 587
    smtp_user: str | None = None
    smtp_password: str | None = None
    smtp_from_email: str | None = None
    smtp_from_name: str | None = None

    # Google Maps
    google_places_api_key: str | None = None

    # Compliance
    business_address: str = ""
    unsubscribe_url: str = ""

    def get_provider_configs(self) -> list[dict[str, Any]]:
        """Get LLM provider configs ordered by priority.

        Returns all providers; callers should skip those with api_key=None.
        """
        return [
            {
                "name": "groq",
                "base_url": "https://api.groq.com/openai/v1",
                "api_key": self.groq_api_key,
                "model": "llama-3.3-70b-versatile",
                "daily_limit": 1000,
                "rpm": 30,
            },
            {
                "name": "openrouter",
                "base_url": "https://openrouter.ai/api/v1",
                "api_key": self.openrouter_api_key,
                "model": "meta-llama/llama-3.3-70b-instruct:free",
                "daily_limit": 200,
                "rpm": 20,
            },
            {
                "name": "gemini",
                "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/",
                "api_key": self.gemini_api_key,
                "model": "gemini-2.5-flash",
                "daily_limit": 250,
                "rpm": 10,
            },
        ]


@lru_cache
def get_settings() -> Settings:
    """Get cached settings singleton."""
    return Settings()
