"""Tests for FastAPI REST API (F003, F021, F023)."""

import pytest
from httpx import ASGITransport, AsyncClient
from src.outlocal.api.main import app, db


@pytest.fixture
async def client(tmp_path):
    """Create async test client with initialized in-memory DB."""
    db._db_path = str(tmp_path / "test_api.db")
    db._conn = None  # Reset any existing connection
    await db.init_db()
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
    await db.close()


class TestHealthCheck:
    """Tests for health check endpoint."""

    @pytest.mark.asyncio
    async def test_health_returns_200(self, client):
        response = await client.get("/health")
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_health_returns_status(self, client):
        data = (await client.get("/health")).json()
        assert data["status"] == "healthy"

    @pytest.mark.asyncio
    async def test_health_returns_version(self, client):
        data = (await client.get("/health")).json()
        assert "version" in data


class TestAPIStructure:
    @pytest.mark.asyncio
    async def test_openapi_docs_available(self, client):
        response = await client.get("/docs")
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_api_v1_leads_endpoint(self, client):
        response = await client.get("/api/v1/leads")
        assert response.status_code == 200


class TestLeadsCRUD:
    """Tests for lead CRUD endpoints (F021)."""

    @pytest.mark.asyncio
    async def test_create_lead(self, client):
        response = await client.post(
            "/api/v1/leads",
            json={
                "business_name": "Test Pub",
                "town": "Bristol",
                "source": "manual",
            },
        )
        assert response.status_code == 201
        data = response.json()
        assert "id" in data

    @pytest.mark.asyncio
    async def test_list_leads_returns_list(self, client):
        response = await client.get("/api/v1/leads")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @pytest.mark.asyncio
    async def test_get_lead_not_found(self, client):
        response = await client.get("/api/v1/leads/99999")
        assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_create_and_get_lead(self, client):
        create = await client.post(
            "/api/v1/leads",
            json={
                "business_name": "Crown Inn",
                "town": "Bath",
                "email": "info@crowninn.co.uk",
            },
        )
        lead_id = create.json()["id"]

        get = await client.get(f"/api/v1/leads/{lead_id}")
        assert get.status_code == 200
        assert get.json()["business_name"] == "Crown Inn"

    @pytest.mark.asyncio
    async def test_update_lead(self, client):
        create = await client.post(
            "/api/v1/leads",
            json={
                "business_name": "Update Test",
                "town": "London",
            },
        )
        lead_id = create.json()["id"]

        update = await client.put(
            f"/api/v1/leads/{lead_id}",
            json={
                "email": "new@example.com",
            },
        )
        assert update.status_code == 200

    @pytest.mark.asyncio
    async def test_delete_lead_soft(self, client):
        create = await client.post(
            "/api/v1/leads",
            json={
                "business_name": "Delete Test",
                "town": "London",
            },
        )
        lead_id = create.json()["id"]

        delete = await client.delete(f"/api/v1/leads/{lead_id}")
        assert delete.status_code == 200


class TestCampaignsCRUD:
    """Tests for campaign endpoints (F016)."""

    @pytest.mark.asyncio
    async def test_create_campaign(self, client):
        response = await client.post(
            "/api/v1/campaigns",
            json={
                "name": "Bristol Q1",
                "target_criteria": {"town": "Bristol"},
            },
        )
        assert response.status_code == 201
        assert "id" in response.json()

    @pytest.mark.asyncio
    async def test_list_campaigns(self, client):
        response = await client.get("/api/v1/campaigns")
        assert response.status_code == 200
        assert isinstance(response.json(), list)


class TestComplianceEndpoints:
    """Tests for compliance endpoints (F023)."""

    @pytest.mark.asyncio
    async def test_unsubscribe_endpoint(self, client):
        response = await client.post("/api/v1/compliance/unsubscribe/test@example.com")
        assert response.status_code == 200
        assert response.json()["status"] == "unsubscribed"

    @pytest.mark.asyncio
    async def test_erasure_endpoint(self, client):
        response = await client.post(
            "/api/v1/compliance/erasure",
            json={
                "email": "erase@example.com",
            },
        )
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_audit_trail_endpoint(self, client):
        response = await client.get("/api/v1/compliance/audit/test@example.com")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
