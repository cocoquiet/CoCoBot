import discord
import asyncio
from discord.ext import commands

import random

player = None       # 가위바위보 플레이어
bot_rsp = None      # 봇의 선택(랜덤, 1:가위  2:바위  3:보)

class RSP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='가위바위보를 해줄게요.')
    async def rsp(self, ctx):
        global bot_rsp
        global player

        await ctx.respond('가위바위보를 시작합니다.')
        await ctx.respond(f'/가위, /바위, /보 중 하나를 내주세요.')
    
        player = ctx.author
        bot_rsp = random.randint(1, 3)

    @commands.slash_command(description='가위를 내요.')
    async def rsp_scissor(self, ctx):
        global bot_rsp
        global player
        
        if player == ctx.author:
            if  bot_rsp== 1:
                await ctx.respond('저도 가위를 냈습니다. 비겼습니다')
            elif bot_rsp == 2:
                await ctx.respond('저는 바위를 냈습니다. 제가 이겼습니다')
            elif bot_rsp == 3:
                await ctx.respond('저는 보를 냈습니다. 제가 졌습니다')
        player = None

    @commands.slash_command(description='바위를 내요.')
    async def rsp_rock(self, ctx):
        global bot_rsp
        global player
        
        if player == ctx.author:
            if bot_rsp == 1:
                await ctx.respond('저는 가위를 냈습니다. 제가 졌습니다')
            elif bot_rsp == 2:
                await ctx.respond('저도 바위를 냈습니다. 비겼습니다')
            elif bot_rsp == 3:
                await ctx.respond('저는 보를 냈습니다. 제가 이겼습니다')
        player = None

    @commands.slash_command(description='보를 내요.')
    async def rsp_paper(self, ctx):
        global bot_rsp
        global player
        
        if player == ctx.author:
            if bot_rsp == 1:
                await ctx.respond('저는 가위를 냈습니다. 제가 이겼습니다')
            elif bot_rsp == 2:
                await ctx.respond('저는 바위를 냈습니다. 제가 졌습니다')
            elif bot_rsp == 3:
                await ctx.respond('저도 보를 냈습니다. 비겼습니다')
        player = None

def setup(bot):
    bot.add_cog(RSP(bot))