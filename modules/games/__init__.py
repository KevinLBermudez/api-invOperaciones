from . import functions_games as games
import numpy as np
from sympy import *

def get_teory(data):

    matrixProbability = None
    equations = None
    indixes = None
    miniumByRow = games.minRow(data)
    maxiumByColumn = games.maxColumn(data)
    chairPoint = games.chairPoint(miniumByRow, maxiumByColumn)

    if len(chairPoint) < 1:

        resultsMatrixProbability = games.matrixProbability(data)

        matrixProbability = resultsMatrixProbability[0]


        if(type(matrixProbability) != int):
            equations = games.equations(matrixProbability)
            indixes = resultsMatrixProbability[1]
        else:
            matrixProbability = None
            indixes = None
        
    return {

        "minimoPorFila": miniumByRow.tolist(),
        "maximoPorColumna": maxiumByColumn.tolist(),
        "puntoDeSilla": chairPoint,
        "matrixProbabilidades": None if matrixProbability is None else matrixProbability.tolist(),
        "indices": None if indixes is None else indixes,
        "ecuaciones": None if equations is None else equations

    }



