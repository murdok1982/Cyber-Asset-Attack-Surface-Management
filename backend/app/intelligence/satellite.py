import os
import requests
from app.core.config import settings

def download_satellite_image(lat: str, lon: str, save_path: str) -> bool:
    """
    Downloads a static map image for the given coordinates to provide physical security context.
    """
    if not settings.SATELLITE_API_KEY:
        print("SATELLITE_API_KEY not configured. Skipping download.")
        # Create a dummy image file for MVP testing
        with open(save_path, "wb") as f:
            f.write(b"dummy image data")
        return True

    # Example: Google Maps Static API
    url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom=18&size=600x400&maptype=satellite&key={settings.SATELLITE_API_KEY}"
    
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(response.content)
            return True
        return False
    except Exception as e:
        print(f"Error downloading satellite map: {e}")
        return False
