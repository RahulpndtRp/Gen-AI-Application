from openai import OpenAI

client = OpenAI(api_key=settings.OPENAI_API_KEY)
import requests
from app.core.config import settings

# Function to query OpenAI for embedding
async def query_openai_embedding(text: str) -> str:
    response = client.embeddings.create(input=text)
    # Returning the embedding vector from OpenAI's response
    return response.data[0].embedding

# Function to query Llama for embedding
async def query_llama_embedding(text: str) -> str:
    llama_url = f"{settings.LLAMA_API_URL}/embedding"
    response = requests.post(llama_url, json={"text": text})
    # Returning the embedding vector from Llama's response
    return response.json().embedding
