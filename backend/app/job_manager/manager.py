import threading, time, uuid
from datetime import datetime, timezone
from app.database import store

_lock = threading.Lock()
_jobs = {}

def now():
    return datetime.now(timezone.utc).isoformat()

def worker(job_id):
    for step in range(1, 11):
        time.sleep(.5)
        with _lock:
            job = _jobs.get(job_id)
            if not job or job["status"] == "Cancelled":
                return
            job["message"] = f"Demo worker progress: {step*10}% (no video analysis performed)"
            job["updated_at"] = now()
            store.save_job(job)
    with _lock:
        job = _jobs[job_id]
        job["status"] = "Completed"
        job["message"] = "Demo job completed. No computer-vision analysis was performed."
        job["updated_at"] = now()
        store.save_job(job)

def start_demo():
    job = {"id":str(uuid.uuid4()),"kind":"demo_test_job","status":"Running",
           "message":"Demo worker started; this does not process video.","created_at":now(),"updated_at":now()}
    with _lock:
        _jobs[job["id"]] = job
        store.save_job(job)
        threading.Thread(target=worker,args=(job["id"],),daemon=True).start()
    return dict(job)

def cancel(job_id):
    with _lock:
        job = _jobs.get(job_id)
        if not job:
            job = next((j for j in store.list_jobs() if j["id"] == job_id), None)
        if not job:
            return None
        if job["status"] == "Running":
            job["status"] = "Cancelled"
            job["message"] = "Cancellation requested."
            job["updated_at"] = now()
            store.save_job(job)
        return dict(job)

def list_all():
    with _lock:
        live = [dict(j) for j in _jobs.values()]
    ids = {j["id"] for j in live}
    return live + [j for j in store.list_jobs() if j["id"] not in ids]

def get_one(job_id):
    return next((j for j in list_all() if j["id"] == job_id), None)
