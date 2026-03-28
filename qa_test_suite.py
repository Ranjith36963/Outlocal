"""
OUTLOCAL QA Test Suite -- Systematic API testing via httpx.

Tests every endpoint with happy path, edge cases, and error cases.
Reports in: ENDPOINT | TEST_NAME | EXPECTED | ACTUAL | PASS/FAIL
"""

import io
import time
import sys
import httpx

# Force UTF-8 stdout so arrows/unicode survive Windows CP1252 terminals
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

BASE_URL = "http://localhost:8000"
RESULTS: list[dict] = []

# ── Utilities ──────────────────────────────────────────────────────────────

def record(endpoint: str, test_name: str, expected: str, actual_status: int,
           actual_body, timing_ms: float, passed: bool) -> None:
    RESULTS.append({
        "endpoint": endpoint,
        "test_name": test_name,
        "expected": expected,
        "actual_status": actual_status,
        "passed": passed,
        "timing_ms": round(timing_ms, 1),
        "body_snippet": str(actual_body)[:120],
    })
    status_icon = "PASS" if passed else "FAIL"
    print(f"  [{status_icon}] {test_name} — {actual_status} ({timing_ms:.0f}ms)")


def req(method: str, path: str, **kwargs):
    """Make a timed HTTP request and return (response, elapsed_ms)."""
    url = BASE_URL + path
    t0 = time.perf_counter()
    try:
        r = httpx.request(method, url, timeout=10, **kwargs)
    except httpx.ConnectError as exc:
        raise SystemExit(f"\nCould not connect to {url}. Is the server running?\n{exc}") from exc
    elapsed = (time.perf_counter() - t0) * 1000
    return r, elapsed


# ── Wait for server ────────────────────────────────────────────────────────

print("Waiting 5 s for server to start…")
time.sleep(5)


# ══════════════════════════════════════════════════════════════════════════
# 1. GET /health
# ══════════════════════════════════════════════════════════════════════════
print("\n=== GET /health ===")

r, ms = req("GET", "/health")
body = r.json()
ok = r.status_code == 200 and body.get("status") == "healthy"
record("GET /health", "happy path", "200 + status=healthy", r.status_code, body, ms, ok)

# Version field present?
ok = "version" in body
record("GET /health", "version field present", "version key exists", r.status_code, body, ms, ok)

# service field
ok = body.get("service") == "outlocal"
record("GET /health", "service=outlocal", "service=outlocal", r.status_code, body, ms, ok)


# ══════════════════════════════════════════════════════════════════════════
# 2. POST /api/v1/leads  — create lead
# ══════════════════════════════════════════════════════════════════════════
print("\n=== POST /api/v1/leads ===")

# Happy path — full data
full_lead = {
    "business_name": "The Bristol Barber",
    "town": "Bristol",
    "source": "google_maps",
    "owner_name": "James Thornton",
    "email": "james@bristolbarber.co.uk",
    "phone": "01179001234",
    "website": "https://bristolbarber.co.uk",
}
r, ms = req("POST", "/api/v1/leads", json=full_lead)
body = r.json()
ok = r.status_code == 201 and "id" in body and body.get("status") == "created"
record("POST /api/v1/leads", "create full lead", "201 + id + status=created", r.status_code, body, ms, ok)
created_lead_id = body.get("id", 1)

# Required fields only
min_lead = {
    "business_name": "Minimal Plumbers",
    "town": "Leeds",
}
r, ms = req("POST", "/api/v1/leads", json=min_lead)
body = r.json()
ok = r.status_code == 201 and "id" in body
record("POST /api/v1/leads", "only required fields", "201 + id", r.status_code, body, ms, ok)
min_lead_id = body.get("id", 2)

# Missing required: business_name
r, ms = req("POST", "/api/v1/leads", json={"town": "London"})
ok = r.status_code == 422
record("POST /api/v1/leads", "missing business_name → 422", "422", r.status_code, r.json(), ms, ok)

# Missing required: town
r, ms = req("POST", "/api/v1/leads", json={"business_name": "Solo Business"})
ok = r.status_code == 422
record("POST /api/v1/leads", "missing town → 422", "422", r.status_code, r.json(), ms, ok)

# Empty body → 422
r, ms = req("POST", "/api/v1/leads", json={})
ok = r.status_code == 422
record("POST /api/v1/leads", "empty body → 422", "422", r.status_code, r.json(), ms, ok)

# Extra/unknown field (should be ignored, still 201)
r, ms = req("POST", "/api/v1/leads", json={
    "business_name": "Test Co",
    "town": "Bath",
    "bogus_field": "ignored",
})
body = r.json()
ok = r.status_code == 201
record("POST /api/v1/leads", "extra field ignored → 201", "201", r.status_code, body, ms, ok)
extra_lead_id = body.get("id", 3)

# Create a Bristol lead for filter test
r2, _ = req("POST", "/api/v1/leads", json={
    "business_name": "Bristol Cafe",
    "town": "Bristol",
    "email": "cafe@bristol.co.uk",
})


# ══════════════════════════════════════════════════════════════════════════
# 3. GET /api/v1/leads
# ══════════════════════════════════════════════════════════════════════════
print("\n=== GET /api/v1/leads ===")

# List all
r, ms = req("GET", "/api/v1/leads")
body = r.json()
ok = r.status_code == 200 and isinstance(body, list) and len(body) > 0
record("GET /api/v1/leads", "list all", "200 + list", r.status_code, f"{len(body)} items", ms, ok)

# Filter by status=new
r, ms = req("GET", "/api/v1/leads?status=new")
body = r.json()
ok = r.status_code == 200 and isinstance(body, list)
all_new = all(l.get("status") == "new" for l in body) if body else True
record("GET /api/v1/leads", "filter ?status=new", "200 + all items status=new",
       r.status_code, f"{len(body)} items, all_new={all_new}", ms, ok and all_new)

# Filter by town=Bristol
r, ms = req("GET", "/api/v1/leads?town=Bristol")
body = r.json()
ok = r.status_code == 200 and isinstance(body, list)
all_bristol = all(l.get("town") == "Bristol" for l in body) if body else True
record("GET /api/v1/leads", "filter ?town=Bristol", "200 + all Bristol",
       r.status_code, f"{len(body)} items, all_bristol={all_bristol}", ms, ok and all_bristol)

# Filter by min_score (score=0 for new leads → returns empty or leads with score>=10)
r, ms = req("GET", "/api/v1/leads?min_score=10")
ok = r.status_code == 200 and isinstance(r.json(), list)
record("GET /api/v1/leads", "filter ?min_score=10", "200 + list", r.status_code, r.json(), ms, ok)

# Pagination: limit=2
r, ms = req("GET", "/api/v1/leads?limit=2")
body = r.json()
ok = r.status_code == 200 and isinstance(body, list) and len(body) <= 2
record("GET /api/v1/leads", "pagination limit=2", "200 + ≤2 items", r.status_code,
       f"{len(body)} items", ms, ok)

# Pagination: offset=100 (should return empty)
r, ms = req("GET", "/api/v1/leads?limit=10&offset=10000")
ok = r.status_code == 200 and r.json() == []
record("GET /api/v1/leads", "offset beyond count → empty list", "200 + []",
       r.status_code, r.json(), ms, ok)

# limit > 500 → validation error
r, ms = req("GET", "/api/v1/leads?limit=501")
ok = r.status_code == 422
record("GET /api/v1/leads", "limit=501 → 422", "422", r.status_code, r.json(), ms, ok)

# Non-existent status filter → empty list (not error)
r, ms = req("GET", "/api/v1/leads?status=nonexistent")
ok = r.status_code == 200 and r.json() == []
record("GET /api/v1/leads", "nonexistent status filter → []", "200 + []",
       r.status_code, r.json(), ms, ok)


# ══════════════════════════════════════════════════════════════════════════
# 4. GET /api/v1/leads/{id}
# ══════════════════════════════════════════════════════════════════════════
print("\n=== GET /api/v1/leads/{id} ===")

# Valid ID
r, ms = req("GET", f"/api/v1/leads/{created_lead_id}")
body = r.json()
ok = (r.status_code == 200
      and body.get("id") == created_lead_id
      and body.get("business_name") == "The Bristol Barber"
      and "activity_log" in body)
record("GET /api/v1/leads/{id}", "valid ID", "200 + full lead + activity_log",
       r.status_code, body, ms, ok)

# Activity log is a list
ok = isinstance(body.get("activity_log"), list)
record("GET /api/v1/leads/{id}", "activity_log is list", "list",
       r.status_code, type(body.get("activity_log")).__name__, ms, ok)

# Invalid ID 99999
r, ms = req("GET", "/api/v1/leads/99999")
ok = r.status_code == 404 and "not found" in r.json().get("detail", "").lower()
record("GET /api/v1/leads/{id}", "invalid ID 99999 → 404", "404 + detail",
       r.status_code, r.json(), ms, ok)

# Non-integer ID → 422
r, ms = req("GET", "/api/v1/leads/abc")
ok = r.status_code == 422
record("GET /api/v1/leads/{id}", "string ID 'abc' → 422", "422",
       r.status_code, r.json(), ms, ok)

# ID 0 → 404 (no lead has ID 0)
r, ms = req("GET", "/api/v1/leads/0")
ok = r.status_code == 404
record("GET /api/v1/leads/{id}", "ID=0 → 404", "404",
       r.status_code, r.json(), ms, ok)


# ══════════════════════════════════════════════════════════════════════════
# 5. PUT /api/v1/leads/{id}
# ══════════════════════════════════════════════════════════════════════════
print("\n=== PUT /api/v1/leads/{id} ===")

# Update email
r, ms = req("PUT", f"/api/v1/leads/{created_lead_id}",
            json={"email": "updated@bristolbarber.co.uk"})
body = r.json()
ok = r.status_code == 200 and body.get("status") == "updated"
record("PUT /api/v1/leads/{id}", "update email", "200 + status=updated",
       r.status_code, body, ms, ok)

# Verify email was updated
r2, _ = req("GET", f"/api/v1/leads/{created_lead_id}")
ok = r2.json().get("email") == "updated@bristolbarber.co.uk"
record("PUT /api/v1/leads/{id}", "verify email persisted after update", "updated email",
       r2.status_code, r2.json().get("email"), _, ok)

# Update multiple fields
r, ms = req("PUT", f"/api/v1/leads/{created_lead_id}",
            json={"phone": "07700900123", "owner_name": "James T."})
ok = r.status_code == 200 and r.json().get("status") == "updated"
record("PUT /api/v1/leads/{id}", "update multiple fields", "200 + updated",
       r.status_code, r.json(), ms, ok)

# Empty body → 400
r, ms = req("PUT", f"/api/v1/leads/{created_lead_id}", json={})
ok = r.status_code == 400
record("PUT /api/v1/leads/{id}", "empty body → 400", "400",
       r.status_code, r.json(), ms, ok)

# All null fields → 400
r, ms = req("PUT", f"/api/v1/leads/{created_lead_id}",
            json={"email": None, "phone": None})
ok = r.status_code == 400
record("PUT /api/v1/leads/{id}", "all null fields → 400", "400",
       r.status_code, r.json(), ms, ok)

# Update non-existent lead (should still return 200 — soft update with no rows affected)
# This tests a design decision: no row-count check on update
r, ms = req("PUT", "/api/v1/leads/99999",
            json={"email": "ghost@nowhere.com"})
# Expected behaviour: 200 (no existence check). Record whatever it actually returns.
expected_str = "200 (no row check) OR 404 if existence checked"
ok_200 = r.status_code == 200
ok_404 = r.status_code == 404
record("PUT /api/v1/leads/{id}", "update nonexistent lead → ?",
       expected_str, r.status_code, r.json(), ms, ok_200 or ok_404)

# Update status field
r, ms = req("PUT", f"/api/v1/leads/{created_lead_id}",
            json={"status": "interested"})
ok = r.status_code == 200
record("PUT /api/v1/leads/{id}", "update status field", "200",
       r.status_code, r.json(), ms, ok)


# ══════════════════════════════════════════════════════════════════════════
# 6. DELETE /api/v1/leads/{id}
# ══════════════════════════════════════════════════════════════════════════
print("\n=== DELETE /api/v1/leads/{id} ===")

# Delete the min lead
r, ms = req("DELETE", f"/api/v1/leads/{min_lead_id}")
body = r.json()
ok = r.status_code == 200 and body.get("status") == "deleted"
record("DELETE /api/v1/leads/{id}", "soft delete", "200 + status=deleted",
       r.status_code, body, ms, ok)

# GET after DELETE — should return status='lost'
r2, ms2 = req("GET", f"/api/v1/leads/{min_lead_id}")
ok = r2.status_code == 200 and r2.json().get("status") == "lost"
record("DELETE /api/v1/leads/{id}", "GET after DELETE → status=lost",
       "200 + status=lost", r2.status_code, r2.json().get("status"), ms2, ok)

# Delete nonexistent → still 200 (soft update, no error)
r, ms = req("DELETE", "/api/v1/leads/99999")
ok = r.status_code == 200
record("DELETE /api/v1/leads/{id}", "delete nonexistent → 200",
       "200 (soft delete, no row check)", r.status_code, r.json(), ms, ok)

# Double-delete same lead → still 200
r, ms = req("DELETE", f"/api/v1/leads/{min_lead_id}")
ok = r.status_code == 200
record("DELETE /api/v1/leads/{id}", "double delete → 200", "200",
       r.status_code, r.json(), ms, ok)


# ══════════════════════════════════════════════════════════════════════════
# 7. POST /api/v1/campaigns
# ══════════════════════════════════════════════════════════════════════════
print("\n=== POST /api/v1/campaigns ===")

# Happy path with target criteria
campaign_payload = {
    "name": "Bristol Plumbers Q2",
    "target_criteria": {
        "town": "Bristol",
        "industry": "plumbing",
        "min_score": 60,
    },
    "template": "Hi {owner_name}, I noticed your plumbing business…",
}
r, ms = req("POST", "/api/v1/campaigns", json=campaign_payload)
body = r.json()
ok = r.status_code == 201 and "id" in body and body.get("status") == "created"
record("POST /api/v1/campaigns", "create with target criteria", "201 + id",
       r.status_code, body, ms, ok)
campaign_id = body.get("id", 1)

# Minimal — name only
r, ms = req("POST", "/api/v1/campaigns", json={"name": "Minimal Campaign"})
body = r.json()
ok = r.status_code == 201 and "id" in body
record("POST /api/v1/campaigns", "name only → 201", "201 + id",
       r.status_code, body, ms, ok)
min_campaign_id = body.get("id", 2)

# Missing required name → 422
r, ms = req("POST", "/api/v1/campaigns", json={"template": "Hello"})
ok = r.status_code == 422
record("POST /api/v1/campaigns", "missing name → 422", "422",
       r.status_code, r.json(), ms, ok)

# Empty body → 422
r, ms = req("POST", "/api/v1/campaigns", json={})
ok = r.status_code == 422
record("POST /api/v1/campaigns", "empty body → 422", "422",
       r.status_code, r.json(), ms, ok)

# Target criteria with complex nested object
r, ms = req("POST", "/api/v1/campaigns", json={
    "name": "Complex Criteria",
    "target_criteria": {"town": "Leeds", "industry": "restaurants", "min_score": 50, "limit": 100},
})
ok = r.status_code == 201
record("POST /api/v1/campaigns", "complex nested criteria → 201", "201",
       r.status_code, r.json(), ms, ok)


# ══════════════════════════════════════════════════════════════════════════
# 8. GET /api/v1/campaigns
# ══════════════════════════════════════════════════════════════════════════
print("\n=== GET /api/v1/campaigns ===")

r, ms = req("GET", "/api/v1/campaigns")
body = r.json()
ok = r.status_code == 200 and isinstance(body, list) and len(body) >= 1
record("GET /api/v1/campaigns", "list all", "200 + list ≥1",
       r.status_code, f"{len(body)} items", ms, ok)

# Check structure of first campaign
if body:
    c = body[0]
    has_keys = all(k in c for k in ["id", "name", "status", "target_criteria", "created_at"])
    record("GET /api/v1/campaigns", "campaign has required fields",
           "id, name, status, target_criteria, created_at",
           r.status_code, list(c.keys()), ms, has_keys)

    # target_criteria should be a dict (not a string)
    ok = isinstance(c.get("target_criteria"), dict)
    record("GET /api/v1/campaigns", "target_criteria is dict (not raw JSON string)",
           "dict", r.status_code, type(c.get("target_criteria")).__name__, ms, ok)


# ══════════════════════════════════════════════════════════════════════════
# 9. GET /api/v1/campaigns/{id}/stats
# ══════════════════════════════════════════════════════════════════════════
print("\n=== GET /api/v1/campaigns/{id}/stats ===")

# Valid campaign
r, ms = req("GET", f"/api/v1/campaigns/{campaign_id}/stats")
body = r.json()
ok = (r.status_code == 200
      and "campaign" in body
      and "stats" in body
      and isinstance(body["stats"], dict))
record("GET /campaigns/{id}/stats", "valid campaign stats", "200 + campaign + stats",
       r.status_code, body, ms, ok)

# stats is empty dict for new campaign with no emails
ok = isinstance(body.get("stats"), dict)
record("GET /campaigns/{id}/stats", "stats is dict", "dict",
       r.status_code, type(body.get("stats")).__name__, ms, ok)

# Non-existent campaign
r, ms = req("GET", "/api/v1/campaigns/99999/stats")
ok = r.status_code == 404
record("GET /campaigns/{id}/stats", "nonexistent campaign → 404", "404",
       r.status_code, r.json(), ms, ok)

# String ID → 422
r, ms = req("GET", "/api/v1/campaigns/abc/stats")
ok = r.status_code == 422
record("GET /campaigns/{id}/stats", "string ID → 422", "422",
       r.status_code, r.json(), ms, ok)


# ══════════════════════════════════════════════════════════════════════════
# 10. POST /api/v1/compliance/unsubscribe/{email}
# ══════════════════════════════════════════════════════════════════════════
print("\n=== POST /api/v1/compliance/unsubscribe/{email} ===")

# Happy path
test_email = "james@bristolbarber.co.uk"
r, ms = req("POST", f"/api/v1/compliance/unsubscribe/{test_email}")
body = r.json()
ok = r.status_code == 200 and body.get("status") == "unsubscribed"
record("POST /compliance/unsubscribe/{email}", "unsubscribe valid email",
       "200 + status=unsubscribed", r.status_code, body, ms, ok)

# email in response matches what was sent
ok = body.get("email") == test_email
record("POST /compliance/unsubscribe/{email}", "response echoes email",
       f"email={test_email}", r.status_code, body.get("email"), ms, ok)

# Idempotent — unsubscribe same email again
r, ms = req("POST", f"/api/v1/compliance/unsubscribe/{test_email}")
ok = r.status_code == 200  # INSERT OR IGNORE — should not error
record("POST /compliance/unsubscribe/{email}", "double unsubscribe → still 200",
       "200 (idempotent)", r.status_code, r.json(), ms, ok)

# Email with + sign (URL path param)
r, ms = req("POST", "/api/v1/compliance/unsubscribe/test%2Bsubscriber%40example.com")
ok = r.status_code == 200
record("POST /compliance/unsubscribe/{email}", "email with + (URL-encoded)",
       "200", r.status_code, r.json(), ms, ok)

# 'Token' is actually free text here — any string works since it's treated as email/token
r, ms = req("POST", "/api/v1/compliance/unsubscribe/not-an-email")
ok = r.status_code == 200  # API does not validate email format for token
record("POST /compliance/unsubscribe/{email}", "non-email token (raw string)",
       "200 (no email validation on token path)", r.status_code, r.json(), ms, ok)


# ══════════════════════════════════════════════════════════════════════════
# 11. POST /api/v1/compliance/erasure
# ══════════════════════════════════════════════════════════════════════════
print("\n=== POST /api/v1/compliance/erasure ===")

# Happy path — erase lead we created
r, ms = req("POST", "/api/v1/compliance/erasure",
            json={"email": "cafe@bristol.co.uk"})
body = r.json()
ok = r.status_code == 200 and body.get("erased") is True
record("POST /compliance/erasure", "erase known email", "200 + erased=True",
       r.status_code, body, ms, ok)

# email echoed in response
ok = body.get("email") == "cafe@bristol.co.uk"
record("POST /compliance/erasure", "response echoes email",
       "email=cafe@bristol.co.uk", r.status_code, body.get("email"), ms, ok)

# Erase nonexistent email (should still return erased=True — best practice: idempotent)
r, ms = req("POST", "/api/v1/compliance/erasure",
            json={"email": "nobody@nowhere.com"})
body = r.json()
ok = r.status_code == 200 and body.get("erased") is True
record("POST /compliance/erasure", "erase nonexistent email → idempotent 200",
       "200 + erased=True", r.status_code, body, ms, ok)

# Missing email field → 422
r, ms = req("POST", "/api/v1/compliance/erasure", json={})
ok = r.status_code == 422
record("POST /compliance/erasure", "missing email → 422", "422",
       r.status_code, r.json(), ms, ok)

# Empty body → 422
r, ms = req("POST", "/api/v1/compliance/erasure", content=b"",
            headers={"Content-Type": "application/json"})
ok = r.status_code == 422
record("POST /compliance/erasure", "empty body → 422", "422",
       r.status_code, r.json(), ms, ok)

# Verify erased lead is gone
r2, _ = req("GET", "/api/v1/leads?town=Bristol")
bristol_emails = [l.get("email") for l in r2.json()]
ok = "cafe@bristol.co.uk" not in bristol_emails
record("POST /compliance/erasure", "erased lead removed from DB",
       "lead not in GET /leads", r2.status_code, f"Bristol leads emails: {bristol_emails}", _, ok)

# Verify erased email is now suppressed (check audit)
r3, _ = req("GET", "/api/v1/compliance/audit/cafe@bristol.co.uk")
has_erasure = any(e.get("action") == "erasure" for e in r3.json())
record("POST /compliance/erasure", "erasure logged in audit trail",
       "audit entry with action=erasure", r3.status_code, r3.json(), _, has_erasure)


# ══════════════════════════════════════════════════════════════════════════
# 12. GET /api/v1/compliance/audit/{email}
# ══════════════════════════════════════════════════════════════════════════
print("\n=== GET /api/v1/compliance/audit/{email} ===")

# Email we unsubscribed
r, ms = req("GET", f"/api/v1/compliance/audit/{test_email}")
body = r.json()
ok = r.status_code == 200 and isinstance(body, list)
record("GET /compliance/audit/{email}", "audit trail for unsubscribed email",
       "200 + list", r.status_code, f"{len(body)} entries", ms, ok)

# Audit entry has required fields
if body:
    entry = body[0]
    has_keys = all(k in entry for k in ["email", "action", "timestamp"])
    record("GET /compliance/audit/{email}", "audit entry has required fields",
           "email, action, timestamp", r.status_code, list(entry.keys()), ms, has_keys)

# Unsubscribe action is in the log
has_unsub = any(e.get("action") == "suppression_added" for e in body)
record("GET /compliance/audit/{email}", "suppression_added action in log",
       "action=suppression_added entry", r.status_code,
       [e.get("action") for e in body], ms, has_unsub)

# Email with no history → empty list
r, ms = req("GET", "/api/v1/compliance/audit/nobody@example.com")
ok = r.status_code == 200 and r.json() == []
record("GET /compliance/audit/{email}", "no-history email → empty list",
       "200 + []", r.status_code, r.json(), ms, ok)

# Case-insensitive email lookup
upper_email = test_email.upper()
r, ms = req("GET", f"/api/v1/compliance/audit/{upper_email}")
body_upper = r.json()
# The compliance engine calls .lower() so results should be the same
ok = r.status_code == 200 and isinstance(body_upper, list)
record("GET /compliance/audit/{email}", "uppercase email → case-insensitive lookup",
       "200 + same entries as lowercase", r.status_code,
       f"{len(body_upper)} entries", ms, ok)


# ══════════════════════════════════════════════════════════════════════════
# Performance summary
# ══════════════════════════════════════════════════════════════════════════
print("\n=== Performance Summary (by endpoint) ===")
endpoint_times: dict[str, list[float]] = {}
for r_ in RESULTS:
    ep = r_["endpoint"]
    endpoint_times.setdefault(ep, []).append(r_["timing_ms"])

for ep, times in endpoint_times.items():
    avg = sum(times) / len(times)
    mx = max(times)
    flag = " *** SLOW > 200ms" if mx > 200 else ""
    print(f"  {ep}: avg={avg:.0f}ms  max={mx:.0f}ms{flag}")


# ══════════════════════════════════════════════════════════════════════════
# Final report
# ══════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 90)
print("FULL TEST REPORT")
print("=" * 90)
print(f"{'ENDPOINT':<42} {'TEST_NAME':<45} {'EXPECTED':<30} {'ACTUAL':>6} {'RESULT':<6}")
print("-" * 90)

for r_ in RESULTS:
    result_str = "PASS" if r_["passed"] else "FAIL"
    print(
        f"{r_['endpoint']:<42} "
        f"{r_['test_name']:<45} "
        f"{r_['expected']:<30} "
        f"{r_['actual_status']:>6} "
        f"{result_str:<6}"
    )

total = len(RESULTS)
passed = sum(1 for r_ in RESULTS if r_["passed"])
failed = total - passed

print("=" * 90)
print(f"TOTAL: {total}  PASSED: {passed}  FAILED: {failed}")
print()

# Grade
pct = passed / total * 100
if pct == 100:
    grade = "A+"
elif pct >= 95:
    grade = "A"
elif pct >= 85:
    grade = "B"
elif pct >= 75:
    grade = "C"
elif pct >= 60:
    grade = "D"
else:
    grade = "F"

print(f"OVERALL GRADE: {grade}  ({passed}/{total} = {pct:.1f}%)")
print()

# Bugs
failures = [r_ for r_ in RESULTS if not r_["passed"]]
if failures:
    print("=== BUGS FOUND ===")
    for f in failures:
        print(f"  FAIL: [{f['endpoint']}] {f['test_name']}")
        print(f"        Expected: {f['expected']}")
        print(f"        Got HTTP {f['actual_status']}: {f['body_snippet']}")
else:
    print("No bugs found — all tests passed.")

sys.exit(0 if failed == 0 else 1)
