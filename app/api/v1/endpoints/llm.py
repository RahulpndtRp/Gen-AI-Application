from fastapi import APIRouter, Depends
from app.schemas.llm import LLMRequest, LLMResponse
from app.services.llm_service import query_llm

router = APIRouter()

@router.post("/query", response_model=LLMResponse)
async def query_llm_endpoint(request: LLMRequest):
    response = await query_llm(model_name=request.model_name, prompt=request.prompt)
    return {"model_name": request.model_name, "response": response}
