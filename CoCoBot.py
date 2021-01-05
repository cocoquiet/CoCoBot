import discord
import asyncio
from discord.ext import commands, tasks
from discord.utils import get

import random
import datetime
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pprint import pprint

import os

bot = commands.Bot(command_prefix="/")

bot.remove_command("help")

startup_extensions = ['cogs.help', 'cogs.CoCo', 'cogs.admin', 'cogs.music', 'cogs.musicbot', 'cogs.game', 'cogs.util', 'cogs.crawling', 'cogs.github', 'cogs.ping', 'cogs.secret']

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print("cannot be loaded {}\n{}".format(extension, e))

@bot.event
async def on_ready():
    print("코코 대기 중")
    print(bot.user.name)
    print(bot.user.id)
    print("=============")

    now = datetime.datetime.now()
    nowTime = now.strftime("%H")

    await bot.change_presence(status=discord.Status.online, activity=discord.Game("주인놈이랑 코딩"))

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)