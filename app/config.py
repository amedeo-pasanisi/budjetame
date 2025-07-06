from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", 
        extra="ignore"
    )
    db_dialect: str
    db_user: str
    db_host: str
    db_port: str
    db_name: str
    db_password: str
    
    
config = Settings()
