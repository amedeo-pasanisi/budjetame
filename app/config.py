from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
    environment: Literal["dev", "prod", "test", "staging"] = "dev"
    db_dialect: str | None = None
    db_user: str | None = None
    db_host: str | None = None
    db_port: str | None = None
    db_name: str | None = None
    db_password: str | None = None
    db_url_prod: str | None = None
    
    @property
    def db_url(self) -> str:
        """
        Returns the correct database URL based on the current environment.
        Uses a manually constructed URL for non-prod environments.
        """
        if self.environment == "prod":
            if not self.db_url_prod:
                raise ValueError("`db_url_prod` is required in production environment.")
            return self.db_url_prod
        return f"{self.db_dialect}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

@lru_cache
def get_settings() -> Settings:
    return Settings()
