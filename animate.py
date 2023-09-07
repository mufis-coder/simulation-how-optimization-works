import numpy as np
import matplotlib.pyplot as plt

from func import objective_function

ax = plt.axes(projection="3d")

x = np.random.randint(0, 5, 50)
y = np.random.randint(0, 5, 50)
z = objective_function(x, y) + 0.5
ax.scatter(x, y, z, c='red', s=15)

x_data = np.arange(0, 5, 0.1)
y_data = np.arange(0, 5, 0.1)

X, Y = np.meshgrid(x_data, y_data)
Z = objective_function(X, Y)
ax.plot_surface(X, Y, Z, cmap="viridis", alpha=1)

ax.view_init(azim=-135, elev=35)

plt.show()