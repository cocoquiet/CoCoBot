import discord
import asyncio
from discord.ext import commands

class Secret(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="시험")
    async def test(self, ctx):
        await ctx.send("설빙님 시험 화이팅!!!!!!!!")

    @commands.command(name="러리")
    async def lery(self, ctx):
        await ctx.send("러리님 대학 합격 축하드려요!!!!!!!!!!!!!!!!!!!!!")

    @commands.command(name="자스고")
    async def jasgo(self, ctx):
        embed = discord.Embed(title="자스고", description=":AMGO_angry:  :AMGO_despair:  :AMGO_peaceful:  :AMGO_sad: ", color=0xffffff)
        embed.set_footer(text="코코#1174 | V1.5")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Secret(bot))