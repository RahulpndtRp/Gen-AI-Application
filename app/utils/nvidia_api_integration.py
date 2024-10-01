import requests
from app.core.config import settings

async def query_nvidia_llm(prompt: str) -> str:
    nvidia_api_url = settings.NVIDIA_API_URL
    response = requests.post(nvidia_api_url, json={"prompt": prompt})
    pass