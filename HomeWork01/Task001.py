week_day = int(input("Введите день недели: "))
if week_day in range(1,6):
    print("Будний день")
elif week_day in range(6,8):
    print("Выходной день")
else:
    print(f"{week_day} - такого дня недели нет")