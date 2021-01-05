import discord
import asyncio
from discord.ext import commands
from discord.utils import get

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="connect", aliases=["c", "ㅊ"])
    async def connect(self, ctx):
        channel = ctx.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

    @commands.command(name="disconnect", aliases=["dc", "ㅇㅊ"])
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command(name="음악목록", aliases=["playlist"])
    async def playlist(self, ctx):
        embed = discord.Embed(title="코양이 유튜브 재생목록", description="유튜브 재생목록 모음입니다.", color=0xffffff)
        embed.add_field(name="`코양이 노동요`", value="https://www.youtube.com/playlist?list=PLylf8Ved3tAFtRQRTgx78KcG2NPdnyzyP", inline=False)
        embed.add_field(name="`코양이 재즈`", value="https://www.youtube.com/playlist?list=PLylf8Ved3tAEGE_f0734AmuQyFWcY0r4T", inline=False)
        embed.add_field(name="`코양이 캐롤`", value="https://www.youtube.com/playlist?list=PLylf8Ved3tAFM2-5BpAhUJzQKjXd0i_Ta", inline=False)
        embed.add_field(name="`코양이 힙합`", value="https://www.youtube.com/playlist?list=PLylf8Ved3tAHdLCjFZJJsLAHkjj8yX6J8", inline=False)
        embed.add_field(name="`코양이 팝`", value="https://youtube.com/playlist?list=PLylf8Ved3tAF6Xhb_63e9tv3TBfmKB0wE", inline=False)
        embed.add_field(name="`코양이 올드팝`", value="https://www.youtube.com/playlist?list=PLylf8Ved3tAH2O8mPPgtHTX8Wx_bbkjDf", inline=False)
        embed.add_field(name="`루 뮤직 리스트`", value="https://youtube.com/playlist?list=PLVW_htI5V49iz9Z38iaKOoS8JByghA0cb", inline=False)
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Music(bot))