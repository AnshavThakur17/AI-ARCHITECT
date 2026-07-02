from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from datetime import datetime

from app.database.db import Base


class ArchitectureAnalysis(Base):

    __tablename__ = "architecture_analysis"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    prompt = Column(
        String,
        nullable=False
    )

    app_type = Column(
        String,
        nullable=False
    )

    architecture = Column(
        String,
        nullable=False
    )

    database_choice = Column(
        String,
        nullable=False
    )

    estimated_cost = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )