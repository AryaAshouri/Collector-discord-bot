import discord, colorama
from colorama import Fore
from discord.ext import commands
from art import text2art
from data import *

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
    author_all_roles = []
    for i in message.author.roles:
        author_all_roles.append(i.name)
    if ("Administrator" in author_all_roles):
        await message.channel.purge(limit=int(num)+1)
    else:
        await message.reply(f"Hey {message.author} only admins could use this command")

bot.run("MTEyMjkzOTUyNDg1MTQ0OTg5MA.Gea3w2.oiW_i68PvvRPlLqYw-TrESLFBSJpsfRxuUDxX8")
