from pydantic import BaseModel


class ArchitectureResponse(BaseModel):

    app_type: str

    users: int

    architecture: list

    estimated_rps: int

    bottlenecks: list