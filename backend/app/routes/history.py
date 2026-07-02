from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.db import get_db

from app.models.architecture_model import (
    ArchitectureAnalysis
)

router = APIRouter()


@router.get("/history")
def get_history(
        db: Session = Depends(get_db)):

    results = db.query(
        ArchitectureAnalysis
    ).all()

    return results