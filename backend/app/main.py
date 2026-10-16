from contextlib import asynccontextmanager
from pathlib import Path
import psutil
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.database.store import init_db
from app.feature_control.service import list_features, update_feature
from app.job_manager.manager import start_demo, cancel, list_all, get_one

@asynccontextmanager
async def lifespan(app):
    init_db()
    yield

app = FastAPI(title="RoadSentinel Nexus API",version="0.1.0",
    description="Local-first foundation. Computer-vision engines are not implemented in v0.1.",lifespan=lifespan)
app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:5173","http://127.0.0.1:5173"],
    allow_credentials=False,allow_methods=["GET","POST","PUT"],allow_headers=["Content-Type"])

class FeatureUpdate(BaseModel):
    enabled: bool

@app.get("/api/health")
def health():
    return {"status":"ok","app":"RoadSentinel Nexus","version":"0.1.0","mode":"local"}

@app.get("/api/system")
def system_metrics():
    root = Path.home().anchor or "/"
    disk = psutil.disk_usage(root)
    mem = psutil.virtual_memory()
    return {"cpu_percent":psutil.cpu_percent(interval=.15),"memory_percent":mem.percent,
      "memory_used_gb":round(mem.used/1024**3,2),"memory_total_gb":round(mem.total/1024**3,2),
      "disk_percent":disk.percent,"disk_used_gb":round(disk.used/1024**3,2),"disk_total_gb":round(disk.total/1024**3,2)}

@app.get("/api/features")
def features():
    return {"features":list_features()}

@app.put("/api/features/{feature_id}")
def set_feature(feature_id: str, body: FeatureUpdate):
    try:
        return {"feature":update_feature(feature_id,body.enabled)}
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e)) from e

@app.get("/api/jobs")
def jobs():
    return {"jobs":list_all()}

@app.post("/api/jobs/demo")
def create_demo_job():
    return {"job":start_demo()}

@app.post("/api/jobs/{job_id}/cancel")
def cancel_job(job_id: str):
    job = cancel(job_id)
    if job is None:
        raise HTTPException(status_code=404,detail="Job not found.")
    return {"job":job}

@app.get("/api/jobs/{job_id}")
def job_detail(job_id: str):
    job = get_one(job_id)
    if job is None:
        raise HTTPException(status_code=404,detail="Job not found.")
    return {"job":job}
