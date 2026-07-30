"""SENTRY application configuration."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://sentry:sentry@localhost:5432/sentry"
    redis_url: str = "redis://localhost:6379/0"
    debug: bool = True
    app_name: str = "SENTRY"
    app_version: str = "0.1.0"
    log_level: str = "INFO"

    model_config = {"env_prefix": "SENTRY_", "env_file": ".env"}


settings = Settings()
