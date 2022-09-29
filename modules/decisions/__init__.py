from . import functions as decisions
import numpy as np


def get_teory(alternatives, probabilities, dependsProbabilities):

    opt = decisions.optimist(alternatives)
    cons = decisions.conservative(alternatives)
    max_regret = decisions.max_regret(opt, cons)
    evidences = decisions.evidences(alternatives, probabilities)

    awaited_value = decisions.evidences(np.array([[opt.max(), cons.max()]]), probabilities)[0]

    vea = awaited_value - evidences.max()

    evidences_with_max_regret = decisions.evidences(max_regret, probabilities)
    print(evidences_with_max_regret)

    probability_success = decisions.evidence(probabilities[0], probabilities[1], dependsProbabilities[0, 0], dependsProbabilities[1, 0])

    probability_fail = decisions.evidence(probabilities[0], probabilities[1], dependsProbabilities[0, 1], dependsProbabilities[1, 1])

    roots = np.array([probability_success, probability_fail])

    results_with_probabilities = decisions.probabilities_of_ocurrence(dependsProbabilities, probabilities, roots)

    # TREE ------------------------------------------------------------------------------------------

    tails = np.array([
            [results_with_probabilities[0], results_with_probabilities[2]], 
            [results_with_probabilities[1], results_with_probabilities[3]]
        ])

    evidence_with_success_percent = decisions.evidences(alternatives, tails[0])
    evidence_with_fail_percent = decisions.evidences(alternatives, tails[1])

    veod = decisions.evidence(roots[0], roots[1], evidence_with_success_percent.max(), evidence_with_fail_percent.max())

    efficiency = abs(veod - awaited_value) / vea 

    ive = veod-evidences.max()

    # GRAPHICS --------------------------------------------------------------------------------------

    chart_points = []

    for alt in alternatives:
        chart_points.append(decisions.get_point(alt[0], alt[1]))
        
    print(chart_points)

    return {
        "optimista": opt.tolist(),
        "conservador": cons.tolist(),
        "maximo_arrepentimiento" : max_regret.tolist(),
        "evidencias": evidences.tolist(),
        "evidencias_maximo_arrepentimiento": evidences_with_max_regret.tolist(),
        "ve": evidences.max(),
        "vea": vea,
        "vea_maximo_arrepentimiento": evidences_with_max_regret.min(),
        "probabilidad_favorable": probability_success,
        "probabilidad_desfavorable": probability_fail,
        "probabilidad_ocurrencia": results_with_probabilities.tolist(),
        "evidencia_favorable": evidence_with_success_percent.tolist(),
        "evidencia_desfavorable": evidence_with_fail_percent.tolist(),
        "veod": veod,
        "eficiencia": efficiency,
        "incrento_valor_esperado":ive,
        "puntos": chart_points
    }