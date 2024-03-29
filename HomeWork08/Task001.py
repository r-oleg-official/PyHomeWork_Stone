import math
import numpy as np
import matplotlib.pyplot as plt


a, b, c = 5, 10, -30
x = np.arange(-10, 10.01, 0.01)

def func(x):
    function = a*x**2 + b*x + c
    return function

def sqr_roots(a, b, c):
    dscrt = b ** 2 - 4 * a * c
    if dscrt > 0:
        x1 = (-b + math.sqrt(dscrt)) / (2 * a)
        x2 = (-b - math.sqrt(dscrt)) / (2 * a)
        return (x1, x2)
    elif dscrt == 0:
        x = -b / (2 * a)
        return x
    else:
        return None

min_func = min(func(x))
x = sqr_roots(a, b, c-min_func)


def change_func(x):
    x_range_down = np.arange(-10, x, 0.01)
    x_range_up = np.arange(x, 10, 0.01)
    plt.title(f'Корни функции: {round(sqr_roots(a, b, c)[0], 2)}, {round(sqr_roots(a, b, c)[1], 2)}')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.grid()
    plt.plot(x_range_down, func(x_range_down), 'r', label="Убывание")
    plt.plot(x_range_up, func(x_range_up), 'b', label="Возрастание")
    plt.plot(x, func(x), 'ro')
    plt.text(x, func(x) + 30, f'Вершина функции x = {x}')
    plt.legend()
    plt.show()

change_func(x)