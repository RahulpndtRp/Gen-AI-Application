from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI LLM App"
    API_V1_STR: str = "/api/v1"
    OPENAI_API_KEY: str
    LLAMA_API_URL: str
    NVIDIA_API_URL : str
    DATABASE_URL: str = "sqlite:///./test.db"
    MULTI_USER_ACCESS: bool = True

    class Config:
        env_file = ".env"
        extra = "allow"  # Allow extra fields

settings = Settings()
