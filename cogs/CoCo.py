import discord
import asyncio
from discord.ext.commands import Cog
from discord.commands import slash_command

import random

CoCoResponse = ['네?', '뭐', '왜', 'ㅇ', 'ㅇㅇ?', '누가 불렀니', '아 왜 불러ㅡㅡ']    # 코코 응답 목록

class CoCo(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def hey(self, ctx):
        """기분이 좋으면 착하게, 기분이 나쁘면 신경질적으로 인사할게요."""
        global CoCoResponse

        await ctx.respond(random.choice(CoCoResponse))

    @slash_command()
    async def hello(self, ctx):
        """예쁘게 인사해줄게요."""
        await ctx.respond('안녕하세요 ' + ctx.author.mention + ' 님!')

    @slash_command()
    async def bark(self, ctx):
        """음...짖을게요."""
        CoCoBark = ['크르릉...', '뀨웅?', '왈왈!', '멍멍!']
        
        await ctx.respond(CoCoBark[random.randint(0, 3)])

def setup(bot):
    bot.add_cog(CoCo(bot))