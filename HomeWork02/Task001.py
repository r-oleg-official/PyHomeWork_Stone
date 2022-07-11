def enter_float_number():
    while(True):
        try:
            number = input("Введите вещественное число: ")
            float(number)
            break
        except ValueError:
            print("Требуется ввести вещественное число")
    return number

def summ_digit(number: any):
    summa = 0
    num = str(number).replace(".", "")
    for index in num:
        summa += int(index)
    return summa

number = enter_float_number()

print(f"В числе {number} сумма всех цифр равна {summ_digit(number)}")