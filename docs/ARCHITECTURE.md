# Architecture

React dashboard -> FastAPI local API -> feature registry / job manager / SQLite / system metrics.

Feature `enabled` is persisted configuration; `implemented` distinguishes a real executor from a planned registry entry. Dependency validation prevents enabling dependent modules before prerequisites. The demo worker only tests job lifecycle and cancellation.

SQLite stores settings and job history. Future OpenCV/YOLO/OCR jobs should run in background workers, store evidence as files, expose progress/status, and require human review of potential traffic violations.
