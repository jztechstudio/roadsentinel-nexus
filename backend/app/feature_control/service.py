from app.database import store
from app.feature_control.registry import FEATURES, BY_ID, validate_enable, public_feature

def list_features():
    states = store.get_feature_states()
    return [public_feature(f, states.get(f.id, f.id == "system_monitor")) for f in FEATURES]

def update_feature(feature_id, enabled):
    states = store.get_feature_states()
    for f in FEATURES:
        states.setdefault(f.id, f.id == "system_monitor")
    error = validate_enable(feature_id, enabled, states)
    if error:
        raise ValueError(error)
    store.set_feature_state(feature_id, enabled)
    return public_feature(BY_ID[feature_id], enabled)
