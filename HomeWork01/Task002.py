select = [True, False]
for x in select:
    for y in select:
        for z in select:
            if not(x or y or z) == (not x and not y and not z):
                print(f"При X={x}, Y={y} и Z={z} утверждение истинно")
            else:
                print(f"При X={x}, Y={y} и Z={z} утверждение ложно")