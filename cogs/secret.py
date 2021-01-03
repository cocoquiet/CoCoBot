import discord
import asyncio
from discord.ext import commands

class Secret(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="시험")
    async def test(self, ctx):
        await ctx.send("설빙 시험 화이팅!!!!!!!!")

    @commands.command(name="신년")
    async def test(self, ctx):
        await ctx.send("다들 새해 복 많이 받으세요!!!!!")

def setup(bot):
    bot.add_cog(Secret(bot))