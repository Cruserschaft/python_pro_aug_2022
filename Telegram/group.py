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


def sq_search(val, ret_users=False, ret_id_group=False):
    with sqlite3.connect("smokers.db") as con:
        cursor = con.cursor()
        if not ret_users and not ret_id_group:
            return bool(len(cursor.execute("SELECT * FROM person WHERE person_id IS (?)", (val,)).fetchall()))
        tmp = cursor.execute("SELECT group_id FROM person WHERE person_id IS (?)", (val,)).fetchone()[0]
        if ret_id_group:
            return tmp
        tmp2 = cursor.execute("SELECT person_id FROM person WHERE group_id IS (?)", (tmp,)).fetchall()
        return [x[0] for index, x in enumerate(tmp2)]


def sq_search_by_grp_id(val, ret_mode=False):
    with sqlite3.connect("smokers.db") as con:
        cursor = con.cursor()
        return bool(len(cursor.execute("SELECT * FROM person WHERE group_id IS (?)", (val,)).fetchall()))


def sq_remove(val):
    with sqlite3.connect("smokers.db") as con:
        cursor = con.cursor()
        cursor.execute("DELETE FROM person WHERE person_id IS (?)", (val,))


def register_user(id, id_group, name):
    with sqlite3.connect("smokers.db") as con:
        cursor = con.cursor()
        cursor.execute("""INSERT INTO person VALUES (?,?,?,?)""", (name, id, id_group, "user"))


def create_group(id, name):
    tmp = rand_id()
    with sqlite3.connect("smokers.db") as con:
        cursor = con.cursor()
        cursor.execute("INSERT INTO person VALUES (?,?,?,?)", (name, id, tmp, "admin"))
    return tmp

