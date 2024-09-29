from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import llm, embeddings
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# Set up CORS
origins = ["*"]  # Adjust as needed for frontend restrictions

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(llm.router, prefix=f"{settings.API_V1_STR}/llm")
app.include_router(embeddings.router, prefix=f"{settings.API_V1_STR}/embeddings")

# Root route
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI LLM App"}
