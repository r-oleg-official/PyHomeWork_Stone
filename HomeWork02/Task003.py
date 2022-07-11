def enter_int_number():
    while True:
        try:
            number = int(input("Введите целое число: "))
            break
        except ValueError:
            print("Требуется ввести целое число")
    return number

def create_list(number: int):
    new_list = []
    for element in range(1, number+1):
        new_list.append((1+1/element)**element)
    return new_list

def print_list(original_list: list):
    index = 1
    summa = 0
    for element in original_list:
        print(f"{index} элемент последовательности из {len(original_list)} чисел равен {element}")
        index += 1
        summa += element
    print(f"\nСумма всех элементов равна {summa}")

number = enter_int_number()
my_list = create_list(number)
print_list(my_list)
