from app.utils.embedding_integration import query_openai_embedding, query_llama_embedding

async def query_embedding(model_name: str, text: str) -> str:
    if model_name == "openai":
        return await query_openai_embedding(text)
    elif model_name == "llama":
        return await query_llama_embedding(text)
    else:
        raise ValueError("Unsupported embedding model")
