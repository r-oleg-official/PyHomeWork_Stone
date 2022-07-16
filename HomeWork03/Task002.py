input_data = input("Введите элементы списка из целых чисел: ")
original_list = input_data.replace(" ", "").split(",")

if len(original_list)%2 == 0:
    lenght_list = len(original_list)//2
else:
    lenght_list = len(original_list) // 2 + 1

for index in range(lenght_list):
    print(int(original_list[index])*int(original_list[len(original_list) - 1 - index]))