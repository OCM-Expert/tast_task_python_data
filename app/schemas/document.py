from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class DocumentBase(BaseModel):
    doc_type: str
    obj: str
    author: str
    organization: str
    executor: str
    task: Optional[str]
    issue_date: datetime
    planned_due_date: datetime
    actual_due_date: Optional[datetime]
    overdue: float
    resolution: Optional[str]
    automatically_comleted: Optional[str]
    template_agreement: Optional[str]
    state: Optional[str]
    date: datetime
    completion_date: Optional[datetime]
    completed: bool


class Document(DocumentBase):
    id: int

    class Config:
        orm_mode = True
