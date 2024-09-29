import requests
from app.core.config import settings

async def query_llama(prompt: str) -> str:
    llama_url = settings.LLAMA_API_URL
    response = requests.post(llama_url, json={"prompt": prompt})
    return response.json().get("response")

async def query_llama_embedding(text: str) -> str:
    llama_url = f"{settings.LLAMA_API_URL}/embedding"
    response = requests.post(llama_url, json={"text": text})
    return response.json().get("embedding")
