import sqlite3 as sqdb


def create_table():
    global base
    print('Create table')
    base.execute('CREATE TABLE IF NOT EXISTS phone_list (cell_id PRIMARY KEY, name, phone)')
    base.commit()

def get_data():
    global base
    res = cur.execute('SELECT name, phone, cell_id FROM phone_list').fetchall()
    return res

def add_item(new_item):
    global base
    cur.execute('INSERT INTO phone_list (name, phone) VALUES (?, ?)', new_item)
    base.commit()

def update_item(update_item, old_item):
    global base
    cur.execute(f'UPDATE phone_list SET (name, phone) = {update_item} WHERE cell_id = {old_item[2]}')
    base.commit()

def delete_item(focus_item):
    global base
    cur.execute(f'DELETE FROM phone_list WHERE cell_id = {focus_item}')
    base.commit()

def init(full_file_name_db):
    global base, cur
    if full_file_name_db:
        base = sqdb.connect(full_file_name_db)
        cur = base.cursor()
        return True
    else: return False

    create_table()