import sqlite3, datetime
from datetime import datetime

def send(message):
    now = datetime.now()
    connection = sqlite3.connect("Database/data.db")
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Send(
    user_name,
    user_id,
    method,
    content,
    "date",
    "time")''')

    cursor.execute('''INSERT INTO Send(
    user_name,
    user_id,
    method,
    content,
    "date",
    "time")

    VALUES (?, ?, ?, ?, ?, ?)''', (
    message.author.name,
    message.author.id,
    "send",
    message.content,
    now.strftime("%Y:%m:%d"),
    now.strftime("%H:%M:%S")))

    connection.commit()
    connection.close()

def delete(message):
    now = datetime.now()
    connection = sqlite3.connect("Database/data.db")
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS "Delete"(
    user_name,
    user_id,
    method,
    content,
    "date",
    "time")''')

    cursor.execute('''INSERT INTO "Delete"(
    user_name,
    user_id,
    method,
    content,
    "date",
    "time")

    VALUES (?, ?, ?, ?, ?, ?)''', (
    message.author.name,
    message.author.id,
    "delete",
    message.content,
    now.strftime("%Y:%m:%d"),
    now.strftime("%H:%M:%S")))

    connection.commit()
    connection.close()

def edit(before, after):
    now = datetime.now()
    connection = sqlite3.connect("Database/data.db")
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Edit(
    user_name,
    user_id,
    method,
    before,
    after,
    "date",
    "time")''')

    cursor.execute('''INSERT INTO Edit(
    user_name,
    user_id,
    method,
    before,
    after,
    "date",
    "time")

    VALUES (?, ?, ?, ?, ?, ?, ?)''', (
    after.author.name,
    after.author.id,
    "edit",
    before.content,
    after.content,
    now.strftime("%Y:%m:%d"),
    now.strftime("%H:%M:%S")))

    connection.commit()
    connection.close()
