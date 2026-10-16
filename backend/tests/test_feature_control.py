from app.feature_control.registry import validate_enable, BY_ID
from app.database import store

def test_dependency_validation():
    assert "Enable dependencies first" in validate_enable("overspeed_detection",True,{"vehicle_detection":False,"object_tracking":False})

def test_feature_exists():
    assert "plate_recognition" in BY_ID

def test_sqlite_persistence(tmp_path, monkeypatch):
    path = tmp_path / "test.sqlite3"
    monkeypatch.setattr(store,"DB_PATH",path)
    store.init_db()
    store.set_feature_state("plate_recognition",True)
    assert store.get_feature_states()["plate_recognition"] is True
