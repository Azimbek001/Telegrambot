import random
import sqlite3

def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute("CREATE TABLE IF NOT EXISTS mentors  "
               "(id INTEGER PRIMARY KEY,"
               "name VARCHAR (50), "
               "age INTEGER , "
               "direction VARCHAR (50) ,"
               "group VARCHAR (50)  ")

    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT OR IGNORE INTO mentors VALUES (?, ?, ?, ?, ?)",
                       tuple(data.values()))
        db.commit()


async def sql_command_random():
    result = cursor.execute("SELECT * FROM mentors").fetchall()
    random_user = random.choice(result)
    return random_user


async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_command_delete(id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (id,))
    db.commit()