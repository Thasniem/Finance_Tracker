from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Finance Tracker API"
    database_url: str
    debug: bool = True

    class Config:
        env_file = ".env"


settings = Settings()