from typing import Optional

from pydantic import BaseModel, ConfigDict


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    completed: bool

class CreateTask(BaseModel):
    title: str
    completed: bool = False

class UpdateTask(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None
