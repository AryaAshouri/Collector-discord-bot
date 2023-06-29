import sqlite3, datetime
from datetime import datetime

def birthday_teller(status):
    connection = sqlite3.connect("Database/birthday.db")
    cursor = connection.cursor()

def birthday_adder(message, birthday):
    connection = sqlite3.connect("Database/birthday.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Birthday(
    user_name,
    user_id,
    birthday)''')

    all_user_id = cursor.execute('''SELECT user_id FROM Birthday''')
    all_user_id = all_user_id.fetchall()

    if (message.author.id in [i[0] for i in all_user_id]):
        return False
    else:
        cursor.execute('''INSERT INTO Birthday(
        user_name,
        user_id,
        birthday)

        VALUES (?, ?, ?)''', (
        message.author.name,
        message.author.id,
        birthday))

        connection.commit()
        connection.close()

def birthday_updater(message, birthday):
    connection = sqlite3.connect("Database/birthday.db")
    cursor = connection.cursor()
    cursor.execute(f'''UPDATE Birthday
      SET birthday = ?

    WHERE user_id = ?''', (
    birthday,
    message.author.id))

    connection.commit()
    connection.close()
