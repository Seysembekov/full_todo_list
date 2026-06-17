from sqlalchemy.orm import Session
from repositories.taskRepo import TaskRepo
from schemes.tasks import CreateTask, UpdateTask, TaskResponse


class TaskService:
    def __init__(self, db: Session):
        self.repo = TaskRepo(db)

    def get_all(self):
        tasks = self.repo.get_all()
        return [TaskResponse.model_validate(task) for task in tasks]

    def get_by_id(self, id: int):
        return TaskResponse.model_validate(self.repo.get_by_id(id))

    def create_task(self, data: CreateTask):
        return TaskResponse.model_validate(self.repo.create_task(data))

    def patch_task(self, id: int, data: UpdateTask):
        return TaskResponse.model_validate(self.repo.patch_task(id, data))

    def delete_task(self, id: int):
        return TaskResponse.model_validate(self.repo.delete_task(id))