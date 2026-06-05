from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_NAME: str = "db"
    DATABASE_URL: str = "postgresql+psycopg://postgres:admin@127.0.0.1:5432/db"


    class Config:
        env_file = '.env'

settings = Settings()