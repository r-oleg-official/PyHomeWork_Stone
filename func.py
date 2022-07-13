from random import randint

def enter_int_number(text_ok = "Введите целое число: ", text_error = "Требуется ввести ЦЕЛОЕ число!"):
    while True:
        try:
            number = int(input(text_ok))
            break
        except ValueError:
            print(text_error)
    return number

def enter_float_number(text_ok = "Введите существенное число: ", text_error = "Требуется ввести СУЩЕСТВЕННОЕ число!"):
    while True:
        try:
            number = int(input(text_ok))
            break
        except ValueError:
            print(text_error)
    return number

def random_fill_list(size: int, min_value = 0, max_value = 100):
    new_list = []
    for index in range(size + 1):
        new_list.append(randint(min_value, max_value))
    return new_list