import discord
import asyncio
from discord.ext import commands, tasks

import random

import os

is_playing = None
player = None

class CoCo(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix = '!!')
        self.remove_command("help")

    async def on_ready(self):
        print('코코 대기 중')
        print(bot.user.name)
        print(bot.user.id)
        print('=============')
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("주인놈이랑 코딩"))

    async def on_message(self, message):
        content = message.content
        guild = message.guild
        author = message.author
        channel = message.channel

        global is_playing
        global player

        if (content == "!!안녕"):
            await channel.send('안녕하세요 %s 님!' %(author))

        if (content == "!!코코야"):
            CoCoResponse = random.randint(1, 4)
            if CoCoResponse == 1:
                await channel.send("네?")
            elif CoCoResponse == 2:
                await channel.send("뭐")
            elif CoCoResponse == 3:
                await channel.send("아 왜 불러ㅡㅡ")
            elif CoCoResponse == 4:
                await channel.send("멍멍!")

        if (content == "!!가위바위보"):
            await channel.send("가위바위보 게임을 시작합니다. 가위, 바위, 보 중 하나를 내주세요.")
            is_playing = True
            player = author

        if((is_playing == True) and (player == author) and ((content == "!!가위") or (content == "!!바위") or (content == "!!보"))):
            bot_rsp = random.randint(1, 3) # 1:가위  2:바위  3:보

            if bot_rsp == 1:
                if content == "!!가위":
                    await channel.send("저도 가위를 냈습니다. 비겼습니다")             
                elif content == "!!바위":
                    await channel.send("저는 가위를 냈습니다. 제가 졌습니다")
                else:
                    await channel.send("저는 가위를 냈습니다. 제가 이겼습니다")
            if bot_rsp == 2:
                if content == "!!바위":
                    await channel.send("저도 바위를 냈습니다. 비겼습니다")             
                elif content == "!!보":
                    await channel.send("저는 바위를 냈습니다. 제가 졌습니다")
                else:
                    await channel.send("저는 바위를 냈습니다. 제가 이겼습니다")
            if bot_rsp == 3:
                if content == "!!보":
                    await channel.send("저도 보를 냈습니다. 비겼습니다")             
                elif content == "!!가위":
                    await channel.send("저는 보를 냈습니다. 제가 졌습니다")
                else:
                    await channel.send("저는 보를 냈습니다. 제가 이겼습니다")
            is_playing = False
            player = None

bot = CoCo()

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
