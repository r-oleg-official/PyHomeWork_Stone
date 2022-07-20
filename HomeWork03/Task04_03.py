import func

number = func.enter_int_number()

num = number
binary_num = []

while num>1:
    binary_num.append(num%2)
    num //= 2
binary_num.append(num)

new_number = ""
for index in range(len(binary_num)):
    new_number += str(binary_num[len(binary_num)-index-1])
print(F"Число {number} равно числу {new_number} в двоичной системе")