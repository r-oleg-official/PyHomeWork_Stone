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
            number = float(input(text_ok))
            break
        except ValueError:
            print(text_error)
    return number

def random_fill_list(size: int, min_value = 0, max_value = 100):
    new_list = []
    for index in range(size + 1):
        new_list.append(randint(min_value, max_value))
    return new_list

def digit_after_dot_counter(num:float):
    count = 0
    div = 1
    while True:
        if not(num*div == int(num*div)):
            count += 1
            div *= 10
        else: break
    return count

def is_simple(number: int):
    for dev in range (2,number,2):
        if number%dev == 0: return False
    return True