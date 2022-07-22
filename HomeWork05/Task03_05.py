import random
import sys
from tkinter import messagebox
import tkinter as tk

win_combinations = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
player_board = []
cpu_board = []
play_board = []
player_sign = ""
cpu_sign = ""

def end_game(text_head: str, text_body: str):
     if messagebox.askyesno(text_head, text_body):
         new_game()

def new_game():
    player_board.clear()
    cpu_board.clear()
    play_board.clear()
    button_restart['text'] = 'START CPU'
    for index in range(9):
        play_button[index]['state'] = tk.NORMAL
        play_button[index]['image'] = empty
        play_button[index]['background'] = "SystemButtonFace"

def two_way_button():
    if player_board == []:
        AI_move(player_board)
        button_restart['text'] = 'RESTART'

    else: new_game()


def win_condition(play_board: list, color: str):
    if len(play_board) >= 3:
        variations = [(i,j,k) for i in play_board for j in play_board for k in play_board]
        for var in variations:
            if var in win_combinations:
                victory(var, color)
                return True

def victory(combination: tuple, color: str):
    for index in range(9):
        play_button[index]['state'] = tk.DISABLED
    for index in combination:
        play_button[index]['background'] = color
    if color == "GREEN": end_game("Победа!!!", "Вонюячая железяка наказана кожанным мешком! Виват "
                                               "органика!\nЕще партеечку?")
    elif color == "BLUE": end_game("Читер!", "Ах ты грязный читер! Не честно, но зато чертовски "
                                             "приятно\nПо честному cграть не хочешь? :)")
    elif color == "GREY": end_game("Ничья", "М-да, уж. И такое бывает. Чё сражались, чё добились?\nМожет "
                                            "еще партейку?")
    else: end_game("Поражение", "Закрой это окно и выйди в настоящее! Лузер, ты проиграл...\nЕще партеечку?")

def player_move(index_button: int):
    play_button[index_button]['image'] = cross
    play_button[index_button]['state'] = tk.DISABLED
    player_board.append(index_button)
    play_board.append(index_button)
    if win_condition(player_board, "GREEN"): return
    elif len(play_board) == 9:
        victory(play_board, "GREY")
        return
    else:
        AI_move(player_board)

def AI_move(player_board: tuple):
    cpu_goes = cpu_moves(play_board)
    play_button[cpu_goes]['image'] = zero
    play_button[cpu_goes]['state'] = tk.DISABLED
    cpu_board.append(cpu_goes)
    play_board.append(cpu_goes)
    if win_condition(cpu_board, "RED"):
        return
    elif len(play_board) == 9:
        victory(play_board, "GREY")
        return
    else:
        return cpu_board

def cpu_moves(play_board: list):
    corners = {0,2,4,6}
    opponent_trap = [(0,2), (2,8), (8,6), (6,0)]
    if len(play_board) == 9:
        return
    if 4 not in play_board:
        cpu_goes = 4
        return cpu_goes
    for win_combo in win_combinations:
        count = 0
        strike = 0
        for win_place in win_combo:
            if int(win_place) in cpu_board:
                count = count + 1
            else:
                strike = win_place
        if count == 2 and strike not in play_board:
            return strike
    for win_combo in win_combinations:
        count = 0
        strike = 0
        for win_place in win_combo:
            if int(win_place) in player_board:
                count = count + 1
            else:
                strike = win_place
        if count == 2 and strike not in play_board:
            return strike
    if 4 in cpu_board:
        for i in corners:
            if i in cpu_board:
                match i:
                    case 0, 8:
                        if 6 not in play_board: return 6
                        if 2 not in play_board: return 2
                    case 2, 6:
                        if 6 not in play_board: return 0
                        if 2 not in play_board: return 8
            if i not in play_board: return i
    if 4 in cpu_board:
        for i in opponent_trap:
            if i in player_board:
                match i:
                    case (0, 2):
                        if 7 not in play_board: return 7
                    case (2, 8):
                        if 3 not in play_board: return 3
                    case (6, 8):
                        if 1 not in play_board: return 1
                    case (0, 6):
                        if 6 not in play_board: return 5
    while True:
        if len(play_board) == 9: break
        cpu_goes = random.randint(0, 8)
        if cpu_goes not in play_board: return cpu_goes

cheat = []
def enter_cheat(symbol: str):
    cheat.append(symbol)
    if symbol not in ['i', 'd', 'q']: cheat.clear()
    if ''.join(cheat) == 'iddqd':
        cheat.clear()
        victory((0, 1, 2, 3, 4, 5, 6, 7, 8), "BLUE")

def press_key(event):
    enter_cheat((event.char).lower())

win = tk.Tk()
photo = tk.PhotoImage(file="Data/ico_cross.png")
cross = tk.PhotoImage(file="Data/cross.png")
zero = tk.PhotoImage(file="Data/zero.png")
empty = tk.PhotoImage(file="Data/empty.png")

win.iconphoto(False, photo)
win.title("Игра КрестНолов")
win.geometry('420x470+900+400')
win.resizable(False,False)
win.wm_attributes("-topmost", 1)
win.bind('<Key>', press_key)

name_game = tk.Label(win, text="Игра КрестНолов", font= ('Calibri 22 bold'), width=20, height=1)

play_button = [0 for x in range(9)]
for index in range(9):
    play_button[index] = tk.Button(win, width=100,height=100, borderwidth=1,
                                   image= empty, command=lambda index=index: player_move(index))
button_restart = tk.Button(win, text="START CPU",width=14,height=2, command=two_way_button)

name_game.grid(row=0,column =0, columnspan=3)

play_button[0].grid(row=1,column=0, sticky='e')
play_button[1].grid(row=1,column=1)
play_button[2].grid(row=1,column=2,sticky='w')
play_button[3].grid(row=2,column=0, sticky='e')
play_button[4].grid(row=2,column=1)
play_button[5].grid(row=2,column=2,sticky='w')
play_button[6].grid(row=3,column=0, sticky='e')
play_button[7].grid(row=3,column=1)
play_button[8].grid(row=3,column=2, sticky='w')
button_restart.grid(row=4,column=1)

[win.grid_columnconfigure(i, minsize= 140, pad= 0) for i in range(3)]
[win.grid_rowconfigure(i,pad=15) for i in range(4)]
win.mainloop()