import numpy as np

def evidence(prob_success, prob_fail, alt_success, alt_fail):
    return (prob_success * alt_success) + (prob_fail * alt_fail) 

def evidences(alternatives, probabilities):
    evidences = np.array([])
    for alt in alternatives:
        evidences = np.append(evidences, evidence(probabilities[0], probabilities[1], alt[0], alt[1]))
    
    return evidences


def optimist(alternatives):
    optimist_array = np.array([])
    for alt in alternatives:
        optimist_array = np.concatenate((optimist_array, np.array([alt.max()])))
    
    return optimist_array

def conservative(alternatives):
    conservative_array = np.array([])
    for alt in alternatives:
        conservative_array = np.concatenate((conservative_array, np.array([alt.min()])))

    return conservative_array


def max_regret(opt, cons):
    def rest_values(arr, element):
        return (arr.max() - element)

    new_opt = interact_and_concat(opt,  rest_values)
    new_cons = interact_and_concat(cons,  rest_values)

    constraints = np.array([])

    for i in range(0, new_opt.size):
        print("Text:", new_opt[i], new_cons[i])
        constraints = np.concatenate((constraints, np.array([new_opt[i], new_cons[i]])))

    return constraints.reshape(3, 2)

def probability_of_occurrence(prob_si, prob_occur_si,  prob_success_or_fail, ):
    return prob_si * prob_occur_si / prob_success_or_fail

def probabilities_of_ocurrence(depends_prob, state_prob, success_or_fail_prob):
    probs = np.array([])
    
    for i, prob in enumerate(depends_prob):
        for j, r_prob in enumerate(prob): 
            probs = np.append(probs, probability_of_occurrence(r_prob, state_prob[i], success_or_fail_prob[j]))

    return probs



def interact_and_concat(arr, transform):
    new_arr = np.array([])
    for element in arr:
        new_arr = np.concatenate((new_arr, np.array([transform(arr=arr, element=element)])))
    
    return new_arr


def get_point(s1, s2):
    return [
        [0, (s1 * 0 + s2 * (1 - 0))], 
        [1, (s1 * 1 + s2 * (1 - 1))]
    ]