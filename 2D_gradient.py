import numpy as np
import matplotlib.pylab as plt


# 2D Gradient Descent
def y_f(x):
    return np.sin(x)

def dy_f(x):
    return np.cos(x)

x = np.arange(-5, 5, 0.1)
y = y_f(x)

learning_rate = 0.03
cur_pos = (1.5, y_f(1.5))

for n in range(1000):
    new_x = cur_pos[0] - learning_rate*dy_f(cur_pos[0])
    new_y = y_f(new_x)
    cur_pos = (new_x, new_y)
    
    plt.title('2D Gradient Descent')
    plt.plot(x, y)
    plt.scatter(cur_pos[0], cur_pos[1], color='red')
    plt.pause(0.001)
    plt.clf()