from . import functions_games as games
import numpy as np
from sympy import *

def get_teory(data):

    matrixProbability = None
    equations = None
    miniumByRow = games.minRow(data)
    maxiumByColumn = games.maxColumn(data)
    chairPoint = games.chairPoint(miniumByRow, maxiumByColumn)

    if len(chairPoint) < 1:

        matrixProbability = games.matrixProbability(data)
        if(matrixProbability != -1):
            
            equations = games.equations(matrixProbability)
        else:
            equations = -1
    return {

        "minimoPorFila": miniumByRow.tolist(),
        "maximoPorColumna": maxiumByColumn.tolist(),
        "puntoDeSilla": chairPoint,
        # "matrixProbabilidades" : matrixProbability.tolist(),
        "matrixProbabilidades": None if matrixProbability is None else matrixProbability,
        #"ecuaciones": equations
        "ecuaciones": None if equations is None else equations

    }



