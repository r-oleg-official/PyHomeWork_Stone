from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter as tk
from app.controller import db_sqlite3 as sqdb
from tkinter import messagebox as mb

from app.model import func

# ================================= ПЕРЕМЕННЫЕ ============================================

main_window = None
main_table = None
window_width = 400
window_height = 400
work_file = ''

# ================================== ИНИЦИАЛИЗАЦИЯ ========================================

def init_program():
    global main_window, main_table
    main_window = tk.Tk()
    init_main_window(main_window)
    init_menu_bar(main_window)
    init_search_entry(main_window)
    init_main_table(main_window)
    init_task_bar(main_window, func.read_log())
    if sqdb.init(func.read_log()):
        file_data = sqdb.get_data()
        for row in file_data:
            main_table.insert('', tk.END, values=row)
    main_window.mainloop()

def init_main_window(window):
    global window_width, window_height
    window_full_width = window.winfo_screenwidth()
    window_full_height = window.winfo_screenheight()
    window.title('Телефонный справочник')
    window.geometry(f'{window_width}x{window_height}+{(window_full_width-window_width)//2}+{(window_full_height-window_height)//2}')
    window.resizable(False, False)

def init_menu_bar(window):
    menu_bar = tk.Menu(window, tearoff=0)
    window.config(menu=menu_bar)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label='Открыть', command=lambda: open_file(window))
    file_menu.add_command(label='Сохранить как DB SQLite3', command=lambda: save_as_db(window))
    file_menu.add_command(label='Сохранить как CSV файл', command=lambda: save_as_csv(window))
    file_menu.add_separator()
    file_menu.add_command(label='Выйти', command=window.destroy)
    menu_bar.add_cascade(label='База данных', menu=file_menu)
    menu_bar.add_command(label='Помощь', command=user_help)

def user_help():
    mb.showinfo('Помощь', 'В данной версии можно открывать БД SQLite3. Добавлять, изменять и удалять элементы при помощи правой кнопки мыши')

def init_search_entry(window):
    search_entry = tk.Entry(window)
    search_entry.place(x=20, y=10, width=360)
    search_entry.insert(0, 'Поиск. Escape для отмены поиска')
    def get_value(event):
        if event.keycode == 27:
            search_entry.delete("0", tk.END)
            search_value('')
        else:
            value = search_entry.get()
            search_value(value+event.char)
    def clear_value(event):
        search_entry.delete("0", tk.END)
    search_entry.bind('<Key>', get_value)
    search_entry.bind('<Button-1>', clear_value)

def search_value(value):
    global main_table
    main_table.delete(*main_table.get_children())
    for i in sqdb.get_data():
        if value in i[0] or value in i[1]:
            main_table.insert('', tk.END, values=i)


def init_main_table(window):
    global main_table, window_width, window_height
    main_table = ttk.Treeview(window, show='headings', height=200, columns=['Имя', 'Телефон'])
    main_table.column('Имя', width=200,anchor='w')
    main_table.column('Телефон', width=160,anchor='e')
    main_table.heading('Имя', text='Имя',anchor='center')
    main_table.heading('Телефон', text='Телефон',anchor='center')
    main_table.bind('<Button-3>', right_button_menu)
    main_table.place(x=20, y=40, height=window_height-60)

def init_task_bar(window,file_path):
    global work_file
    task_bar = tk.Label(window, text=f'Открыт: {file_path}', justify='right')
    task_bar.place(x=20, y=380, width=360)

def right_button_menu(event):
    global main_window
    popup_menu = tk.Menu(main_window, tearoff=0)
    rowID = event.widget.identify('item', event.x, event.y)
    event.widget.focus()
    file_menu = tk.Menu(popup_menu, tearoff=0)
    file_menu.add_command(label='Новый контакт', command=lambda: new_item_window(main_window))
    file_menu.add_separator()
    file_menu.add_command(label='Изменить контакт', command=lambda: change_item_window(main_window, rowID))
    file_menu.add_command(label='Удалить контакт', command=lambda: delete_item(event.widget, rowID))
    file_menu.post (event.x_root, event.y_root)

# ============================================== КОМАНДЫ МЕНЮ ==========================================

def open_file(window):
    global main_table
    types = (("SQLite3 DB file", "*.db"), ("all files", "*.*"))
    full_file_name = askopenfilename(title='Открыть базу данных', filetypes=types)
    init_task_bar(window, full_file_name)
    func.write_log(full_file_name)
    sqdb.init(full_file_name)
    func.refresh_table(main_table)

def save_as_db(window):
    mb.showinfo('Информация!', 'Эта функция в разработке')
    # global main_table
    # types = (("SQLite3 DB file", "*.db"),)
    # new_file_name = asksaveasfilename(title='Экспорт Базы данных SQLite3', filetypes=types, defaultextension=".db")
    # sqdb.init(new_file_name)

def save_as_csv(window):
    mb.showinfo('Информация!', 'Эта функция в разработке')
    # global main_table
    # types = (("CSV файл", "*.db"),)
    # new_file_name = asksaveasfilename(title='"Экспорт CSV файла"', filetypes=types, defaultextension=".csv")


def new_item_window(window):
    width = 300
    height = 90
    wfw = window.winfo_screenwidth()
    wfh = window.winfo_screenheight()

    new_entry_window = tk.Toplevel(window)
    new_entry_window.resizable(False, False)
    new_entry_window.geometry(f'{width}x{height}+{(wfw - width) // 2}+{(wfh - height // 2) // 2}')
    new_entry_window.wm_attributes("-topmost", 1)
    name_label = tk.Label(new_entry_window, text='Имя', justify='right')
    phone_label = tk.Label(new_entry_window, text='Телефон', justify='right')
    name_entry = tk.Entry(new_entry_window, width=30)
    phone_entry = tk.Entry(new_entry_window, width=30)
    btn_new_entry_confirm = tk.Button(new_entry_window, text='Создать', command=lambda: new_item_comfirm(new_entry_window, name_entry, phone_entry))
    btn_new_entry_cancel = tk.Button(new_entry_window, text='Отмена', command=window.destroy)
    name_label.place(x=10, y=5, width=60)
    phone_label.place(x=10, y=35, width=60)
    name_entry.place(x=70, y=5, width=220)
    phone_entry.place(x=70, y=35, width=220)
    btn_new_entry_confirm.place(x=70, y=60, width=60)
    btn_new_entry_cancel.place(x=170, y=60, width=60)
    new_entry_window.mainloop()

def new_item_comfirm(window, name_field, phone_field):
    global main_table
    new_item = (name_field.get(), phone_field.get())
    sqdb.add_item(new_item)
    func.refresh_table(main_table)
    window.destroy()

def delete_item(table, ID):
    data = tuple(table.item(ID)['values'])
    if mb.askyesno('Удаление', f'Вы точно хотите удалить {data[0]}?'):
        sqdb.delete_item(data[2])
        func.refresh_table(table)


def change_item_window(window, ID):
    global main_table
    width = 300
    height = 90
    wfw = window.winfo_screenwidth()
    wfh = window.winfo_screenheight()

    new_entry_window = tk.Toplevel(window)
    new_entry_window.resizable(False, False)
    new_entry_window.geometry(f'{width}x{height}+{(wfw - width) // 2}+{(wfh - height // 2) // 2}')
    # new_entry_window.wm_attributes("-topmost", 1)
    name_label = tk.Label(new_entry_window, text='Имя')
    phone_label = tk.Label(new_entry_window, text='Телефон')
    old_item = tuple(main_table.item(ID)['values'])
    name_entry = tk.Entry(new_entry_window, width=30)
    name_entry.insert(0, old_item[0])
    phone_entry = tk.Entry(new_entry_window, width=30)
    phone_entry.insert(0, old_item[1])
    btn_new_entry_confirm = tk.Button(new_entry_window, text='Применить', command=lambda: change_item_confirm(new_entry_window, (name_entry.get(), phone_entry.get()), old_item))
    btn_new_entry_cancel = tk.Button(new_entry_window, text='Отмена', command=window.destroy)
    name_label.place(x=10, y=5, width=60)
    phone_label.place(x=10, y=35, width=60)
    name_entry.place(x=70, y=5, width=220)
    phone_entry.place(x=70, y=35, width=220)
    btn_new_entry_confirm.place(x=60, y=60, width=80)
    btn_new_entry_cancel.place(x=160, y=60, width=80)
    new_entry_window.mainloop()

def change_item_confirm(window, update_item: tuple, old_item: tuple):
    global main_table
    sqdb.update_item(update_item, old_item)
    func.refresh_table(main_table)
    window.destroy()