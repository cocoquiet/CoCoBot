import discord
import asyncio
from discord.ext import commands

noneRomance = False

class Secret(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="시험")
    async def test(self, ctx):
        await ctx.send("설빙님 화이팅!!!!!!!!")

    @commands.command(name="러리")
    async def lery(self, ctx):
        await ctx.send("러리님 과제 화이팅하세요!!!!!!!!!!")

def setup(bot):
    bot.add_cog(Secret(bot))