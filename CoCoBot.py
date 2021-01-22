import discord
import asyncio
from discord.ext import commands
from discord.utils import get

import youtube_dl

import random
import datetime
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pprint import pprint

import os

bot = commands.Bot(command_prefix="/")

bot.remove_command("help")

startup_extensions = ['cogs.help', 'cogs.CoCo', 'cogs.admin', 'cogs.music', 'cogs.RSP', 'cogs.omok', 'cogs.util', 'cogs.crawling', 'cogs.github', 'cogs.ping', 'cogs.secret']

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print("cannot be loaded {}\n{}".format(extension, e))

@bot.event
async def on_ready():
    print("빌드 성공")
    print(bot.user.name)
    print(bot.user.id)
    print("=============")

    await bot.change_presence(status=discord.Status.online, activity=discord.Game("주인놈이랑 코딩"))

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)