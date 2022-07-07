print(" 1 | 2 \n---+---\n 4 | 3 ")

num_plane = int(input("Введите номер плоскости: "))
if num_plane in range (1,5) :
    match num_plane:
        case 1:
            print(f"В {num_plane} плоскости X = [0,-inf) и Y = [0,+inf)")
        case 2:
            print(f"В {num_plane} плоскости X = [0,+inf) и Y = [0,+inf)")
        case 3:
            print(f"В {num_plane} плоскости X = [0,+inf) и Y = [0,-inf)")
        case 4:
            print(f"В {num_plane} плоскости X = [0,-inf) и Y = [0,-inf)")
else:
    print("Такой плоскости не существует")