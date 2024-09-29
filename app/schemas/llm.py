from pydantic import BaseModel

class LLMRequest(BaseModel):
    model_name: str
    prompt: str

    class Config:
        protected_namespaces = ()

class LLMResponse(BaseModel):
    model_name: str
    response: str

    class Config:
        protected_namespaces = ()
