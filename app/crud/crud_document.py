from sqlalchemy.orm import Session

from app.models import Document

def get_documents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Document).offset(skip).limit(limit).all()