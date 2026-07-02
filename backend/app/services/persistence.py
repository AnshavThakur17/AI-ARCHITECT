from sqlalchemy.orm import Session

from app.models.architecture_model import (
    ArchitectureAnalysis
)


def save_analysis(
        db: Session,
        prompt,
        app_type,
        architecture,
        database,
        cost,
        scale):

    new_record = ArchitectureAnalysis(

        prompt=prompt,

        app_type=app_type,

        architecture=str(architecture),

        database_choice=str(database),

        estimated_cost=str(cost),

        scale=scale
    )

    db.add(new_record)

    db.commit()

    db.refresh(new_record)

    return new_record