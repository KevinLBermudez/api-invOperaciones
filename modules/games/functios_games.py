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