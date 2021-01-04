import discord
import asyncio
from discord.ext import commands
from discord.utils import get

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick")
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, user : discord.Member, *, reason=None):
        await user.kick(reason=reason)

    @commands.command(name="ban")
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, user : discord.Member, *, reason=None):
        await user.ban(reason=reason)

    @commands.command(name="청소")
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount):
        await ctx.channel.purge(limit=int(amount) + 1)

    @commands.command(name="고코위")
    @commands.has_permissions(administrator=True)
    async def CCC(self, ctx):
        admin = get(ctx.guild.roles, name="Admin")
        await ctx.send(ctx.message.author.mention + "님이 불렀습니다 : " + str(admin.mention))

def setup(bot):
    bot.add_cog(Admin(bot))