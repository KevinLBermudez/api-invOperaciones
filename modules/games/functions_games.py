from os import error
import numpy as np
import sympy as sym
from sympy import  Symbol
from sympy import *
from sympy.solvers.diophantine.diophantine import length

def minRow(matrix):
    miniumByRow = np.amin(matrix, axis=1)

    return miniumByRow

def maxColumn(matrix):
    maxiumByColumn = np.amax(matrix, axis=0)

    return maxiumByColumn

def chairPoint(row,column):

    chairPoints = []
    indexes = []

    for i in row:
        for j in column:
            if i == j:
                chairPoints.append([i])
                indexes.append([row.tolist().index(i), column.tolist().index(j)])

    return [chairPoints, indexes]


def matrixProbability(matrix):

    flagRow = False
    flagColumn = False
    flagCicle = False
    contador = 0 
    x = 5

    matrixCopy = np.zeros(shape=(np.shape(matrix)[0], np.shape(matrix)[1],2))

    for i in range(0,np.shape(matrix)[0]):
        for j in range(0,np.shape(matrix)[1]):
            matrixCopy[i,j] = np.array([i,j])

    while flagCicle == False:

            dimensions = matrix.shape
            rows = np.arange(dimensions[0])
            columns = np.arange(dimensions[1])

            #delete rows
            if (flagRow == False):
                for i in rows:
                    if (flagRow == False):
                        for j in rows:
                            if (set(matrix[i, ]) != set(matrix[j, ])):
                                c = np.less_equal(matrix[i, ], matrix[j, ])
                                all_are_true = all(x == True for x in c)

                                if all_are_true:

                                    matrix = np.delete(matrix, (i), axis=0)
                                    matrixCopy = np.delete(matrixCopy, (i), axis=0)

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


            #delete columns
            if (flagColumn == False):
                for i in columns:
                    if (flagColumn == False):
                        for j in columns:
                            if (set(matrix[:, i]) != set(matrix[:, j])):
                                c = np.greater(matrix[:, i], matrix[:, j])
                                all_are_true = all(x == True for x in c)

                                if all_are_true:

                                    matrix = np.delete(matrix, (i), axis=1)
                                    matrixCopy = np.delete(matrixCopy, (i), axis=1)


                                    flagRow = False
                                    flagColumn = True
                                    break
                                else:
                                    flagColumn = False
                else:
                    contador += 1

            if (contador > x):
                flagCicle = True

            if (np.shape(matrix) != (2,2) and contador > x):
                return -1
            
    return [matrix, np.reshape(matrixCopy,(4,2))]


def equations(matrix):

    p = Symbol('p')

    eq1 = matrix[0, 0]*p + matrix[1, 0] * (1-p)
    eq2 = matrix[0, 1]*p + matrix[1, 1] * (1-p)
    eq3 = matrix[0,0]*p + matrix[0,1] * (1-p)
    eq4 = matrix[1,0]*p + matrix[1,1] * (1-p)

    p1 = sym.solve(sym.Eq(eq1,eq2), p)
    p2 = sym.solve(sym.Eq(eq3,eq4), p)

    eq1 = (eq1.subs(p, p1[0]))/100
    eq2 = (eq2.subs(p, p1[0]))/100
    eq3 = (eq3.subs(p, p2[0]))/100
    eq4 = (eq4.subs(p, p2[0]))/100

    
    return {"ecuacion1": str(eq1),
            "ecuacion2": str(eq2),
            "ecuacion3": str(eq3),
            "ecuacion4": str(eq4),
            "probabilidad1": str(p1[0]),
            "probabilidad2": str(p2[0])}



def foundIndex( i, list ):

    if( i in list ):

        return foundIndex(i + len(list), list)

    return i