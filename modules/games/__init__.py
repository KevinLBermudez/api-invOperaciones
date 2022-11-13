from . import functios_games as games
import numpy as np
from sympy import *

def get_teory(data):

    matrixProbability = None
    equations = None
    miniumByRow = games.minRow(data)
    maxiumByColumn = games.maxColumn(data)
    chairPoint = games.chairPoint(miniumByRow,maxiumByColumn)
    print(len(chairPoint))
    if len (chairPoint) < 1 : 
        matrixProbability = games.matrixProbability(data)
        equations = games.equations(matrixProbability)

    return {
        "minimoPorFila" : miniumByRow.tolist(),
        "maximoPorColumna" : maxiumByColumn.tolist(),
        "puntoDeSilla" : chairPoint,
        "matrixProbabilidades": None if matrixProbability is None else matrixProbability.tolist(),
        "ecuaciones": None if equations is None else equations
    }


