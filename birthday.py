import sqlite3
from datetime import date
from datetime import datetime

def birthday_teller(status):
    connection = sqlite3.connect("Database/birthday.db")
    cursor = connection.cursor()

    if (status == "activate"):
        all_user_name = cursor.execute('''SELECT user_name FROM Birthday''')
        all_user_name = all_user_name.fetchall()
        all_user_name = [i[0] for i in all_user_name]

        all_user_birthday = cursor.execute('''SELECT birthday FROM Birthday''')
        all_user_birthday = all_user_birthday.fetchall()
        all_user_birthday = [i[0] for i in all_user_birthday]

        all_info_names_and_birthdays = dict(zip(all_user_name, all_user_birthday))
        now_date = datetime.now().now.strftime("%Y/%m/%d")
        now_time = datetime.now().now.strftime("%H:%M")
        for name, birthday in all_info_names_and_birthdays:
            

    elif (status == "deactivate"):
        pass

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

    all_user_id = cursor.execute('''SELECT user_id FROM Birthday''')
    all_user_id = all_user_id.fetchall()

    if (message.author.id not in [i[0] for i in all_user_id]):
        return False
    else:
        cursor.execute(f'''UPDATE Birthday
          SET birthday = ?

        WHERE user_id = ?''', (
        birthday,
        message.author.id))

        connection.commit()
        connection.close()
