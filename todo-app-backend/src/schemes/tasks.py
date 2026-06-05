from pydantic import BaseModel

class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool = False

class CreateTask(BaseModel):
    title: str
    completed: bool = False

class UpdateTask(BaseModel):
    title: str | None
    completed: bool = False
