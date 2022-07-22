import func

number = func.enter_int_number()
simple_devs = [x for x in range(1,number) if number%x == 0 and func.is_simple(x)]
print(simple_devs)