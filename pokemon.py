import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("data.csv")

type_count = data["Type1"].value_counts(ascending=True)

plt.barh(type_count.index, type_count.values, color="blue", edgecolor="black")

plt.title("No. of Pokemon by primary types")
plt.xlabel("Count")
plt.ylabel("Type")
plt.tight_layout()

plt.show()
