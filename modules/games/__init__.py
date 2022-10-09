from . import functios_games as games
import numpy as np
from sympy import *

def get_teory(data):

    miniumByRow = games.minRow(data)
    maxiumByColumn = games.maxColumn(data)
    chairPoint = games.chairPoint(miniumByRow,maxiumByColumn)
    matrixProbability = games.matrixProbability(data)
    equations = games.equations(matrixProbability)

    return {

        "minimoPorFila" : miniumByRow.tolist(),
        "maximoPorColumna" : maxiumByColumn.tolist(),
        "puntoDeSilla" : chairPoint,
        "matrixProbabilidades" : matrixProbability.tolist(),
        "ecuaciones": equations
    }