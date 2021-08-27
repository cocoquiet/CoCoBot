import discord
import asyncio
from discord.ext import commands

from config import CoCoColor
from config import CoCoVER

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping', aliases=['핑'])
    async def ping(self, ctx):
        latency = self.bot.latency
        
        embed = discord.Embed(title='Ping!', description=':ping_pong: Pong! ' + '**' + str(round(latency * 1000)) + ' ms' + '**', color=CoCoColor)
        embed.set_footer(text=CoCoVER)
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Ping(bot))