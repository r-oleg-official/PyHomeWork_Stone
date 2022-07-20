def enter_int_number():
    while True:
        try:
            number = int(input("Введите целое число: "))
            break
        except ValueError:
            print("Требуется ввести целое число")
    return number


def factorial(number: int):
    fact = 1
    for index in range(1, int(number) + 1):
        fact *= index
    return fact


number = enter_int_number()

print(f"Факториалом числа {number} является {factorial(number)}")
