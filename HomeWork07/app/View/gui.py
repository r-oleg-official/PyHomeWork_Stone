import os
from tkinter import filedialog, ttk
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename
import tkinter as tk
from appdata.model import tel


main_window = None
main_table = None
name_label = ''
phone_label = ''
window_width = 500
window_height = 400

def init_program():

    global main_window

    main_window = tk.Tk()

    init_main_window(main_window)
    init_menu_bar(main_window)
    init_main_table(main_window)
    init_search_entry(main_window)
    main_window.mainloop()

def init_main_window(window):

    global window_width, window_height

    window_full_width = window.winfo_screenwidth()
    window_full_height = window.winfo_screenheight()

    window.title('Телефонный справочник')
    window.geometry(f'{window_width}x{window_height}+{(window_full_width-window_width)//2}+{(window_full_height-window_height)//2}')

def init_menu_bar(window):

    menu_bar = tk.Menu(window, tearoff=0)
    window.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0)

    file_menu.add_command(label='Подключиться...', command= lambda: connect_db_select(main_window))
    file_menu.add_command(label='Открыть', command=open_file)
    file_menu.add_command(label='Сохранить')
    file_menu.add_command(label='Сохранить как...')
    file_menu.add_separator()
    file_menu.add_command(label='Выйти')

    menu_bar.add_cascade(label='База данных', menu=file_menu)

def init_main_table(window):

    global main_table, window_width, window_height

    main_table = ttk.Treeview(window, show='headings', columns=['Имя', 'Телефон'])
    main_table.column('Имя',width=(window_width-140)//3*2,anchor='w')
    main_table.column('Телефон',width=(window_width-140)//3,anchor='e')
    main_table.heading('Имя', text='Имя',anchor='center')
    main_table.heading('Телефон', text='Телефон',anchor='center')

    main_table.place(x=20, y=40, height=window_height-40)

def init_search_entry(window):

    search_entry = tk.Entry(window)
    search_entry.place(x=20, y=10, width=360)

def init_button_panel(window):

    btn_new = tk.Button(window)
    btn_new = tk.Button(window)
    btn_new = tk.Button(window)

def open_file():

    global main_table

    print('Открыть файл')
    full_file_name = askopenfilename()
    print(full_file_name)
    with open(full_file_name, 'r') as data:
        file_data = data.readlines()
    print(file_data)

    new_file = {("Panfilov Kirill", 89545134837),
                ("Anna sdffsf", 65468768746),
                ("sdjn nlknlnkl", 64684646468)}
    for row in new_file:
        main_table.insert('', tk.END, values=row)


def connect_db_select(window):

    global window_width, window_height

    this_width = 400
    this_height = 90
    window_full_width = main_window.winfo_screenwidth()
    window_full_height = main_window.winfo_screenheight()

    connect_db_window = tk.Toplevel(window)
    connect_db_window.resizable(False, False)
    connect_db_window.geometry(
        f'{this_width}x{this_height}+{(window_full_width - this_width) // 2}+{(window_full_height - this_height // 2) // 2}')
    connect_db_window.wm_attributes("-topmost", 1)
    db_label = tk.Label(connect_db_window, text='Путь к BD')
    db_path_entry = tk.Entry(connect_db_window, width=30)
    btn_db_browse = tk.Button(connect_db_window, text='Обзор...', command=lambda: connect_db_browse(db_path_entry))
    btn_db_confirm = tk.Button(connect_db_window, text='OK', command=lambda: connect_db_confirm(connect_db_window, db_path_entry))
    db_label.grid(row=0, column=1, sticky='e')
    db_path_entry.grid(row=0, column=2, padx=5, pady=5, sticky='we')
    btn_db_browse.grid(row=1, column=1, sticky='we')
    btn_db_confirm.grid(row=1, column=2,  sticky='we')
    connect_db_window.mainloop()

def connect_db_browse(entry_field):
    global main_table


    full_file_name = askopenfilename()
    entry_field.insert(0, full_file_name)

    # with open(full_file_name, 'r') as data:
    #     file_data = data.readlines()
    # print(file_data)
    #
    # new_file = {("Panfilov Kirill", 89545134837),
    #             ("Anna sdffsf", 65468768746),
    #             ("sdjn nlknlnkl", 64684646468)}
    # for row in new_file:
    #     main_table.insert('', tk.END, values=row)

def connect_db_confirm(window, entry_field):
    path_db = entry_field.get()
    window.destroy()
    with open(path_db, 'r') as data:
        file_data = data.readlines()
    print(file_data)


init_program()