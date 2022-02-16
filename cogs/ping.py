from pydoc import describe
import discord
import asyncio
from discord.ext import commands

from config import CoCoColor
from config import CoCoVER

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def ping(self, ctx):
        """제 연결 상태를 보여드릴게요."""
        latency = self.bot.latency
        
        embed = discord.Embed(title='Ping!', description=':ping_pong: Pong! ' + '**' + str(round(latency * 1000)) + ' ms' + '**', color=CoCoColor)
        embed.set_footer(text=CoCoVER)
        
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Ping(bot))