from pydantic import BaseModel
class Body(BaseModel):
    matrix: list[list[float]] = []
    probabilities: list[float] = []
    depends_probabilities: list[list[float]] = []