import discord
import asyncio
from discord.ext import commands
from discord.utils import get

from config import *

import youtube_dl

import random
import datetime
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pprint import pprint

import os

bot = discord.Bot()

if __name__ == '__main__':
    for extension in EXTENSIONS:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('cannot be loaded {}\n{}'.format(extension, e))

@bot.event
async def on_ready():
    print('Build succeeded')
    print(botName)
    print(botID)
    print('=============')

    await bot.change_presence(status=discord.Status.online, activity=discord.Game(f'{CoCoPrefix}help 치면 사용법 설명'))

access_token = os.environ['BOT_TOKEN']
bot.run(access_token)