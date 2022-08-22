import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-200, 200, 0.01)

def func(x):
    function = -12 * x**4 * np.sin(np.cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30
    return function

plt.grid()
plt.plot(x, func(x))
plt.show()