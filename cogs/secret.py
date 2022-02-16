import discord
import asyncio
from discord.ext import commands
from discord.commands import slash_command

class Secret(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='설빙')
    async def sul(self, ctx):
        """"""
        await ctx.respond('설빙님 화이팅!!!!!!!!')

    @slash_command(name='러리')
    async def lery(self, ctx):
        """"""
        await ctx.respond('러리님 과제 화이팅하세요!!!!!!!!!!')

def setup(bot):
    bot.add_cog(Secret(bot))