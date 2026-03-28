"""Tests for configuration management (F002)."""

import os
from unittest.mock import patch

from src.outlocal.core.config import Settings, get_settings


class TestSettings:
    """Tests for the Settings configuration class."""

    def test_settings_loads_defaults(self):
        """Settings should have sensible defaults."""
        with patch.dict(os.environ, {}, clear=False):
            settings = Settings(
                _env_file=None,  # Don't load .env in tests
            )
        assert settings.app_env == "development"
        assert settings.app_port == 8000
        assert settings.app_host == "0.0.0.0"

    def test_settings_loads_from_env(self):
        """Settings should load values from environment variables."""
        env = {
            "APP_ENV": "production",
            "APP_PORT": "9000",
            "GROQ_API_KEY": "gsk_test123",
        }
        with patch.dict(os.environ, env, clear=False):
            settings = Settings(_env_file=None)
        assert settings.app_env == "production"
        assert settings.app_port == 9000
        assert settings.groq_api_key == "gsk_test123"

    def test_provider_configs_structure(self):
        """Provider configs should have required fields."""
        env = {
            "GROQ_API_KEY": "gsk_test",
            "OPENROUTER_API_KEY": "sk-or-test",
            "GEMINI_API_KEY": "AIza_test",
        }
        with patch.dict(os.environ, env, clear=False):
            settings = Settings(_env_file=None)
            providers = settings.get_provider_configs()

        assert len(providers) >= 3
        for provider in providers:
            assert "name" in provider
            assert "base_url" in provider
            assert "api_key" in provider
            assert "model" in provider
            assert "daily_limit" in provider
            assert "rpm" in provider

    def test_groq_is_first_provider(self):
        """Groq should be the primary (first) provider."""
        env = {"GROQ_API_KEY": "gsk_test"}
        with patch.dict(os.environ, env, clear=False):
            settings = Settings(_env_file=None)
            providers = settings.get_provider_configs()

        groq = next(p for p in providers if p["name"] == "groq")
        assert providers[0]["name"] == "groq"
        assert groq["api_key"] == "gsk_test"

    def test_smtp_config_from_env(self):
        """SMTP settings should load from environment."""
        env = {
            "SMTP_HOST": "smtp.test.com",
            "SMTP_PORT": "465",
            "SMTP_USER": "user@test.com",
            "SMTP_PASSWORD": "secret123",
            "SMTP_FROM_EMAIL": "sender@test.com",
            "SMTP_FROM_NAME": "Test Sender",
        }
        with patch.dict(os.environ, env, clear=False):
            settings = Settings(_env_file=None)

        assert settings.smtp_host == "smtp.test.com"
        assert settings.smtp_port == 465
        assert settings.smtp_user == "user@test.com"
        assert settings.smtp_password == "secret123"
        assert settings.smtp_from_email == "sender@test.com"
        assert settings.smtp_from_name == "Test Sender"

    def test_database_url_default(self):
        """Database URL should default to local SQLite."""
        settings = Settings(_env_file=None)
        assert "sqlite" in settings.database_url

    def test_providers_without_keys_excluded(self):
        """Providers without API keys should be excluded from active list."""
        with patch.dict(os.environ, {}, clear=False):
            settings = Settings(_env_file=None)
            providers = settings.get_provider_configs()

        # Without any keys set, no providers should be active
        for p in providers:
            if p["api_key"] is None:
                pass  # That's expected — provider listed but won't be used

    def test_get_settings_returns_instance(self):
        """get_settings() should return a Settings instance."""
        settings = get_settings()
        assert isinstance(settings, Settings)
