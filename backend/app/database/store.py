import os, sqlite3
from pathlib import Path

DB_PATH = Path(os.environ.get("ROADSENTINEL_DB", Path(__file__).resolve().parents[3] / "data" / "roadsentinel.sqlite3"))

def connect():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB_PATH, timeout=10)
    con.row_factory = sqlite3.Row
    return con

def init_db():
    with connect() as con:
        con.execute("""CREATE TABLE IF NOT EXISTS features (
            id TEXT PRIMARY KEY, enabled INTEGER NOT NULL DEFAULT 0,
            updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)""")
        con.execute("""CREATE TABLE IF NOT EXISTS jobs (
            id TEXT PRIMARY KEY, kind TEXT NOT NULL, status TEXT NOT NULL,
            message TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL)""")

def get_feature_states():
    with connect() as con:
        return {r["id"]: bool(r["enabled"]) for r in con.execute("SELECT id, enabled FROM features")}

def set_feature_state(feature_id, enabled):
    with connect() as con:
        con.execute("""INSERT INTO features(id, enabled, updated_at) VALUES(?,?,CURRENT_TIMESTAMP)
        ON CONFLICT(id) DO UPDATE SET enabled=excluded.enabled, updated_at=CURRENT_TIMESTAMP""",
        (feature_id, int(enabled)))

def save_job(job):
    with connect() as con:
        con.execute("""INSERT INTO jobs(id,kind,status,message,created_at,updated_at) VALUES(?,?,?,?,?,?)
        ON CONFLICT(id) DO UPDATE SET status=excluded.status,message=excluded.message,updated_at=excluded.updated_at""",
        (job["id"],job["kind"],job["status"],job["message"],job["created_at"],job["updated_at"]))

def list_jobs():
    with connect() as con:
        return [dict(r) for r in con.execute("SELECT * FROM jobs ORDER BY created_at DESC LIMIT 50")]
