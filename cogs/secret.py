import discord
import asyncio
from discord.ext import commands

noneRomance = False

class Secret(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="시험")
    async def test(self, ctx):
        await ctx.send("설빙님 시험 화이팅!!!!!!!!")

    @commands.command(name="러리")
    async def lery(self, ctx):
        await ctx.send("러리님 대학 합격 축하드려요!!!!!!!!!!!!!!!!!!!!!")

    @commands.command(name="틀니")
    async def falseteeth(self, ctx):
        await ctx.send("딱!딱!")

    @commands.command(name="삽만두", aliases=["sapmando"])
    async def spamando(self, ctx):
        await ctx.send("삽만두님?")
        await ctx.send("남중 다니고 주변에 여사친 없는 모솔이래요")
        await ctx.send("엌ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")

def setup(bot):
    bot.add_cog(Secret(bot))