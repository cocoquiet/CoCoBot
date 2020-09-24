import discord
import asyncio
import random
from discord.ext import commands, tasks
import youtube_dl
import os

bot = commands.Bot(command_prefix='!!')

@bot.event
async def on_ready():
    print('코코 대기 중')
    print(bot.user.name)
    print(bot.user.id)
    print('=============')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("주인놈이랑 코딩"))

@bot.command(name='안녕')
async def hello(ctx):
    await ctx.send('안녕하세요 %s 님!' %(ctx.author))

@bot.command(name='코코야')
async def HeyYou(ctx):
    CoCoResponse = random.randint(1, 4)
    if CoCoResponse == 1:
        await ctx.send("네?")
    elif CoCoResponse == 2:
        await ctx.send("뭐")
    elif CoCoResponse == 3:
        await ctx.send("아 왜 불러ㅡㅡ")
    elif CoCoResponse == 4:
        await ctx.send("멍멍!")

@bot.command(name='가위바위보')
async def RSP(ctx, arg):
    bot_rsp = random.randint(1, 3) # 1:가위  2:바위  3:보

    if bot_rsp == 1:
        if arg == "가위":
            await ctx.send("저도 가위를 냈습니다. 비겼습니다")             
        elif arg == "바위":
            await ctx.send("저는 가위를 냈습니다. 제가 졌습니다")
        else:
            await ctx.send("저는 가위를 냈습니다. 제가 이겼습니다")
    if bot_rsp == 2:
        if arg == "바위":
            await ctx.send("저도 바위를 냈습니다. 비겼습니다")             
        elif arg == "보":
            await ctx.send("저는 바위를 냈습니다. 제가 졌습니다")
        else:
            await ctx.send("저는 바위를 냈습니다. 제가 이겼습니다")
    if bot_rsp == 3:
        if arg == "보":
            await ctx.send("저도 보를 냈습니다. 비겼습니다")             
        elif arg == "가위":
            await ctx.send("저는 보를 냈습니다. 제가 졌습니다")
        else:
            await ctx.send("저는 보를 냈습니다. 제가 이겼습니다")

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
