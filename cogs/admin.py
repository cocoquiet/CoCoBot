import discord
import asyncio
from discord.ext import commands
from discord.utils import get

from logTranslation import translateLog

from config import CoCoColor
from config import CoCoVER

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', aliases=['강퇴', '추방'])
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, kickedUser : discord.Member, *, reason=None):
        await ctx.send(embed=discord.Embed(title='강퇴', description=kickedUser.mention + '님을 추방합니다', color=CoCoColor))
        await kickedUser.kick(reason=reason)

    @commands.command(name='ban', aliases=['차단'])
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, bannedUser : discord.Member, *, reason=None):
        await ctx.send(embed=discord.Embed(title='강퇴', description=bannedUser.mention + '님을 추방합니다', color=CoCoColor))
        await bannedUser.ban(reason=reason)
        
    @commands.command(name='mute', aliases=['뮤트', 'ㅁㅌ', 'mt'])
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, mutedUser : discord.Member, muteMode : int = None):
        if muteMode == None:
            muteEmbed = discord.Embed(title='뮤트', description='명령어 뒤에 모드 번호를 적어주세요', color=CoCoColor)
            muteEmbed.add_field(name='`1.` 현재 채널 뮤트', value='이 채널에서만 뮤트시킵니다', inline=False)
            muteEmbed.add_field(name='`2.` 서버 전체 뮤트', value='서버 전체에서 뮤트시킵니다', inline=False)

            await ctx.send(embed=muteEmbed)

        else:
            sinner = discord.PermissionOverwrite()
            sinner.send_messages = False
            sinner.manage_channels = False
            sinner.manage_permissions = False
            sinner.manage_webhooks = False
            sinner.create_instant_invite = False
            sinner.embed_links = False
            sinner.attach_files = False
            sinner.add_reactions = False
            sinner.use_external_emojis = False
            sinner.mention_everyone = False
            sinner.manage_messages = False
            sinner.send_tts_messages = False

            if muteMode == 1:
                await ctx.channel.set_permissions(mutedUser, overwrite=sinner)
                await ctx.send(embed=discord.Embed(title='현재 채널 뮤트', 
                                                    description='뮤트 대상 : ' + mutedUser.mention + '\n뮤트 채널 : ' + ctx.channel.mention + '\n`뮤트했습니다`', 
                                                    color=CoCoColor))

            elif muteMode == 2:
                page = await ctx.send(embed=discord.Embed(title='서버 전체 뮤트', description='뮤트 대상 : ' + mutedUser.mention + '\n뮤트하시겠습니까?', color=CoCoColor))

                await page.add_reaction('✔️')
                await page.add_reaction('❌')

                def muteCheck(reaction, user):
                    return user == ctx.author
            
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout = 30.0, check = muteCheck)
                except asyncio.TimeoutError:
                    await page.edit(embed=discord.Embed(title='서버 전체 뮤트', description='뮤트 대상 : ' + mutedUser.mention + '\n`취소되었습니다`', color=CoCoColor))
                    await page.clear_reactions()
                else:
                    if reaction.emoji == '✔️':
                        for sinnerChannel in ctx.guild.text_channels:
                            if mutedUser in sinnerChannel.members:
                                await sinnerChannel.set_permissions(mutedUser, overwrite=sinner)

                        await page.clear_reactions()
                        await page.edit(embed=discord.Embed(title='서버 전체 뮤트', description='뮤트 대상 : ' + mutedUser.mention + '\n`뮤트했습니다`', color=CoCoColor))
                    elif reaction.emoji == '❌':
                        await page.clear_reactions()
                        await page.edit(embed=discord.Embed(title='서버 전체 뮤트', description='뮤트 대상 : ' + mutedUser.mention + '\n`취소되었습니다`', color=CoCoColor))

    @commands.command(name='unmute', aliases=['언뮤트', 'ㅇㅁㅌ', 'umt'])
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, unmutedUser : discord.Member, muteMode : int = None):
        if muteMode == None:
            muteEmbed = discord.Embed(title='뮤트', description= '명령어 뒤에 모드 번호를 적어주세요', color=CoCoColor)
            muteEmbed.add_field(name='`1.` 현재 채널 언뮤트', value='이 채널에서만 언뮤트시킵니다', inline=False)
            muteEmbed.add_field(name='`2.` 서버 전체 언뮤트', value='서버 전체에서 언뮤트시킵니다', inline=False)

            await ctx.send(embed=muteEmbed)

        else:
            if muteMode == 1:
                await ctx.channel.set_permissions(unmutedUser, overwrite=None)
                await ctx.send(embed=discord.Embed(title='현재 채널 언뮤트', 
                                                    description='언뮤트 대상 : ' + unmutedUser.mention + '\n언뮤트 채널 : ' + ctx.channel.mention + '\n`언뮤트했습니다`', 
                                                    color=CoCoColor))

            elif muteMode == 2:
                page = await ctx.send(embed=discord.Embed(title='서버 전체 언뮤트', description='언뮤트 대상 : ' + unmutedUser.mention + '\n언뮤트하시겠습니까?', color=CoCoColor))

                await page.add_reaction('✔️')
                await page.add_reaction('❌')

                def unmuteCheck(reaction, user):
                    return user == ctx.author
            
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout = 30.0, check = unmuteCheck)
                except asyncio.TimeoutError:
                    page.clear_reactions()
                else:
                    if reaction.emoji == '✔️':
                        for sinnerChannel in ctx.guild.text_channels:
                            if unmutedUser in sinnerChannel.members:
                                await sinnerChannel.set_permissions(unmutedUser, overwrite=None)

                        await page.clear_reactions()
                        await page.edit(embed=discord.Embed(title='서버 전체 언뮤트', description='언뮤트 대상 : ' + unmutedUser.mention + '\n`언뮤트했습니다`', color=CoCoColor))
                    elif reaction.emoji == '❌':
                        await page.clear_reactions()
                        await page.edit(embed=discord.Embed(title='서버 전체 언뮤트', description='언뮤트 대상 : ' + unmutedUser.mention + '\n`취소되었습니다`', color=CoCoColor))

    @commands.command(name='잠수함', aliases=['submarine', 'ㅈㅅㅎ', '잠수'])
    @commands.has_permissions(administrator=True)
    async def submarine(self, ctx, *members: discord.Member):
        channel = ctx.guild.get_channel(886321655306129430) 

        for member in members:
            member = ctx.guild.get_member(member.id)

            await member.move_to(channel)

    @commands.command(name='청소', aliases=['clean', 'clear', 'purge'])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount : int = None, name : discord.TextChannel = None):
        if amount == None:
            await ctx.channel.purge(limit=11)
        elif amount == -1:
            if name == ctx.channel:
                position = ctx.channel.position
                newChannel = await ctx.channel.clone()
                await ctx.channel.delete()
                await newChannel.edit(position=position)
            elif name == None:
                await ctx.send('사고 대비를 위해 채널을 멘션해주세요')
        else:
            await ctx.channel.purge(limit=amount + 1)

    @commands.command(name='초기화', aliases=['reset', '리셋', 'delall'])
    @commands.has_permissions(administrator=True)
    async def reset(self, ctx, name : discord.TextChannel = None):
        if name == ctx.channel:
            position = ctx.channel.position
            newChannel = await ctx.channel.clone()
            await ctx.channel.delete()
            await newChannel.edit(position=position)
        elif name == None:
            await ctx.send('사고 대비를 위해 채널을 멘션해주세요')

    @commands.command(name='로그', aliases=['log', '감사로그'])
    @commands.has_permissions(administrator=True)
    async def log(self, ctx, amount : int = None, moderator : discord.Member = None):
        log = ''                                         # 로그 (10개 단위)  
        logList = []                                     # log 10개씩 하나로 담은 리스트
        logIndex = 1                                     # log 개수 (10개씩 끊어서 logList에 담기)

        embedPage = 0                                    # 임베드 페이지 (0에서 시작)
        
        def editPage(moderator, embedPage):              # 임베드 정의 함수 (사용자 및 페이지 정의)
            if moderator == None:
                return discord.Embed(title='감사로그', description='\n\n' + logList[embedPage], color=CoCoColor)
            else:
                return discord.Embed(title=moderator.name + '님의 감사로그', description='\n\n' + logList[embedPage], color=CoCoColor)
        
        if amount == None:
            amount = 10

        async for entry in ctx.guild.audit_logs(user=moderator, limit=amount):
            translatedAction = translateLog(entry, entry.action)
            if entry.target == None:
                log += '`' + str(logIndex) + '.` ' + entry.user.mention + '님이 ' + translatedAction + '\n'
            else:
                log += '`' + str(logIndex) + '.` ' + entry.user.mention + '님이 ' + translatedAction + '\n'
                
            if logIndex % 10 == 0:
                logList.append(log)
                log = ''
                logIndex += 1
            elif logIndex != amount:
                logIndex += 1
            else:
                logList.append(log)

        embed = editPage(moderator, embedPage)
        
        if len(logList) == 1:
            embed.set_footer(text=CoCoVER)
            await ctx.send(embed=embed)
        else:
            embed.set_footer(text=f'페이지 {embedPage + 1}/{len(logList)}\n' + CoCoVER)
            page = await ctx.send(embed=embed)
            
            reaction = None                              # 이모지 반응

            await page.add_reaction('⏮')
            await page.add_reaction('◀')
            await page.add_reaction('▶')
            await page.add_reaction('⏭')

            def check(reaction, user):
                return user == ctx.author

            while True:
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout = 300.0, check = check)
                except asyncio.TimeoutError:
                    await page.clear_reactions()
                    break
                else:
                    if reaction.emoji == '⏮':
                        embedPage = 0
                    elif reaction.emoji == '◀':
                        if embedPage > 0:
                            embedPage -= 1
                    elif reaction.emoji == '▶':
                        if embedPage < len(logList) - 1:
                            embedPage += 1
                    elif reaction.emoji == '⏭':
                        embedPage = len(logList) - 1

                    await page.remove_reaction(reaction, user)
                    
                    embed = editPage(moderator, embedPage)
                    embed.set_footer(text=f'페이지 {embedPage + 1}/{len(logList)}\n' + CoCoVER)
                    await page.edit(embed = embed)
        
    @commands.command(name='고코위', aliases=['관리자'])
    @commands.has_permissions(administrator=True)
    async def CCC(self, ctx):
        admin = get(ctx.guild.roles, name='Admin')
        await ctx.send(ctx.message.author.mention + '님이 불렀습니다 : ' + str(admin.mention))
        
def setup(bot):
    bot.add_cog(Admin(bot))