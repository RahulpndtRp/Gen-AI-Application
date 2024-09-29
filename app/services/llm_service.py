from app.utils.openai_integration import query_openai
from app.utils.llama_integration import query_llama

async def query_llm(model_name: str, prompt: str) -> str:
    if model_name == "openai":
        return await query_openai(prompt)
    elif model_name == "llama":
        return await query_llama(prompt)
    else:
        raise ValueError("Unsupported model")
