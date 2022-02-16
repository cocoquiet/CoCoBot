import discord
import asyncio
from discord.ext import commands
from discord.commands import slash_command

from config import CoCoColor
from config import CoCoVER

class Github(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def github(self, ctx):
        """관리자들의 깃허브 링크를 보여줄게요."""
        embed = discord.Embed(title='관리자 깃허브 링크 목록', description='깃허브 링크 모음입니다.', color=CoCoColor)
        embed.add_field(name='`코양이 위원장`', value='https://github.com/easycastle', inline=False)
        embed.add_field(name='`양사`', value='https://github.com/sat0317', inline=False)
        embed.add_field(name='`러리`', value='https://github.com/Coalery', inline=False)
        embed.add_field(name='`Cpp고수`', value='https://github.com/cpprhtn', inline=False)
        embed.add_field(name='`깃고`', value='https://github.com/ajb3296', inline=False)
        embed.add_field(name='`루`', value='https://github.com/Lu175', inline=False)
        embed.add_field(name='`뽀로로`', value='https://github.com/paxbun', inline=False)
        embed.add_field(name='`녹색치킨`', value='https://github.com/IceJack', inline=False)
        embed.set_footer(text=CoCoVER)

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Github(bot))