from sqlalchemy.orm import Session
from repositories.taskRepo import TaskRepo
from schemes.tasks import CreateTask, UpdateTask


class TaskService:
    def __init__(self, db: Session):
        self.repo = TaskRepo(db)

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id: int):
        return self.repo.get_by_id(id)

    def create_task(self, data: CreateTask):
        return self.repo.create_task(data)

    def patch_task(self, id: int, data: UpdateTask):
        return self.repo.patch_task(id, data)

    def delete_task(self, id: int):
        return self.repo.delete_task(id)