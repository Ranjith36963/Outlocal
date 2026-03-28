"""Tests for FastAPI application skeleton (F003)."""

import pytest
from httpx import AsyncClient, ASGITransport

from src.outlocal.api.main import app


@pytest.fixture
async def client():
    """Create async test client for the FastAPI app."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


class TestHealthCheck:
    """Tests for health check endpoint."""

    @pytest.mark.asyncio
    async def test_health_returns_200(self, client):
        response = await client.get("/health")
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_health_returns_status(self, client):
        response = await client.get("/health")
        data = response.json()
        assert data["status"] == "healthy"

    @pytest.mark.asyncio
    async def test_health_returns_version(self, client):
        response = await client.get("/health")
        data = response.json()
        assert "version" in data


class TestAPIStructure:
    """Tests for API versioning and docs."""

    @pytest.mark.asyncio
    async def test_openapi_docs_available(self, client):
        response = await client.get("/docs")
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_api_v1_prefix_exists(self, client):
        """API v1 routes should be accessible under /api/v1."""
        response = await client.get("/api/v1/leads")
        # Should return 200 (empty list), not 404
        assert response.status_code == 200
