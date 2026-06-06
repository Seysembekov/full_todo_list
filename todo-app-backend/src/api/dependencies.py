from sqlalchemy.orm import Session
from database import get_db
from redis_client import get_redis
from fastapi import Depends
from redis.asyncio import Redis

def get_db_Session(db: Session = Depends(get_db)):
    return db

async def get_redis_client(redis: Redis = Depends(get_redis)):
    return redis