import os
import requests
from typing import Optional, Tuple

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

DISTANCE_MATRIX_URL = "https://maps.googleapis.com/maps/api/distancematrix/json"

def get_eta_and_distance_minutes(
    origin_lat: float,
    origin_lng: float,
    dest_lat: float,
    dest_lng: float,
    timeout: float = 5.0,
) -> Optional[Tuple[float, float]]:
    """
    Returns (duration_minutes, distance_km) if successful, else None.
    """
    if not GOOGLE_MAPS_API_KEY:
        return None

    params = {
        "origins": f"{origin_lat},{origin_lng}",
        "destinations": f"{dest_lat},{dest_lng}",
        "mode": "driving",
        "units": "metric",
        "key": GOOGLE_MAPS_API_KEY,
    }

    try:
        resp = requests.get(DISTANCE_MATRIX_URL, params=params, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()

        if data.get("status") != "OK":
            return None

        rows = data.get("rows", [])
        if not rows or not rows[0].get("elements"):
            return None

        el = rows[0]["elements"][0]
        if el.get("status") != "OK":
            return None

        duration_sec = el["duration"]["value"]           # seconds
        distance_m  = el["distance"]["value"]            # meters

        duration_min = duration_sec / 60.0
        distance_km  = distance_m / 1000.0
        return duration_min, distance_km

    except requests.RequestException:
        return None
