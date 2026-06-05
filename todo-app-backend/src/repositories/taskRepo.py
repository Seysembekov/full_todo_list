import self
from sqlalchemy.orm import Session

from models.tasks import Tasks
from schemes.tasks import TaskResponse, UpdateTask, CreateTask
from database import Base, get_db, sessionmaker

class TaskRepo:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Tasks).all()

    def get_by_id(self, id: int):
        return self.db.query(Tasks).filter(Tasks.id == id).first()

    def create_task(self, data: CreateTask):
        task = Tasks(**data.model_dump())
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def patch_task(self,id:int, data: UpdateTask):
        task_p = self.db.query(Tasks).filter(Tasks.id == id).first()
        if data.title is not None:
            task_p.title = data.title

        if data.completed is not False:
            task_p.completed = data.completed

        self.db.commit()
        self.db.refresh(task_p)
        return task_p

    def delete_task(self, id: int):
        task_d = self.db.query(Tasks).filter(Tasks.id == id).first()
        if task_d:
            self.db.delete(task_d)
            self.db.commit()
