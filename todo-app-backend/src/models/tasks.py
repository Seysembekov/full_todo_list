from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class Tasks(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    completed: Mapped[bool] = mapped_column(default=False)