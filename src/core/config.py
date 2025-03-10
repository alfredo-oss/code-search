from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv("core/env/.env")

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI"
    APP_PORT: int = 8080

    DATABASE_NAME: str
    DATABASE_USER: str
    TABLE_NAME: str
    FIELDS: str

    class Config:
        env_file = "env/.env"

settings = Settings()