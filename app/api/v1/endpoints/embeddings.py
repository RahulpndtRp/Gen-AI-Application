from fastapi import APIRouter
from app.schemas.llm import LLMRequest, LLMResponse
from app.services.embedding_service import query_embedding

router = APIRouter()

@router.post("/query", response_model=LLMResponse)
async def query_embedding_endpoint(request: LLMRequest):
    response = await query_embedding(model_name=request.model_name, text=request.prompt)
    return {"model_name": request.model_name, "response": response}
