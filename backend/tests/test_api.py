from fastapi.testclient import TestClient
from app.main import app

def test_health():
    with TestClient(app) as client:
        r=client.get("/api/health")
        assert r.status_code == 200 and r.json()["status"] == "ok"

def test_metrics():
    with TestClient(app) as client:
        r=client.get("/api/system")
        assert r.status_code == 200 and "cpu_percent" in r.json()
