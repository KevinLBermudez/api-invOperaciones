from modules import *
import matplotlib.pyplot as plt
import numpy as np

from modules import decisions

column_labels = ["S1", "S2"]

row_labels = []

for i in range(0, decisions.alternatives.shape[0]):
    row_labels.append(f"D{i+1}")

def assing_axis(ax):
    ax.axis("tight")
    ax.axis("off")

ax_one = plt.subplot(2, 2, 1)
assing_axis(ax_one)

ax_one.table(
    cellText=decisions.alternatives,
    colLabels=column_labels,
    rowLabels=row_labels,
    loc="center",
)

plt.title("Probabilidad de ganar al apostar al Real Madrid")

optimist_and_conservative = np.array([decisions.opt, decisions.cons]) 

ax_two = plt.subplot(2, 2, 2)
assing_axis(ax_two)


ax_two.table(
    cellText=optimist_and_conservative,
    rowLabels=["Optmista", "Conservador"],
    loc="center",
)

plt.title("Enfoques optimista y conservador")

ax_three = plt.subplot(2, 2, 3)
assing_axis(ax_three)

ax_three.table(
    cellText=decisions.max_regret,
    loc="center",
)

plt.title("Probabilidad de ganar al apostar al Real Madrid")


plt.show()

