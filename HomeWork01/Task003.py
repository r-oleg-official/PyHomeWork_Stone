coordinates = input("Введите координаты точки через запятую (x,y): ")
coord_list = coordinates.split(",")

print(" 2 | 1 \n---+---\n 3 | 4 ")

if int(coord_list[0]) > 0 and int(coord_list[1]) > 0:
    print(f"Точка с координатами {coord_list[0]},{coord_list[1]} находится в первой четверти")
elif int(coord_list[0]) > 0 and int(coord_list[1]) < 0:
    print(f"Точка с координатами {coord_list[0]},{coord_list[1]} находится во второй четверти")
elif int(coord_list[0]) < 0 and int(coord_list[1]) < 0:
    print(f"Точка с координатами {coord_list[0]},{coord_list[1]} находится в третьей четверти")
elif int(coord_list[0]) < 0 and int(coord_list[1]) > 0:
    print(f"Точка с координатами {coord_list[0]},{coord_list[1]} находится в четвертой четверти")
else:
    print(f"Одна из точек находится на оси")