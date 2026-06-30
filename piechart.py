import matplotlib.pyplot as plt
import numpy as np

categories = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
values = np.array([300, 250, 200, 234])
colors = ["#d4e09b", "#f6f4d2", "#cbdfbd", "#f19c79"]

plt.title("College")
plt.pie(values, labels=categories, autopct="%1.1f%%", colors=colors, explode=[0.1, 0, 0, 0], shadow=True,
        startangle=180)
plt.show()
