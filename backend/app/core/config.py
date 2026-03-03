import os

class Settings:
    PROJECT_NAME: str = "Internal CAASM Portal"
    DATABASE_URL: str = "sqlite:///../../data/db.sqlite"
    # To use a local HF model offline, we can configure this path. For now, pull from Hub.
    VISION_MODEL_ID: str = "google/vit-base-patch16-224"
    SATELLITE_API_KEY: str = os.getenv("SATELLITE_API_KEY", "")
    LLM_API_KEY: str = os.getenv("LLM_API_KEY", "")

settings = Settings()
