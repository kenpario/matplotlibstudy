import matplotlib.pyplot as plt
import numpy as np

categories = ["Grains", "Fruit", "Vegetables", "Protein", "Dairy", "Sweets"]
values = np.array([4, 3, 1, 5, 3, 2])

plt.bar(categories, values, color="red")

plt.grid(axis="y",
         linestyle="dashed",
         color="black")

plt.title("Daily Consumption")

plt.xlabel("Food")
plt.ylabel("Quantity")

plt.show()
