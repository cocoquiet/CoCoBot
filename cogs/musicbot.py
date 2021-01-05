import discord
import asyncio
from discord.ext import commands

class Musicbot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="connect", aliases=["c", "ㅊ"])
    async def connect(self, ctx):
        user = ctx.message.author
        channel = user.voice.channel
        
        await channel.connect()

    @commands.command(name="disconnect", aliases=["dc", "ㅇㅊ"])
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

def setup(bot):
    bot.add_cog(Musicbot(bot))