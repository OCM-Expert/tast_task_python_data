from typing import Any
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.api import deps
from app.crud.crud_document import get_documents
from app.schemas.document import Document

router = APIRouter()

@router.get("/", response_model=List[Document])
def read_documents(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve documents.
    """
    documents = get_documents(db, skip=skip, limit=limit)
    return documents