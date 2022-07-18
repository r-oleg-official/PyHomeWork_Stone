import func

number = func.enter_int_number()
simple_devs = []
for dev in range (1, number):
    if (number%dev == 0) and func.is_simple(dev):
        simple_devs.append(dev)
print(simple_devs)