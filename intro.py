import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([30, 25, 20, 18])
y2 = np.array([15, 25, 28, 35])
y3 = np.array([15, 20, 23, 50])

plt.title("Class size", fontsize=20,
          fontstyle="italic",
          family="Calibri",
          fontweight="bold")

label_style = dict(fontsize=15,
                   family="Calibri",
                   fontweight="bold")

plt.xlabel("Year", **label_style)
plt.ylabel("Size", **label_style)

line_style = dict(marker="o",
                  markersize=7,
                  markerfacecolor="black",
                  markeredgecolor="black",
                  linestyle="solid",
                  linewidth="2.5", )

plt.plot(x, y1, **line_style, color="orange")

plt.plot(x, y2, **line_style, color="blue")

plt.plot(x, y3, **line_style, color="green")

plt.show()
