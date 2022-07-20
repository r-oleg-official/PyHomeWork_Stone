print(" 2 | 1 \n---+---\n 3 | 4 ")

num_plane = int(input("Введите номер плоскости: "))
match num_plane:
    case 1:
        print(f"В {num_plane} плоскости X = [0,+inf) и Y = [0,+inf)")
    case 2:
        print(f"В {num_plane} плоскости X = [0,-inf) и Y = [0,+inf)")
    case 3:
        print(f"В {num_plane} плоскости X = [0,-inf) и Y = [0,-inf)")
    case 4:
        print(f"В {num_plane} плоскости X = [0,+inf) и Y = [0,-inf)")
    case num_plane:
        print("Такой плоскости не существует")