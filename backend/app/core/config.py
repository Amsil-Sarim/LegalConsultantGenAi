from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
# Set up Pydantic settings for OpenAI API key and logging
# Add RATE_LIMIT_REQUESTS and RATE_LIMIT_WINDOW
