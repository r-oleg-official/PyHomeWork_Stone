import os
import tkinter as tk
from app.controller import db_sqlite3 as sqdb


def read_log():
    path = 'data/log.txt'
    if os.path.isfile(path):
        with open(path, 'r') as data:
            db_path = data.readline()
        if os.path.isfile(db_path):
            return db_path
    else: return False

def write_log(path):
    log_path = 'data/log.txt'
    with open(log_path, 'w') as data:
        data.write(path)


def refresh_table(table):
    table.delete(*table.get_children())
    file_data = sqdb.get_data()
    for row in file_data:
        table.insert('', tk.END, values=row)