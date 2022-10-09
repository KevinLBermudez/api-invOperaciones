import numpy as np

def minRow(matrix):
    miniumByRow = np.amin(matrix, axis=1)

    return miniumByRow

def maxColumn(matrix):
    maxiumByColumn = np.amax(matrix, axis=0)

    return maxiumByColumn

def chairPoint(row,column):

    chairPoints = []

    for i in row:
        for j in column:
            if i == j:
                chairPoints.append([i,row.tolist().index(i),column.tolist().index(j)])
    
    return chairPoints


def matrixProbability(matrix):

    flagRow = False
    flagColumn = False
    flagCicle = False
    contador = 0 
    x = 4

    while flagCicle == False:

        print(flagCicle);

        dimensions = matrix.shape
        rows = np.arange(dimensions[0])
        columns = np.arange(dimensions[1])

        if (flagRow == False):
            for i in rows:
                if (flagRow == False):
                    for j in rows:
                        if (set(matrix[i, ]) != set(matrix[j, ])):
                            c = np.less_equal(matrix[i, ], matrix[j, ])
                            all_are_true = all(x == True for x in c)
                            if all_are_true:
                                matrix = np.delete(matrix, (i), axis=0)
                                print("se elimino la fila: ", i)
                                print(matrix)
                                flagColumn = False
                                flagRow = True
                                break
                            else:
                                flagRow = False
            else:
                contador += 1
                
        dimensions = matrix.shape
        rows = np.arange(dimensions[0])
        columns = np.arange(dimensions[1])

        if (flagColumn == False):
            for i in columns:
                if (flagColumn == False):
                    for j in columns:
                        if (set(matrix[:, i]) != set(matrix[:, j])):
                            c = np.greater(matrix[:, i], matrix[:, j])
                            all_are_true = all(x == True for x in c)
                            if all_are_true:
                                matrix = np.delete(matrix, (i), axis=1)
                                print("se elimino la columna: ", i)
                                print(matrix)
                                flagRow = False
                                flagColumn = True
                                break
                            else:
                                flagColumn = False
            else:
                contador += 1

        print(contador)

        if (contador > x):
            flagCicle = True

    return matrix



