import os

def aadition_coefficient(new_equation: list, equation: list):
    sign = 1
    for member in equation:
        match member:
            case "+":
                sign = 1
                continue
            case "-":
                sign = -1
                continue
            case _:
                pass
        if "*x^" in member:
            member = member.split("*x^")
            for member_nc in new_equation:
                if int(member[1]) == int(member_nc[1]): member_nc[0] += sign*int(member[0])
        elif "*x" in member:
            member = member.split("*x")
            new_equation[-2][0] += sign * int(member[0])
        elif member == 0: pass
        elif member.isdigit():
            new_equation[-1][0] += sign * int(member)
    return new_equation

def create_equation_matrix(new_equation: list, equation: list):
    for member in equation:
        if "*x^" in member:
            member = member.split("*x^")
            if [0, int(member[1])] not in new_equation:
                new_equation.append([0, int(member[1])])
    return new_equation

def create_new_equation(new_equation: list):
    polynomial = ""

    for member in new_equation:
        if member[1] == len(new_equation):
            if member[0] > 0:
                polynomial += (str(member[0]) + "*x^" + str(member[1]))
            else:
                polynomial += (str(member[0]) + "*x^" + str(member[1]))
        else:
            match member[1]:
                case 1:
                    if member[0] > 0:
                        polynomial += (" + " + str(member[0]) + "*x")
                    else:
                        polynomial += (" - " + str(-member[0]) + "*x")
                case 0:
                    if member[0] > 0:
                        polynomial += (" - " + str(member[0]) + " = 0")
                    else:
                        polynomial += (" - " + str(-member[0]) + " = 0")
                case _:
                    if member[0] > 0:
                        polynomial += (" + " + str(member[0]) + "*x^" + str(member[1]))
                    else:
                        polynomial += (" - " + str(-member[0]) + "*x^" + str(member[1]))
    path = os.path.join('folder', 'final_equation.txt')
    with open(path, 'w') as data:
        data.write(polynomial)



first_path = os.path.join('folder', 'first_equation.txt')
second_path = os.path.join('folder', 'second_equation.txt')

with open(first_path, 'r') as first_data:
    first_equation = first_data.readline().split(" ")

with open(second_path, 'r') as second_data:
    second_equation = second_data.readline().split(" ")

new_equation = []

new_equation = create_equation_matrix(new_equation, first_equation)
new_equation = create_equation_matrix(new_equation, second_equation)

new_equation.append([0, 1])
new_equation.append([0, 0])

new_equation = aadition_coefficient(new_equation, first_equation)
new_equation = aadition_coefficient(new_equation, second_equation)


create_new_equation(new_equation)

