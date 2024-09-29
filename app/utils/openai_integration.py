import openai
from app.core.config import settings

async def query_openai(prompt: str) -> str:
    openai.api_key = settings.OPENAI_API_KEY
    response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=100)
    return response.choices[0].text.strip()

async def query_openai_embedding(text: str) -> str:
    openai.api_key = settings.OPENAI_API_KEY
    response = openai.Embedding.create(input=text)
    return response["data"][0]["embedding"]
