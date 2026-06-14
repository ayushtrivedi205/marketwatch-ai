import os
import json
from datetime import datetime


def save_alerts(alerts, path="data/alerts/alerts.json"):
    """
    Save a list of alert dicts to a JSON file (append mode).
    Each alert gets a timestamp added automatically.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Load existing alerts if file exists
    existing = []
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                existing = json.load(f)
        except (json.JSONDecodeError, IOError):
            existing = []

    # Stamp and append
    for alert in alerts:
        alert["timestamp"] = datetime.now().isoformat()
        existing.append(alert)

    with open(path, "w") as f:
        json.dump(existing, f, indent=2)

    print(f"Saved {len(alerts)} alert(s) to {path}")
