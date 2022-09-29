import numpy as np

# d1 = np.array([65, 0])
# d2 = np.array([54, 23])
# d3 = np.array([14, 48])

# alternatives = np.array([d1,  d2, d3])
# probabilities = np.array([0.70, 0.30])

# dependsProbabilities = np.array([[0.68, 0.32], [0.24, 0.76]])

def setData(alternatives, probabilities, dependsProbabilities):
    print(alternatives, probabilities, dependsProbabilities)
    return surround_in_array([alternatives,probabilities, dependsProbabilities])

def surround_in_array(arr):
    return np.array(arr)