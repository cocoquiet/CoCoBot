import discord
import asyncio
from discord.ext import commands

class Secret(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="시험")
    async def test(self, ctx):
        await ctx.send("설빙님 시험 화이팅!!!!!!!!")

    @commands.command(name="자스고")
    @commands.has_permissions(administrator=True)
    async def jasgo(self, ctx):
        member = "@CoCoTestBot#7796"
        await member.kick()

def setup(bot):
    bot.add_cog(Secret(bot))