import matplotlib.pyplot as plt
import matplotlib.pyplot as ply
import numpy as np

x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 8])
y1 = np.array([55, 60, 65, 62, 68, 70, 78, 82, 85, 87, 88])

x2 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 8])
y2 = np.array([52, 63, 68, 69, 72, 75, 80, 82, 85, 89, 95])

plt.scatter(x1, y1, color="green", label="Class A")
plt.scatter(x2, y2, color="red", label="Class B")
plt.title("Student Data")
plt.xlabel("Hours studied")
plt.ylabel("Grades")
plt.grid(color="black", linestyle="dashed")

plt.legend()
plt.show()
