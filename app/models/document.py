from sqlalchemy import Column
from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import String, Float, DateTime

from app.db.base_class import Base


class Document(Base):
    __tablename__ = "document"

    id = Column(Integer, primary_key=True, index=True)
    doc_type = Column("Вид документа", String)
    obj = Column("Объект", String)
    author = Column("Автор", String)
    organization = Column("Организация", String)
    executor = Column("Исполнитель", String)
    task = Column("Задача", String)
    issue_date = Column("Дата выдачи", DateTime)
    planned_due_date = Column("Дата выполнения (план)", DateTime)
    actual_due_date = Column("Дата выполнения (факт)", DateTime)
    overdue = Column("Просрочена, ч", Float, nullable=False)
    resolution = Column("Резолюция", String)
    automatically_comleted = Column("Выполнена автоматически", String)
    template_agreement = Column("Договор по шаблону", String)
    state = Column("Состояние", String)
    date = Column("Дата", DateTime)
    completion_date = Column("Дата завершения", DateTime)
    completed = Column("Завершен", Boolean, default=False)

    def __repr__(self) -> str:
        return f"Document(id={self.id}, task={self.task})"
