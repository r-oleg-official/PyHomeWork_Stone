import func

random_list = func.random_fill_list(20, 0 , 10)
print(random_list)

new_list =[]

for orig_element in random_list:
    count = 0
    for compare_element in random_list:
        if orig_element == compare_element: count += 1
    if count == 1: new_list.append(orig_element)

print(new_list)