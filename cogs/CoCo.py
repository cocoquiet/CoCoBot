import discord
import asyncio
from discord.ext import commands

import random

CoCoResponse = ['네?', '뭐', '왜', 'ㅇ', 'ㅇㅇ?', '누가 불렀니', '아 왜 불러ㅡㅡ']    # 코코 응답 목록

class CoCo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='기분이 좋으면 착하게, 기분이 나쁘면 신경질적으로 인사할게요.')
    async def hey(self, ctx):
        global CoCoResponse

        await ctx.respond(random.choice(CoCoResponse))

    @commands.slash_command(description='예쁘게 인사해줄게요.')
    async def hello(self, ctx):
        await ctx.respond('안녕하세요 ' + ctx.message.author.mention + ' 님!')

    @commands.slash_command(description='음...짖을게요.')
    async def bark(self, ctx):
        CoCoBark = ['크르릉...', '뀨웅?', '왈왈!', '멍멍!']
        
        await ctx.respond(CoCoBark[random.randint(0, 3)])

def setup(bot):
    bot.add_cog(CoCo(bot))