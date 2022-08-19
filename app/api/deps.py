from typing import Any
from typing import Generator

from app.db.database import SessionLocal


def get_db() -> Generator[Any, None, None]:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()