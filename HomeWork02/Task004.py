from random import randint
import func

def enter_coords():
    while True:
        try:
            coord = input("Введите индексы требуемых элементов (через пробел): ")
            coords = coord.split(" ")
            break
        except ValueError:
            print("Введите целые числа через пробел")
    return coords


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


number = func.enter_int_number("Введите размер списка: ")
new_list = func.random_fill_list(number)
print_list(new_list)
coords = enter_coords()
print(f"Произведение элементов на позициях {coords} равно {multiply_elements(new_list, coords)}")
