from . import functios_games as games
import numpy as np

def get_teory(data):

    miniumByRow = games.minRow(data)
    maxiumByColumn = games.maxColumn(data)
    chairPoint = games.chairPoint(miniumByRow,maxiumByColumn)
    matrixProbability = games.matrixProbability(data)

    return {

        "minimo por fila" : miniumByRow.tolist(),
        "maximo por columna" : maxiumByColumn.tolist(),
        "punto de silla" : chairPoint,
        "matrix de probabilidades" : matrixProbability.tolist()
    }