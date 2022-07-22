import os

import func

def enter_choice(text_ok = "Введите 1 (для сжатия) или 2 (для распаковки): ", text_error = "Ошибка ввода!"):
    while True:
        try:
            number = int(input(text_ok))
            if 0 < number < 3: break
            else: print(text_error)
        except ValueError:
            print(text_error)
    return number

def enter_file_name():
    while True:
        try:
            file_name = input("Введите имя файла вместе с его расширением: ")
            path = os.path.join('Data', file_name)
            with open(path, 'r') as data:
                data.readline()
            break
        except:
            print("Такого файла не существует!")
    return file_name

def open_file(file_name: str):
    path = os.path.join('Data', file_name)
    with open(path, 'r') as data:
        string_data = data.readline()
    return string_data

def compress_file(string_data: str):
    counter = 0
    new_string = ''
    prev_char = string_data[0]
    for index in range(len(string_data)):
        if string_data[index] != prev_char:
            if counter == 1:
                new_string += prev_char
            else:
                new_string += prev_char + str(counter)
                counter = 1
        else:
            counter += 1
        prev_char = string_data[index]
        if index == len(string_data) - 1:
            new_string += prev_char + str(counter)
    return new_string

def uncompress_file(string_data: str):
    new_string = ''
    string_data += "+"
    index = 0
    while index < len(string_data)-1:
        char_data = ""
        num_data = ""
        if not string_data[index].isdigit() and not string_data[index+1].isdigit():
            new_string += string_data[index]
            index += 1
        if not string_data[index].isdigit() and string_data[index + 1].isdigit():
            char_data += string_data[index]
            index += 1
            while string_data[index].isdigit():
                    num_data += string_data[index]
                    index += 1
            new_string += char_data * int(num_data)

    return new_string

choice = enter_choice()
file_name = enter_file_name()

match choice:
    case 1:
        print(f"Оригинальный файл: {open_file(file_name)}")
        print(f"После сжатия: {compress_file(open_file(file_name))}")
    case 2:
        print(f"Оригинальный файл: {open_file(file_name)}")
        print(f"После распаковки: {uncompress_file(open_file(file_name))}")