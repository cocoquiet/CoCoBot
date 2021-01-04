import discord
import asyncio
from discord.ext import commands

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
        embed=discord.Embed(title="디스코드봇 초대 링크", description="디코봇들의 초대 링크입니다.", color=0xffffff)
        embed.add_field(name="코코봇", value="[초대 링크](https://discord.com/oauth2/authorize?client_id=758507966965350420&permissions=8&scope=bot)", inline=False)
        embed.add_field(name="어떤 과학의 음악봇", value="[초대 링크](https://discord.com/oauth2/authorize?client_id=714140461840728144&permissions=8&scope=bot)", inline=False)
        embed.add_field(name="NAVI", value="[초대 링크](https://discord.com/oauth2/authorize?client_id=742281764411670579&permissions=8&scope=bot)", inline=False)
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Ping(bot))