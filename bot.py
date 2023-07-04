import discord, colorama
from colorama import Fore
from discord.ext import commands
from art import text2art
from data import *
from birthday import *

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="")

@bot.event
async def on_ready():
    print(text2art("Bot  is  ready"))

@bot.event
async def on_message(message):
    send(message)
    await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
    delete(message)

@bot.event
async def on_message_edit(before, after):
    edit(before, after)

@bot.command()
async def clear(message, num):
    author_all_roles = [i.name for i in message.author.roles]
    if ("Administrator" in author_all_roles):
        await message.channel.purge(limit=int(num)+1)
    else:
        await message.reply(f"Hey {message.author} only admins could use this command")

@bot.command()
async def birthday(message, status, date=None):
    if (date != None):
        if (status == "add"):
            result = birthday_adder(message, date)
            if (result == False):
                await message.reply("You have already added your Birthday")
            else:
                await message.reply('Your birthday has been added succesfuly')
        elif (status == "update"):
            result = birthday_updater(message, date)
            if (result == False):
                await message.reply("You haven't added your birthday yet")
            else:
                await message.reply('Your birthday has been updated succesfuly')

        else:
            await message.reply("Command is not acceptable")
    else:
        if (status == "activate"):
            author_all_roles = [i.name for i in message.author.roles]
            if ("Administrator" in author_all_roles):
                result = birthday_teller(status)
                await message.reply("Birthday has been activated succesfuly")
                [await message.channel.send(f"The day has been arrived!\nIts' {i}'s birthday :partying_face::tada:") for i in result]
            else:
                await message.reply(f"Hey {message.author} only admins could use this command")

        elif (status == "deactivate"):
            author_all_roles = [i.name for i in messagulte.author.roles]
            if ("Administrator" in author_all_roles):
                birthday_teller(status)
                await message.reply("Birthday has been deactivated succesfuly")
            else:
                await message.reply(f"Hey {message.author} only admins could use this command")

        elif (status == "delete"):
            result = birthday_deleter(message)
            if (result == False):
                await message.reply("You haven't added your birthday yet")
            else:
                await message.reply("Your birthday has been deleted succesfuly")

        else:
            await message.reply("Command is not acceptable")


bot.run("BOT_TOKEN")
