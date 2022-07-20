from random import randint
import func

def fill_list(number: int):
    new_list = []
    for index in range(number + 1):
        new_list.append(randint(0, 100))
    return new_list


def mix_list(original_list: list):
    list_index = []
    new_list = original_list[:]
    for element in original_list:
        trigger = True
        while (trigger):
            index = randint(0, len(new_list) - 1)
            if index not in list_index:
                new_list[index] = element
                list_index.append(index)
                trigger = False
    return new_list


def print_list(original_list: list, text: str):
    print("{: >22}".format(text), end=" ")
    for element in original_list:
        print("{: ^4}".format(element), end=" | ")
    print("\n")


number = func.enter_int_number()
my_list = func.random_fill_list(number)
print_list(my_list, "Исходный список:")
mixed_list = mix_list(my_list)
print_list(mixed_list, "Перемещанный список:")