import discord
import asyncio
from discord.ext.commands import Cog
from discord.commands import slash_command

from config import CoCoColor, CoCoVER

class Help(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def help(self, ctx, *, args : str = None):
        """명령어들의 종류를 크게 구분해서 보여줄게요."""
        if args == None:
            embed = discord.Embed(title='도움말', description='안녕하세요! 아래의 명령어들을 이용해 도움말을 보세요!', color=CoCoColor)
            embed.add_field(name=f'`/help`', value='명령어들의 종류를 크게 구분해서 보여줄게요.', inline=True)
            embed.add_field(name=f'`/help general`', value='기본적인 명령어들을 보여줄게요.', inline=True)
            embed.add_field(name=f'`/help game`', value='저를 통해 할 수 있는 게임의 명령어들을 보여줄게요.', inline=True)
            embed.add_field(name=f'`/help music`', value='음악과 관련된 명령어들을 보여줄게요.', inline=True)
            embed.add_field(name=f'`/help admin`', value='관리자만 사용 가능한 명령어들을 보여줄게요.', inline=True)
            embed.set_footer(text=CoCoVER)

            await ctx.respond(embed=embed)

        elif (args == 'general') or (args == '일반'):
            embed = discord.Embed(title='기본 명령어', description='안녕하세요? 기본적인 명령어를 알려줄게요!', color=CoCoColor)
            embed.add_field(name=f'`/코코야`', value='기분이 좋으면 착하게, 기분이 나쁘면 신경질적으로 인사할게요.', inline=True)
            embed.add_field(name=f'`/안녕`', value='예쁘게 인사해줄게요.', inline=True)
            embed.add_field(name=f'`/짖어`', value='음...짖을게요.', inline=True)
            embed.add_field(name=f'`/날짜`', value='오늘의 날짜를 알려줄게요.', inline=True)
            embed.add_field(name=f'`/시간`', value='현재 시간을 알려줄게요.', inline=True)
            embed.add_field(name=f'`/ㅋ케`', value='웃기 힘드실때 대신 웃어줄게요.', inline=True)
            embed.add_field(name=f'`/뽑기 <최솟값> <최댓값>`', value='원하는 범위 내의 숫자를 뽑아줄게요.', inline=True)
            embed.add_field(name=f'`/초대`', value='저와 제 친구들을 다른 서버로 초대할 수 있는 링크를 줄게요.', inline=True)
            embed.add_field(name=f'`/신청`', value='특정한 방에서 활동할 수 있게 해줄게요.', inline=True)
            embed.add_field(name=f'`/해제`', value='특정한 방에서 퇴장할 수 있게 해줄게요.', inline=True)
            embed.add_field(name=f'`/깃허브`', value='관리자들의 깃허브 링크를 보여줄게요.', inline=True)
            embed.add_field(name=f'`/ping`', value='제 연결 상태를 보여드릴게요.', inline=True)
            embed.set_footer(text=CoCoVER)

            await ctx.respond(embed=embed)

        elif (args == 'game') or (args == '게임'):
            embed = discord.Embed(title='게임 명령어', description='저를 통해 할 수 있는 게임의 명령어들을 알려줄게요!', color=CoCoColor)
            embed.add_field(name=f'`/가위바위보`', value='가위바위보를 해줄게요.', inline=True)
            embed.add_field(name=f'`/오목 <다른 플레이어>`', value='다른 사람과 오목을 하게 해줄게요.', inline=True)
            embed.set_footer(text=CoCoVER)

            await ctx.respond(embed=embed)

        elif (args == 'music') or (args == '음악'):
            embed = discord.Embed(title='음악 명령어', description='음악과 관련된 명령어를 알려줄게요!', color=CoCoColor)
            embed.add_field(name=f'`/play`', value='원하는 노래를 들려줄게요.', inline=True)
            embed.add_field(name=f'`/stop`', value='듣고 있는 음악을 멈춰줄게요.', inline=True)
            embed.add_field(name=f'`/volume`', value='음악의 볼륨을 조절해줄게요.', inline=True)
            embed.add_field(name=f'`/음악목록`', value='음악 재생목록 링크를 모아서 보여줄게요.', inline=True)
            embed.set_footer(text=CoCoVER)

            await ctx.respond(embed=embed)

        elif (args == 'admin') or (args == '어드민') or (args == '관리자'):
            embed = discord.Embed(title='관리자 명령어', description='관리자만 사용 가능한 명령어를 알려줄게요!', color=CoCoColor)
            embed.add_field(name=f'`/kick <추방할 유저>`', value='문제가 있는 사람들을 추방시켜줄게요.', inline=True)
            embed.add_field(name=f'`/ban <차단할 유저>`', value='마음에 들지 않은 사람들을 차단시켜 줄게요.', inline=True)
            embed.add_field(name=f'`/mute <뮤트할 유저>`', value='시끄러운 사람들을 조용히 있게 해줄게요.', inline=True)
            embed.add_field(name=f'`/unmute <언뮤트할 유저>`', value='조용해진 사람들을 말할 수 있게 해줄게요.', inline=True)
            embed.add_field(name=f'`/감금 <감금시킬 유저>`', value='중한 죄를 저지른 사람들을 뒤주에 보내줄게요.', inline=True)
            embed.add_field(name=f'`/이동 <음성 채널> <이동시킬 유저들>`', value='원하는 음성 채널로 사람들을 보내줄게요.', inline=True)
            embed.add_field(name=f'`/잠수함 <잠수시킬 유저>`', value='조용해보이는 사람들을 잠수함에 보내줄게요.', inline=True)
            embed.add_field(name=f'`/청소 <삭제할 개수>`', value='많은 메세지를 한번에 지워줄게요.\n개수를 입력하지 않으면 10개를, -1을 입력하면 다 지워줄게요.', inline=True)
            embed.add_field(name=f'`/초기화`', value='채팅방을 맨 처음의 모습으로 돌려줄게요.', inline=True)
            embed.add_field(name=f'`/로그`', value='이 서버의 감사 로그를 보여줄게요.', inline=True)
            embed.add_field(name=f'`/고코위`', value='모든 어드민들을 불러줄게요.', inline=True)
            embed.set_footer(text=CoCoVER)

            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))