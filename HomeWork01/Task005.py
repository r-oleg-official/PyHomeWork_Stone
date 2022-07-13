import math
import func

coordinates = input("Введите координаты точек через запятую разделив пробелом (x1,y1 x2,y2): ")
dot_coord = coordinates.split(" ")
first_dot = dot_coord[0].split(",")
second_dot = dot_coord[1].split(",")
disatnce = math.sqrt((int(first_dot[0]) - int(second_dot[0]))**2 + (int(first_dot[1]) - int(second_dot[1]))**2)
print(f"Расстояние между точками {dot_coord[0]} и {dot_coord[1]} равно {disatnce}")