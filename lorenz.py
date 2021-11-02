''' 
    Taken and modified from the page https://en.wikipedia.org/wiki/Lorenz_system on 11/1/21
'''

import numpy as np
from scipy.integrate import odeint
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from ipywidgets import interact

mpl.rcParams['figure.figsize'] = (10,10)

@interact(rho=(20, 30), beta=(0.1, 3), sigma=(0.1, 15))

def plot_trajectory(rho=28.0, beta=8.0 / 3, sigma=10.0): 

    def f(state, t):
        x, y, z = state  # Unpack the state vector
        return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # Derivatives

    state0 = [1.0, 1.0, 1.0]
    t = np.arange(0.0, 40.0, 0.001)

    states = odeint(f, state0, t)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(states[:, 0], states[:, 1], states[:, 2], c=cm.cool(np.abs(t / 50)), s=0.5)
    plt.draw()
    plt.show()