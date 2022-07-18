import os

def add_employee (text_name: str):
    name_employee = input(text_name)
    if name_employee == "отмена":
        return False
    while True:
        try:
            salary_employee = float(input("Введите зарплату работника: "))
            break
        except ValueError:
            print("Зарплата исчисляется в цифрах, можно даже в дробных, но в ЦИФРАХ!")
    path = os.path.join('folder', 'employee.txt')
    with open(path, 'a') as data:
        data.write(name_employee + " " + str(salary_employee) + "\n")
    return True

start_enter = True
average_salary = 0
count = 0

while (start_enter):
    start_enter = add_employee("Введите имя сотрудника или введите 'отмена' для выхода: ")

path = os.path.join('folder', 'employee.txt')
with open(path, 'r') as data:
    workers = data.readlines()
    print("Сотрудники с зарпалатой менее 20000:")
    for employee in workers:
        employee = employee.replace('\n', '').split(' ')
        if float(employee[1]) < 20000: print(employee[0] + " (" + employee[1] + ")")
        count += 1
        average_salary += float(employee[1])

print(f"Средняя зарплата всех сотрудников равна {round(average_salary/count, 2)}")

