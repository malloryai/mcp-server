import os

MALLORY_API_KEY = os.environ.get("MALLORY_API_KEY", "")
MALLORY_BASE_URL = os.environ.get(
    "MALLORY_BASE_URL", "https://api.mallory.ai/v1"
)
