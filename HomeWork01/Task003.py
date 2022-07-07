coordinates = input("Введите координаты точки через запятую (x,y): ")
coord_list = coordinates.split(",")

print(" 1 | 2 \n---+---\n 4 | 3 ")

if int(coord_list[0]) > 0 and int(coord_list[1]) > 0:
    print(f"Точка с координатами {coord_list[0]},{coord_list[1]} находится во второй четверти")
elif int(coord_list[0]) > 0 and int(coord_list[1]) < 0:
    print(f"Точка с координатами {coord_list[0]},{coord_list[1]} находится в третей четверти")
elif int(coord_list[0]) < 0 and int(coord_list[1]) < 0:
    print(f"Точка с координатами {coord_list[0]},{coord_list[1]} находится в четвертой четверти")
elif int(coord_list[0]) < 0 and int(coord_list[1]) > 0:
    print(f"Точка с координатами {coord_list[0]},{coord_list[1]} находится в первой четверти")
else:
    print(f"Одна из точек находится на оси")