from contextlib import asynccontextmanager
from database import Base, engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import tasks

from redis_client import redis_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    await redis_client.ping()
    print('redis and database is ready')
    yield
    await redis_client.aclose()
    print('redis connection closed')


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['http://localhost:3000'],
    allow_methods = ['*']
)

app.include_router(tasks.router, prefix='/api/v1')



