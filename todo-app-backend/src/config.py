from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_NAME: str = "db"
    DATABASE_URL: str = "postgresql+psycopg://postgres:admin@127.0.0.1:5432/db"

    REDIS_HOST: str = 'localhost'
    REDIS_PORT: str = 6379
    REDIS_DB: int = 0
    CACHE_EXPIRE: int = 300

    class Config:
        env_file = '.env'

settings = Settings()