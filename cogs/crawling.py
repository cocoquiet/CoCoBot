import discord
import asyncio
from discord.ext import commands
from config import CoCo_VER

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pprint import pprint

class Crawling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="실검")
    async def searchterm(self, ctx):
        json = requests.get("https://www.naver.com/srchrank?frm=main").json()
        ranks = json.get("data")
        
        embed = discord.Embed(title="실시간 검색어", description="네이버 실시간 검색어 1~20위입니다.", color=0x000000)
        
        i = 1
        for item in ranks:
            keyword = item.get("keyword")
            link = keyword.replace(" ", "+")
            embed.add_field(name=str(i) + "위", value="[" + keyword + "](https://search.naver.com/search.naver?query=" + link + ")", inline=False)
            i += 1
        embed.set_footer(text=CoCo_VER)

        await ctx.send(embed=embed)

    @commands.command(name="날씨", aliases=["weather"])
    async def weather(self, ctx, *, locate):
        location = str(locate).replace(" ", "+")

        html = requests.get("https://search.naver.com/search.naver?query=날씨" + str(location))
        soup = BeautifulSoup(html.text, 'html.parser')
        weather_box = soup.find('div', {'class': 'weather_box'})

        find_address = weather_box.find('span', {'class':'btn_select'}).text
        find_currenttemp = weather_box.find('span',{'class': 'todaytemp'}).text
        dd = weather_box.findAll('dd')
        find_dust = dd[0].find('span', {'class':'num'}).text
        find_ultra_dust = dd[1].find('span', {'class':'num'}).text

        embed=discord.Embed(title="날씨", description="현재의 날씨 정보를 알려드립니다.", color=0xffffff)
        embed.add_field(name="검색 위치", value=find_address, inline=False)
        embed.add_field(name="현재 온도", value=find_currenttemp + "℃", inline=False)
        embed.add_field(name="현재 미세먼지", value=find_dust, inline=False)
        embed.add_field(name="현재 초미세먼지", value=find_ultra_dust, inline=False)
        embed.set_footer(text=CoCo_VER)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Crawling(bot))