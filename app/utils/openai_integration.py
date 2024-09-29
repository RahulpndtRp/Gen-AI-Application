from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

from app.core.config import settings

async def query_openai(prompt: str) -> str:
    response = client.completions.create(engine="davinci", prompt=prompt, max_tokens=100)
    return response.choices[0].text.strip()

async def query_openai_embedding(text: str) -> str:
    response = client.embeddings.create(input=text)
    return response.data[0].embedding
