import discord
import asyncio
from discord.ext import commands

from discord.utils import get

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick", aliases=["강퇴", "추방"])
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, user : discord.Member, *, reason=None):
        await user.kick(reason=reason)

    @commands.command(name="ban", aliases=["차단"])
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, user : discord.Member, *, reason=None):
        await user.ban(reason=reason)

    @commands.command(name="청소", aliases=["clean", "clear", "purge"])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount : int = None, name : str = None):
        if amount == None:
            await ctx.channel.purge(limit=11)
        elif amount == -1:
            if name == ctx.channel.mention:
                position = ctx.channel.position
                newChannel = await ctx.channel.clone()
                await ctx.channel.delete()
                await newChannel.edit(position=position)
            elif name == None:
                await ctx.send("사고 대비를 위해 채널을 멘션해주세요")
        else:
            await ctx.channel.purge(limit=amount + 1)

    @commands.command(name="초기화", aliases=["reset", "리셋", "delall"])
    @commands.has_permissions(administrator=True)
    async def reset(self, ctx, name : str = None):
        if name == ctx.channel.mention:
            position = ctx.channel.position
            newChannel = await ctx.channel.clone()
            await ctx.channel.delete()
            await newChannel.edit(position=position)
        elif name == None:
            await ctx.send("사고 대비를 위해 채널을 멘션해주세요")
    
    @commands.command(name="고코위", aliases=["관리자"])
    @commands.has_permissions(administrator=True)
    async def CCC(self, ctx):
        admin = get(ctx.guild.roles, name="Admin")
        await ctx.send(ctx.message.author.mention + "님이 불렀습니다 : " + str(admin.mention))
        
def setup(bot):
    bot.add_cog(Admin(bot))