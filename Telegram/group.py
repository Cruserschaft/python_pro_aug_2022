import sqlite3
import random
import config


with sqlite3.connect("smokers.db") as con:
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS person(name, person_id, group_id, rights)""")


def rand_id():
    tmp = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!#$%^&*()"
    res = ""
    for i in range(config.ID_MAX_VALUE):
        res += tmp[random.randint(0, len(tmp)-1)]
    return res


def sq_search(val):
    with sqlite3.connect("smokers.db") as con:
        cursor = con.cursor()
        return bool(len(cursor.execute("SELECT * FROM person WHERE person_id IS (?)", (val,)).fetchall()))

def sq_search_byID(val):
    with sqlite3.connect("smokers.db") as con:
        cursor = con.cursor()
        return bool(len(cursor.execute("SELECT * FROM person WHERE group_id IS (?)", (val,)).fetchall()))

def register_user(id, id_group, name):
    pass


def create_group(id, name):
    tmp = rand_id()
    with sqlite3.connect("smokers.db") as con:
        cursor = con.cursor()
        cursor.execute("INSERT INTO person VALUES (?,?,?,?)", (name, id, tmp, "admin"))
    return tmp
