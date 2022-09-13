import sqlite3
import random
import config


with sqlite3.connect("smokers.db") as con:
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS person(name, id, rights)""")


def sq_search(val):
    with sqlite3.connect("smokers.db") as con:
        cursor = con.cursor()
        return bool(len(cursor.execute("SELECT * FROM person WHERE id IS (?)", (val,)).fetchall()))

def sq_register(id, rand):
    pass


def rand_id():
    tmp = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!#$%^&*()"
    res = ""
    for i in range(config.ID_MAX_VALUE):
        res += tmp[random.randint(0, len(tmp)-1)]
    return res


def create_group(id):
    if not sq_search(id):
        group_id = rand_id()
        sq_register(id, group_id)
        return group_id
    return "Увы, вы состоите в другой групе"
