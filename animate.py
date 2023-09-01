import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection="3d")

x_data = np.arange(0, 5, 0.1)
y_data = np.arange(0, 5, 0.1)

X, Y = np.meshgrid(x_data, y_data)
Z = (np.square(X-3.14) + np.square(Y - 2.72) + np.sin(3*X + 1.41) + 
     np.sin(4*Y - 1.73) - np.cos(1.5*X - 1.21) - np.cos(1.2*Y + 1.7) + X) 
ax.plot_surface(X, Y, Z, cmap="viridis")
plt.show()