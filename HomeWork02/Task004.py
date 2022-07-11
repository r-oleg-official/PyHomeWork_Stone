from random import randint


def enter_int_number():
    while True:
        try:
            number = int(input("Введите размер списка: "))
            break
        except ValueError:
            print("Требуется ввести целое число")
    return number


def enter_coords():
    while True:
        try:
            coord = input("Введите индексы требуемых элементов (через пробел): ")
            coords = coord.split(" ")
            break
        except ValueError:
            print("Введите целые числа через пробел")
    return coords


def fill_list(number: int):
    new_list = []
    for index in range(number + 1):
        new_list.append(randint(-number, number))
    return new_list


def multiply_elements(original_list: list, coords: list):
    multiply = 1
    for element in coords:
        multiply *= original_list[int(element)]
    return multiply


def print_list(original_list: list):
    print("{: >7}".format("Индекс"), end=" ")
    for index in range(len(original_list)):
        print("{: ^3}".format(index), end=" | ")
    print("{: >7}".format("\nЭлемент"), end=" ")
    for element in original_list:
        print("{: ^3}".format(element), end=" | ")
    print("\n")


number = enter_int_number()
new_list = fill_list(number)
print_list(new_list)
coords = enter_coords()
print(f"Произведение элементов на позициях {coords} равно {multiply_elements(new_list, coords)}")
