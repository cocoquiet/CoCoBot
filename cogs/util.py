import discord
import asyncio
from discord.ext import commands
from discord.utils import get

from config import CoCo_VER

import datetime

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(name="ㅋ케", aliases=["lol", "앜ㅋ"])
    async def lol(self, ctx):
        await ctx.send(ctx.message.author.mention + " : ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")

    @commands.command(name="시간", aliases=["time"])
    async def time(self, ctx):
        now = datetime.datetime.now()

        Meridiem = now.strftime("%p")
        nowHour = now.strftime("%I")
        nowMinute = now.strftime("%M")
        nowSecond = now.strftime("%S")
        
        if(Meridiem == "AM"):
            nowMeridiem = "오전"
        else:
            nowMeridiem = "오후"

        await ctx.send("지금은 " + nowMeridiem + " " + nowHour + "시 " + nowMinute + "분 " + nowSecond + "초 입니다!")

    @commands.command(name="날짜", aliases=["date"])
    async def date(self, ctx):
        now = datetime.datetime.now()

        nowYear = now.strftime("%Y")
        nowMonth = now.strftime("%m")
        nowDay = now.strftime("%d")

        await ctx.send("오늘은 " + nowYear + "년 " + nowMonth + "월 " + nowDay + "일 입니다!")

    @commands.command(name="초대", aliases=["invite"])
    async def invite(self, ctx):
        embed = discord.Embed(title="디스코드봇 초대 링크", description="디코봇들의 초대 링크입니다.", color=0xffffff)
        embed.add_field(name="코코봇 / 재롱부리는 강아지", value="[초대 링크](https://discord.com/oauth2/authorize?client_id=758507966965350420&permissions=0&scope=bot)", inline=False)
        embed.add_field(name="어떤 과학의 음악봇 / 음악봇", value="[초대 링크](https://discord.com/oauth2/authorize?client_id=714140461840728144&permissions=0&scope=bot)", inline=False)
        embed.add_field(name="NAVI / 파싱하는 고양이", value="[초대 링크](https://discord.com/oauth2/authorize?client_id=742281764411670579&permissions=0&scope=bot)", inline=False)
        embed.add_field(name="인절미 빙수 / 설빙", value="[초대 링크](https://discord.com/oauth2/authorize?client_id=796053822371397642&permissions=0&scope=bot)", inline=False)
        embed.add_field(name="루비 / 이모티콘봇", value="[초대 링크](https://discord.com/oauth2/authorize?client_id=796342455762419712&permissions=0&scope=bot)", inline=False)
        embed.add_field(name="노트패드 / 메모장", value="[초대 링크](https://discord.com/oauth2/authorize?client_id=797014035559088159&permissions=0&scope=bot)", inline=False)
        embed.set_footer(text=CoCo_VER)
        
        await ctx.send(embed=embed)

    @commands.command(name="신청", aliases=["request", "re", "ㅅㅊ", "tc"])
    async def request(self, ctx, role : str = None):
        if role == None:
            embed = discord.Embed(title="신청 방법", color=0x000000)
            embed.add_field(name="`/신청 친목`", value="친목방에서 활동할 수 있습니다.", inline=False)
            embed.add_field(name="`/신청 십덕`", value="10_duck방에서 활동할 수 있습니다.", inline=False)

            await ctx.send(embed=embed)

        elif role == "친목":
            intimate = get(ctx.guild.roles, name="Private")
            await ctx.author.add_roles(intimate)
            await ctx.message.add_reaction("✅")

        elif role == "십덕":
            weeb = get(ctx.guild.roles, name="공인 10덕")
            await ctx.author.add_roles(weeb)
            await ctx.message.add_reaction("✅")

def setup(bot):
    bot.add_cog(Ping(bot))