import os
from pydantic import BaseModel


class Settings(BaseModel):
    """
    Application configuration loaded from environment variables.
    """

    APP_NAME: str = "AI Agent MVP"

    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

    MODEL_NAME: str = os.getenv("MODEL_NAME", "gpt-4.1-mini")

    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql+asyncpg://agent:password@postgres:5432/agent_db"
    )

    REQUEST_TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", "30"))

    MAX_RETRIES: int = int(os.getenv("MAX_RETRIES", "3"))


settings = Settings()