import func
import random
import os

deegre_of_num = func.enter_int_number("Введите степень многочлена: ")

polynomial = ""
while deegre_of_num >= 0:
    coefficient = random.randint(0, 100)
    if coefficient != 0:
        match deegre_of_num:
            case 1: polynomial += (str(coefficient) + "*x" + " + ")
            case 0: polynomial += (str(coefficient) + " = 0")
            case _: polynomial += (str(coefficient) + "*x^" + str(deegre_of_num) + " + ")
    deegre_of_num -= 1

path = os.path.join('folder', 'equation.txt')
with open(path, 'w') as data:
    data.write(polynomial)
