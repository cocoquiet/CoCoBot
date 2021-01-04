import discord
import asyncio
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx, *, args : str = None):
        if args == None:
            embed = discord.Embed(title="도움말", description="안녕하세요! 아래의 명령어들을 이용해 도움말을 보세요!", color=0xffffff)
            embed.add_field(name="```/help```", value="명령어들의 종류를 크게 구분해서 보여줄게요.", inline=True)
            embed.add_field(name="```/help general```", value="기본적인 명령어들을 보여줄게요.", inline=True)
            embed.add_field(name="```/help music```", value="음악과 관련된 명령어들을 보여줄게요.", inline=True)
            embed.add_field(name="```/help admin```", value="관리자만 상용 가능한 명령어들을 보여줄게요.", inline=True)
            embed.set_footer(text="코코#1174 | V1.5")

            await ctx.send(embed=embed)

        elif args == "general":
            embed = discord.Embed(title="기본 명령어", description="기본적인 명령어를 알려줄게요!", color=0xffffff)
            embed.add_field(name="```/안녕```", value="예쁘게 인사해줄게요.", inline=True)
            embed.add_field(name="```/코코야```", value="기분이 좋으면 착하게, 기분이 나쁘면 신경질적으로 인사할거에요.", inline=True)
            embed.add_field(name="```/짖어```", value="음...짖을게요.", inline=True)
            embed.add_field(name="```/가위바위보```", value="가위바위보를 해줄게요.", inline=True)
            embed.add_field(name="```/날짜```", value="오늘의 날짜를 알려줄게요.", inline=True)
            embed.add_field(name="```/시간```", value="현재 시간을 알려줄게요.", inline=True)
            embed.add_field(name="```/ㅋ케```", value="웃기 힘드실때 대신 웃어줄게요.", inline=True)
            embed.add_field(name="```/초대```", value="저와 제 친구들을 다른 서버로 초대할 수 있는 링크를 줄게요.", inline=True)
            embed.add_field(name="```/실검```", value="네이버의 실시간 검색어 순위를 보여줄게요.", inline=True)
            embed.add_field(name="```/날씨 <지역>```", value="입력하신 지역의 날씨 상태를 알려줄게요.", inline=True)
            embed.add_field(name="```/깃허브```", value="관리자들의 깃허브 링크를 보여줄게요.", inline=True)
            embed.add_field(name="```/ping```", value="제 연결 상태를 보여드릴게요.", inline=True)
            embed.set_footer(text="코코#1174 | V1.5")

            await ctx.send(embed=embed)

        elif args == "music":
            embed = discord.Embed(title="음악 명령어", description="음악과 관련된 명령어를 알려줄게요!", color=0xffffff)
            embed.add_field(name="```/음악목록```", value="음악 재생목록 링크를 모아서 보여줄게요.", inline=True)
            embed.set_footer(text="코코#1174 | V1.5")

            await ctx.send(embed=embed)

        elif args == "admin":
            embed = discord.Embed(title="관리자 명령어", description="관리자만 사용 가능한 명령어를 알려줄게요!", color=0xffffff)
            embed.add_field(name="```/kick <추방할 유저> <추방 사유>```", value="문제가 있는 사람들을 추방시켜줄게요.", inline=True)
            embed.add_field(name="```/ban <차단할 유저> <차단 사유>```", value="마음에 들지 않은 사람들을 차단시켜 줄게요.", inline=True)
            embed.add_field(name="```/청소 <삭제할 개수>```", value="많은 메세지를 한번에 지워줄게요.", inline=True)
            embed.add_field(name="```/고코위```", value="모든 어드민들을 불러줄게요.", inline=True)
            embed.set_footer(text="코코#1174 | V1.5")

            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))