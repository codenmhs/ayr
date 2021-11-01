''' 
    Taken and modified from the page https://en.wikipedia.org/wiki/Lorenz_system on 11/1/21
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0

def f(state, t):
    x, y, z = state  # Unpack the state vector
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # Derivatives

state0 = [1.0, 1.0, 1.0]
t = np.arange(0.0, 40.0, 0.001)

states = odeint(f, state0, t)

fig = plt.figure()
ax = fig.gca(projection="3d")
# ax.plot(states[:, 0], states[:, 1], states[:, 2])
ax.scatter(states[:, 0], states[:, 1], states[:, 2], c=cm.cool(np.abs(t / 50)), s=0.5)
plt.draw()
plt.show()