import discord
import asyncio
from discord.ext import commands, tasks

import random
import datetime

import os

bot = commands.Bot(command_prefix="/")

player = None
bot_rsp = None

bot.remove_command("help")

@bot.event
async def on_ready():
    print("코코 대기 중")
    print(bot.user.name)
    print(bot.user.id)
    print("=============")

    now = datetime.datetime.now()
    nowTime = now.strftime("%H")

    await bot.change_presence(status=discord.Status.online, activity=discord.Game("주인놈이랑 코딩"))

@bot.command(name="도움말")
async def help(ctx):
    embed = discord.Embed(title="도움말", description="안녕하세요! 사용법을 알려드릴게요!", color = 0x00ff00)
    embed.add_field(name="```/안녕```", value="예쁘게 인사해줄게요.", inline=True)
    embed.add_field(name="```/코코야```", value="기분이 좋으면 착하게, 기분이 나쁘면 신경질적으로 인사할거에요.", inline=True)
    embed.add_field(name="```/가위바위보```", value="가위바위보를 해줄게요.", inline=True)
    embed.add_field(name="```/날짜```", value="오늘의 날짜를 알려드릴게요.", inline=True)
    embed.add_field(name="```/시간```", value="현재 시간을 알려드릴게요.", inline=True)
    embed.add_field(name="```/ㅋ케```", value="웃기 힘드실때 대신 웃어드릴게요.", inline=True)
    embed.add_field(name="```/음악목록```", value="음악 재생목록 링크를 모아서 보여줘요.", inline=True)
    embed.add_field(name="```/ping```", value="제 연결 상태를 보여드릴게요.", inline=True)
    embed.add_field(name="```/청소```", value="많은 메세지를 한번에 지워드줄게요.", inline=True)
    embed.set_footer(text="앞으로 여러가지를 추가할거에요!!")
    
    await ctx.send(embed=embed)

@bot.command(name="안녕")
async def hello(ctx):
    await ctx.send("안녕하세요 %s 님!" %(ctx.author))

@bot.command(name="코코야")
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

@bot.command(name="가위바위보")
async def RSP(ctx):
    global bot_rsp
   
    global player
    await ctx.send("가위바위보를 시작합니다.")
    await ctx.send("가위, 바위, 보 중 하나를 내주세요.")
   
    player = ctx.author
    bot_rsp = random.randint(1, 3) # 1:가위  2:바위  3:보

@bot.command(name="가위")
async def rsp_scissors(ctx):
    global bot_rsp
    global player
    
    if player == ctx.author:
        if  bot_rsp== 1:
            await ctx.send("저도 가위를 냈습니다. 비겼습니다")
        elif bot_rsp == 2:
            await ctx.send("저는 바위를 냈습니다. 제가 이겼습니다")
        elif bot_rsp == 3:
            await ctx.send("저는 보를 냈습니다. 제가 졌습니다")
    player = None

@bot.command(name="바위")
async def rsp_rock(ctx):
    global bot_rsp
    global player
    
    if player == ctx.author:
        if bot_rsp == 1:
            await ctx.send("저는 가위를 냈습니다. 제가 졌습니다")
        elif bot_rsp == 2:
            await ctx.send("저도 바위를 냈습니다. 비겼습니다")
        elif bot_rsp == 3:
            await ctx.send("저는 보를 냈습니다. 제가 이겼습니다")
    player = None

@bot.command(name="보")
async def rsp_rock(ctx):
    global bot_rsp
    global player
    
    if player == ctx.author:
        if bot_rsp == 1:
            await ctx.send("저는 가위를 냈습니다. 제가 이겼습니다")
        elif bot_rsp == 2:
            await ctx.send("저는 바위를 냈습니다. 제가 졌습니다")
        elif bot_rsp == 3:
            await ctx.send("저도 보를 냈습니다. 비겼습니다")
    player = None
    
@bot.command(name="ping")
async def ping(ctx):
    latency = bot.latency
    
    embed = discord.Embed(title="Ping!", description=":ping_pong: Pong! " + "**" + str(round(latency * 1000)) + " ms" + "**", color=0x00ff00)
    embed.set_footer(text="코코#1174 | V1.0")
    
    await ctx.send(embed=embed)

@bot.command(name="ㅋ케")
async def lol(ctx):
    await ctx.send("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")

@bot.command(name="시간")
async def date(ctx):
    now = datetime.datetime.now()

    Meridiem = now.strftime("%p")
    nowHour = now.strftime("%I")
    nowMinute = now.strftime("%M")
    nowSecond = now.strftime("%S")
    
    if(Meridiem == "AM"):
        nowMeridiem = "오전"
    else:
        nowMeridiem = "오후"

    await ctx.send("지금은 " + nowMeridiem + " " + nowHour + "시 " + nowMinute + "분 " + nowSecond + "초 입니다!")

@bot.command(name="날짜")
async def date(ctx):
    now = datetime.datetime.now()

    nowYear = now.strftime("%Y")
    nowMonth = now.strftime("%m")
    nowDay = now.strftime("%d")

    await ctx.send("오늘은 " + nowYear + "년 " + nowMonth + "월 " + nowDay + "일 입니다!")

@bot.command(name="음악목록")
async def playlist(ctx):
    embed = discord.Embed(title="코양이 유튜브 재생목록", description="유튜브 재생목록 모음입니다.", color = 0x00ff00)
    embed.add_field(name="```코양이 노동요```", value="https://www.youtube.com/playlist?list=PLylf8Ved3tAFtRQRTgx78KcG2NPdnyzyP", inline=False)
    embed.add_field(name="```코양이 재즈 노동요```", value="https://www.youtube.com/playlist?list=PLylf8Ved3tAEGE_f0734AmuQyFWcY0r4T", inline=False)
    embed.add_field(name="```코양이 캐롤```", value="https://www.youtube.com/playlist?list=PLylf8Ved3tAFM2-5BpAhUJzQKjXd0i_Ta", inline=False)
    
    await ctx.send(embed=embed)
    
@bot.command(name="청소")
@commands.has_permissions(administrator=True)
async def clear(ctx, amount):
    await ctx.channel.purge(limit=int(amount) + 1)

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
