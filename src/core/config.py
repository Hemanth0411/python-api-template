from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Application settings powered by Pydantic.
    It automatically reads from environment variables or a .env file.
    """
    APP_TITLE: str
    APP_VERSION: str = "0.2.0"
    DEBUG: bool
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()