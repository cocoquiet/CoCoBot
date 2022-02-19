import discord
import asyncio
from discord.ext.commands import Cog
from discord.commands import slash_command
from discord.utils import get

from config import CoCoColor, CoCoVER

import datetime
import random

class Util(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def date(self, ctx):
        """오늘의 날짜를 알려줄게요."""
        
        now = datetime.datetime.now()

        nowYear = now.strftime('%Y')
        nowMonth = now.strftime('%m')
        nowDay = now.strftime('%d')

        await ctx.respond('오늘은 ' + nowYear + '년 ' + nowMonth + '월 ' + nowDay + '일 입니다!')

    @slash_command()
    async def time(self, ctx):
        """현재 시간을 알려줄게요."""
        
        now = datetime.datetime.now()

        Meridiem = now.strftime('%p')
        nowHour = now.strftime('%I')
        nowMinute = now.strftime('%M')
        nowSecond = now.strftime('%S')
        
        if(Meridiem == 'AM'):
            nowMeridiem = '오전'
        else:
            nowMeridiem = '오후'

        await ctx.respond('지금은 ' + nowMeridiem + ' ' + nowHour + '시 ' + nowMinute + '분 ' + nowSecond + '초 입니다!')

    @slash_command()
    async def lol(self, ctx):
        """웃기 힘드실때 대신 웃어줄게요."""
        
        await ctx.respond(ctx.author.mention + ' : ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ')

    @slash_command()
    async def random(self, ctx, min: Option(int, '최솟값', required=True), max: Option(int, '최댓값', required=True)):
        """원하는 범위 내의 숫자를 뽑아줄게요."""
        
        await ctx.respond(random.randrange(min, max+1))

    @slash_command()
    async def invite(self, ctx):
        """저와 제 친구들을 다른 서버로 초대할 수 있는 링크를 줄게요."""
        
        embed = discord.Embed(title='디스코드봇 초대 링크', description='디코봇들의 초대 링크입니다.', color=CoCoColor)
        embed.add_field(name='코코봇 / 재롱부리는 강아지', value='[초대 링크](https://discord.com/oauth2/authorize?client_id=758507966965350420&permissions=0&scope=bot%20applications.commands)', inline=False)
        embed.add_field(name='어떤 과학의 음악봇 / 음악봇', value='[초대 링크](https://discord.com/oauth2/authorize?client_id=714140461840728144&permissions=0&scope=bot%20applications.commands)', inline=False)
        embed.add_field(name='인절미 빙수 / 설빙', value='[초대 링크](https://discord.com/oauth2/authorize?client_id=796053822371397642&permissions=0&scope=bot%20applications.commands)', inline=False)
        embed.add_field(name='루비 / 이모티콘봇', value='[초대 링크](https://discord.com/oauth2/authorize?client_id=796342455762419712&permissions=0&scope=bot%20applications.commands)', inline=False)
        embed.set_footer(text=CoCoVER)
        
        await ctx.respond(embed=embed)

    @slash_command()
    async def request(self, ctx, role : str = None):
        """특정한 방에서 활동할 수 있게 해줄게요."""
        
        if role == None:
            if ctx.channel.id == 737283234156511242:
                embed = discord.Embed(color=CoCoColor)
                embed.add_field(name=f'`친목`', value='친목방에서 활동할 수 있습니다.', inline=False)
                embed.add_field(name=f'`십덕`', value='10_duck방에서 활동할 수 있습니다.', inline=False)
                embed.add_field(name=f'`게임`', value='게임방에서 활동할 수 있습니다.', inline=False)

                await ctx.respond(embed=embed)
            elif ctx.channel.id == 811584272825712692:
                embed = discord.Embed(color=CoCoColor)
                embed.add_field(name=f'`견적`', value='견적방에서 활동할 수 있습니다.', inline=False)
                # embed.add_field(name=f'`/신청 전쟁`', value='견적-전쟁터 방에서 활동할 수 있습니다.', inline=False)

                await ctx.respond(embed=embed)

        elif (ctx.channel.id == 737283234156511242) and (role == '친목'):
            intimate = get(ctx.guild.roles, name='친목')
            await ctx.author.add_roles(intimate)
            await ctx.message.add_reaction('✅')

        elif (ctx.channel.id == 737283234156511242) and (role == '십덕'):
            weeb = get(ctx.guild.roles, name='10덕')
            await ctx.author.add_roles(weeb)
            await ctx.message.add_reaction('✅')

        elif (ctx.channel.id == 737283234156511242) and (role == '게임'):
            nerd = get(ctx.guild.roles, name='게임')
            await ctx.author.add_roles(nerd)
            await ctx.message.add_reaction('✅')
            
        elif (ctx.channel.id == 811584272825712692) and (role == '견적'):
            PC = get(ctx.guild.roles, name='견적')
            await ctx.author.add_roles(PC)
            await ctx.message.add_reaction('✅')

        elif (ctx.channel.id == 811584272825712692) and ((role == '전쟁') or (role == '전쟁터')):
            battleField = ctx.guild.get_channel(826116146054168656)

            fighter = discord.PermissionOverwrite()
            fighter.read_messages = True
            fighter.send_messages = False
            
            await battleField.set_permissions(ctx.author, overwrite=fighter)
            await ctx.message.add_reaction('✅')
            
            await battleField.send('전쟁터에 오신 것을 환영합니다.')

        else:
            await ctx.respond('번지수 잘못 찾아왔다ㅡㅡ')

    @slash_command()
    async def dismiss(self, ctx, role : str = None):
        """특정한 방에서 퇴장할 수 있게 해줄게요."""
        
        if role == None:
            if ctx.channel.id == 737283234156511242:
                embed = discord.Embed(color=CoCoColor)
                embed.add_field(name=f'`친목`', value='친목방에서 퇴장할 수 있습니다.', inline=False)
                embed.add_field(name=f'`십덕`', value='10_duck방에서 퇴장할 수 있습니다.', inline=False)
                embed.add_field(name=f'`게임`', value='게임방에서 퇴장할 수 있습니다.', inline=False)

                await ctx.respond(embed=embed)
            elif ctx.channel.id == 811584272825712692:
                embed = discord.Embed(color=CoCoColor)
                embed.add_field(name=f'`견적`', value='견적방에서 퇴장할 수 있습니다.', inline=False)
                # embed.add_field(name=f'`/해제 전쟁`', value='견적-전쟁터 방에서 퇴장할 수 있습니다.', inline=False)

                await ctx.respond(embed=embed)

        elif (ctx.channel.id == 737283234156511242) and (role == '친목'):
            intimate = get(ctx.guild.roles, name='친목')
            await ctx.author.remove_roles(intimate)
            await ctx.message.add_reaction('👍')

        elif (ctx.channel.id == 737283234156511242) and (role == '십덕'):
            weeb = get(ctx.guild.roles, name='10덕')
            await ctx.author.remove_roles(weeb)
            await ctx.message.add_reaction('👍')
            
        elif (ctx.channel.id == 737283234156511242) and (role == '게임'):
            nerd = get(ctx.guild.roles, name='게임')
            await ctx.author.remove_roles(nerd)
            await ctx.message.add_reaction('👍')
            
        elif (ctx.channel.id == 811584272825712692) and (role == '견적'):
            PC = get(ctx.guild.roles, name='견적')
            await ctx.author.remove_roles(PC)
            await ctx.message.add_reaction('👍')

        else:
            await ctx.respond('번지수 잘못 찾아왔다ㅡㅡ')

def setup(bot):
    bot.add_cog(Util(bot))