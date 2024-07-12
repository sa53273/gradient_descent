import numpy as np
import matplotlib.pyplot as plt

def z_f(x, y):
    return (np.sin(5*x) * np.cos(5*y)) / 5

def gradient(x, y):
    dx = np.cos(5*x) * np.cos(5*y)
    dy = -np.sin(5*x) * np.sin(5*y)
    return dx, dy

x = np.arange(-1, 1, 0.05)
y = np.arange(-1, 1, 0.05)

X, Y = np.meshgrid(x, y)
Z = z_f(X, Y)

pos = (0.7, 0.4, z_f(0.7, 0.4))
lr = 0.01

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', computed_zorder=False)

for _ in range(1000):
    dx, dy = gradient(pos[0], pos[1])
    new_x = pos[0] - dx * lr
    new_y = pos[1] - dy * lr
    new_z = z_f(new_x, new_y)
    pos = new_x, new_y, new_z

    ax.cla()  # Clear the axes
    ax.plot_surface(X, Y, Z, cmap='viridis', zorder=0)
    ax.scatter(pos[0], pos[1], pos[2], color='magenta', zorder=1)
    plt.pause(0.01)

plt.show()
