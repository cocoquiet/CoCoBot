import discord
import asyncio
from discord.ext import commands

noneRomance = False

class Secret(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="시험")
    async def test(self, ctx):
        await ctx.send("설빙님 시험 화이팅!!!!!!!!")

    @commands.command(name="러리")
    async def lery(self, ctx):
        await ctx.send("러리님 대학 합격 축하드려요!!!!!!!!!!!!!!!!!!!!!")

    @commands.command(name="틀니")
    async def falseteeth(self, ctx):
        await ctx.send("딱!딱!")

    @commands.command(name="삽만두", aliases=["sapmando"])
    async def spamando(self, ctx):
        await ctx.send("삽만두님?")
        await ctx.send("남중 다니고 주변에 여사친 없는 모솔이래요")
        await ctx.send("엌ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")

    @commands.command(name="모솔")
    @commands.has_permissions(administrator=True)
    async def noneRomance(self, ctx):
        global noneRomance

        noneRomance = True

    @commands.Cog.listener()
    async def on_message(self, message):
        global noneRomance
        if (message.author.id == 702396818167824435) and (noneRomance == True):
            await message.channel.send("으응 모솔ㅋㅋㅋㅋㅋㅋㅋ")


def setup(bot):
    bot.add_cog(Secret(bot))