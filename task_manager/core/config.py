from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Task Manager API"
    VERSION: str = "2025.10"
    API_V1_STR: str = "/api/v1"

    POSTGRES_USER: str = "taskuser"
    POSTGRES_PASSWORD: str = "taskpass"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str = "taskmanager"

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg:// \
            {self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@\
                {self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    SECRET_KEY: str = "key_in_prod"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)


settings = Settings()
