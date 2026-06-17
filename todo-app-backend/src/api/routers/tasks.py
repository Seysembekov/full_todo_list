import json

from fastapi import Depends, HTTPException, status, APIRouter
from redis.asyncio import Redis
from sqlalchemy.orm import Session

from config import settings
from schemes.tasks import TaskResponse, CreateTask, UpdateTask
from service.service_task import TaskService
from api.dependencies import get_redis_client, get_db_Session


router = APIRouter(prefix='/tasks', tags=['Tasks'])

@router.get('/')
async def get_all(
        db: Session = Depends(get_db_Session)
):
    service = TaskService(db)
    tasks = service.get_all()

    return [
        {
            "id": task.id,
            "title": task.title,
            "completed": task.completed
        }
        for task in tasks
    ]
@router.get("/")
async def get_all():
    print("REQUEST RECEIVED")
    return {"status": "ok"}

@router.get('/{task_id}')
async def get_by_id( task_id: int, db: Session = Depends(get_db_Session), redis: Redis = Depends(get_redis_client)):
    cache_key = f'tasks:{task_id}'
    cached = await redis.get(cache_key)
    if cached:
        return json.loads(cached)

    service = TaskService(db)
    task = service.get_by_id(task_id)

    await redis.set(cache_key, json.dumps(task.model_dump()), ex = settings.CACHE_EXPIRE)
    return task

@router.post('/')
async def create_task(data: CreateTask, db: Session = Depends(get_db_Session), redis: Redis = Depends(get_redis_client)):
    service = TaskService(db)
    task = service.create_task(data)

    await redis.delete('tasks:all')
    return task

@router.patch('/{task_id}')
async def update_task(task_id: int, data: UpdateTask, db: Session = Depends(get_db_Session), redis: Redis = Depends(get_redis_client)):
    service = TaskService(db)
    task = service.patch_task(task_id, data)

    await redis.delete(f'tasks:{task_id}')
    return task

@router.delete('/{task_id}')
async def delete_task(task_id: int, db: Session = Depends(get_db_Session), redis: Redis= Depends(get_redis_client)):
    service = TaskService(db)
    task = service.delete_task(task_id)

    await redis.delete('tasks:all')
    return task