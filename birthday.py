import sqlite3, datetime
from datetime import datetime

connection = sqlite3.connect("Database/birthday.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Birthday(
user_name,
user_id,
birthday)''')

def birthday_teller(status):
    pass

def birthday_adder(message, birthday):
    cursor.execute('''INSERT INTO Birthday(
    user_name,
    user_id,
    birthday)

    VALUES (?, ?, ?)''', (
    message.author.name,
    message.author.id,
    birthday))

def birthday_updater(message, birthday):
    cursor.execute(f'''UPDATE Birthday
      SET birthday = ?

      WHERE user_id = ?''', (
      birthday,
      message.author.id))
