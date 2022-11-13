from pydantic import BaseModel

class Body(BaseModel):
    matrix: list[list[float]] = []
    probabilities: list[float] = []
    depends_probabilities: list[list[float]] = []

class BodyGames(BaseModel):
    matrix: list[list[float]] = []

class BodyQueues(BaseModel):
    numberServices: int 
    averageArrivals: float = 0
    averageServices: float = 0


class BodyQueuesProbabilities(BaseModel):
    numberServices: int
    averageArrivals: float = 0
    averageServices: float = 0
    n: int

class BodyEconomicAnalysis(BaseModel):

    costAverageByService : float
    hoursServiceByDay : int
    numberServices: int
    averageArrivals: float = 0
    averageServices: float = 0
