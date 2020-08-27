import numpy as np
import matplotlib.pyplot as plt
import math
x = np.arange(-3*(math.pi), 3*(math.pi), 0.2)
y1 = np.sin(x)
y2 = np.sin(x+0.5)
y3 = np.sin(x+1)
y4 = np.sin(x+1.5)

plt.plot(x, y1, color="blue", linewidth=1, linestyle="dotted")
plt.plot(x, y2, color="green", linewidth=1, linestyle="dashed")
plt.plot(x, y3, color="orange", linewidth=1, linestyle="dashdot")
plt.plot(x, y4, color="pink")

plt.show()
