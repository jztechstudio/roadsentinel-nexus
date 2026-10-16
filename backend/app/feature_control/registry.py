from dataclasses import dataclass

@dataclass(frozen=True)
class Feature:
    id: str
    name: str
    description: str
    category: str
    dependencies: tuple[str, ...] = ()
    implemented: bool = False

FEATURES = (
    Feature("system_monitor","Windows Monitoring","Real CPU, RAM and disk metrics.","System",implemented=True),
    Feature("video_analysis","Video Analysis","Recorded-video processing foundation.","Vision"),
    Feature("vehicle_detection","Vehicle / Object Detection","Detect objects in footage.","Traffic",("video_analysis",)),
    Feature("object_tracking","Object Tracking","Track detected objects across frames.","Traffic",("vehicle_detection",)),
    Feature("plate_recognition","License Plate Recognition","Plate-region detection and OCR.","Traffic",("vehicle_detection",)),
    Feature("overspeed_detection","Overspeed Detection","Calibrated speed estimation and candidate events.","Traffic",("vehicle_detection","object_tracking")),
    Feature("red_light_detection","Red-Light Candidate Detection","Configured signal and stop-line analysis.","Traffic",("vehicle_detection",)),
    Feature("lane_violation_detection","Lane Violation Candidate Detection","Configured lane-boundary analysis.","Traffic",("vehicle_detection","object_tracking")),
    Feature("parking_occupancy","Parking Occupancy","Configured parking-space analysis.","Parking",("vehicle_detection",)),
    Feature("illegal_parking","Restricted-Zone Parking","Restricted-zone dwell-time analysis.","Parking",("vehicle_detection","object_tracking")),
    Feature("network_monitor","Network Monitoring","Connectivity monitoring foundation.","Network"),
    Feature("lan_inventory","LAN Inventory","Inventory devices on a permitted local network.","Network",("network_monitor",)),
    Feature("wifi_scope","Wi-Fi Signal Analyzer","Local adapter and signal details where supported.","Network",("network_monitor",)),
    Feature("link_watch","Connectivity Uptime Monitor","Configured endpoint reachability checks.","Network",("network_monitor",)),
    Feature("api_workbench","API Workbench","API request workspace.","Developer"),
    Feature("repo_pilot","Repository Health Checker","Inspect a selected local repository.","Developer"),
    Feature("reports","Reports & Evidence","Reviewed events and reports.","Operations"),
)
BY_ID = {f.id:f for f in FEATURES}

def validate_enable(feature_id, enabled, states):
    feature = BY_ID.get(feature_id)
    if not feature:
        return "Unknown feature."
    if enabled:
        missing = [BY_ID[d].name for d in feature.dependencies if not states.get(d, False)]
        if missing:
            return "Enable dependencies first: " + ", ".join(missing)
    return None

def public_feature(f, enabled):
    return {"id":f.id,"name":f.name,"description":f.description,"category":f.category,
            "dependencies":list(f.dependencies),"implemented":f.implemented,"enabled":enabled,
            "status": ("Enabled (foundation only)" if f.implemented else "Configured — engine not implemented") if enabled else "Disabled"}
