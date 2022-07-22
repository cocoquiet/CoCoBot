import discord
import asyncio
from discord.ext.commands import Cog, has_permissions
from discord.commands import slash_command, Option
from discord.utils import get

from logTranslation import translateLog

from config import CoCoColor
from config import CoCoVER

class Admin(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    @has_permissions(administrator=True)
    async def kick(self, ctx, kicked_user: Option(discord.Member, '추방할 유저', required=True), reason: Option(str, '추방하는 이유', required=False, default=None)):
        """문제가 있는 사람들을 추방시켜줄게요."""
        
        await ctx.respond(embed=discord.Embed(title='강퇴', description=kicked_user.mention + '님을 추방합니다', color=CoCoColor))
        await kicked_user.kick(reason=reason)

    @slash_command()
    @has_permissions(administrator=True)
    async def ban(self, ctx, banned_user: Option(discord.Member, '차단할 유저', required=True), reason: Option(str, '차단하는 이유', required=False, default=None)):
        """마음에 들지 않은 사람들을 차단시켜 줄게요."""
        
        await ctx.respond(embed=discord.Embed(title='강퇴', description=banned_user.mention + '님을 추방합니다', color=CoCoColor))
        await banned_user.ban(reason=reason)

    @slash_command()
    @has_permissions(administrator=True)
    async def mute_chat(self, ctx, muted_user: Option(discord.Member, '뮤트할 유저', required=True), mute_mode: Option(str, '뮤트 모드', choices=['현재 채널 뮤트', '서버 전체 뮤트'], required=False, default=None)):
        """채팅이 시끄러운 사람들을 조용히 있게 해줄게요."""
        
        if mute_mode == None:
            muteEmbed = discord.Embed(title='채팅 뮤트', description='명령어 뒤에 뮤트 모드를 적어주세요', color=CoCoColor)
            muteEmbed.add_field(name='`1.` 현재 채널 뮤트', value='이 채널에서만 뮤트시킵니다', inline=False)
            muteEmbed.add_field(name='`2.` 서버 전체 뮤트', value='서버 전체에서 뮤트시킵니다', inline=False)

            await ctx.respond(embed=muteEmbed)

        else:
            sinner = discord.PermissionOverwrite()
            sinner.send_messages = False
            sinner.send_messages_in_threads = False
            sinner.create_public_threads = False
            sinner.create_private_threads = False
            sinner.embed_links = False
            sinner.attach_files = False
            sinner.add_reactions = False
            sinner.use_external_emojis = False
            sinner.use_external_stickers = False
            sinner.mention_everyone = False
            sinner.manage_messages = False
            sinner.manage_threads = False
            sinner.read_message_history = False
            sinner.send_tts_messages = False
            sinner.use_application_commands = False
            sinner.manage_channels = False
            sinner.manage_permissions = False
            sinner.manage_webhooks = False
            sinner.create_instant_invite = False

            if mute_mode == '현재 채널 뮤트':
                await ctx.channel.set_permissions(muted_user, overwrite=sinner)
                await ctx.respond(embed=discord.Embed(title='현재 채널 뮤트', description=f'뮤트 대상 : {muted_user.mention}\n뮤트 채널 : {ctx.channel.mention}\n`뮤트했습니다`', color=CoCoColor))

            elif mute_mode == '서버 전체 뮤트':
                for sinnerChannel in ctx.guild.text_channels:
                    if muted_user in sinnerChannel.members:
                        await sinnerChannel.set_permissions(muted_user, overwrite=sinner)

                await ctx.respond(embed=discord.Embed(title='서버 전체 뮤트', description=f'뮤트 대상 : {muted_user.mention}\n`뮤트했습니다`', color=CoCoColor))

    @slash_command()
    @has_permissions(administrator=True)
    async def unmute_chat(self, ctx, unmuted_user: Option(discord.Member, '언뮤트할 유저', required=True), mute_mode: Option(str, '언뮤트 모드', choices=['현재 채널 언뮤트', '서버 전체 언뮤트'], required=False, default=None)):
        """채팅이 조용해진 사람들을 말할 수 있게 해줄게요."""
        
        if mute_mode == None:
            unmuteEmbed = discord.Embed(title='채팅 언뮤트', description= '명령어 뒤에 언뮤트 모드를 적어주세요', color=CoCoColor)
            unmuteEmbed.add_field(name='`1.` 현재 채널 언뮤트', value='이 채널에서만 언뮤트시킵니다', inline=False)
            unmuteEmbed.add_field(name='`2.` 서버 전체 언뮤트', value='서버 전체에서 언뮤트시킵니다', inline=False)

            await ctx.respond(embed=unmuteEmbed)

        else:
            if mute_mode == '현재 채널 언뮤트':
                await ctx.channel.set_permissions(unmuted_user, overwrite=None)
                await ctx.respond(embed=discord.Embed(title='현재 채널 언뮤트', description=f'언뮤트 대상 : {unmuted_user.mention}\n언뮤트 채널 : {ctx.channel.mention}\n`언뮤트했습니다`', color=CoCoColor))

            elif mute_mode == '서버 전체 언뮤트':
                for sinnerChannel in ctx.guild.text_channels:
                    if unmuted_user in sinnerChannel.members:
                        await sinnerChannel.set_permissions(unmuted_user, overwrite=None)

                await ctx.respond(embed=discord.Embed(title='서버 전체 언뮤트', description=f'언뮤트 대상 : {unmuted_user.mention}\n`언뮤트했습니다`', color=CoCoColor))

    @slash_command()
    @has_permissions(administrator=True)
    async def mute_voice(self, ctx, muted_user: Option(discord.Member, '뮤트할 유저', required=False, default=None)):
        """소리가 시끄러운 사람들을 조용히 있게 해줄게요."""
        
        muteChannel = ctx.author.voice.channel
        
        if muted_user == None:
            members = muteChannel.members
            init_member = members[0]
            for member in members:
                await member.edit(mute=True)
            await ctx.respond(embed=discord.Embed(title='음성 뮤트', description=f'뮤트 대상 : {init_member.mention} 외 {len(members)-1}명\n뮤트 채널 : {muteChannel.mention}\n`뮤트했습니다`', color=CoCoColor))
        else:
            await muted_user.edit(mute=True)
            await ctx.respond(embed=discord.Embed(title='음성 뮤트', description=f'뮤트 대상 : {muted_user.mention}\n뮤트 채널 : {muteChannel.mention}\n`뮤트했습니다`', color=CoCoColor))

    @slash_command()
    @has_permissions(administrator=True)
    async def unmute_voice(self, ctx, unmuted_user: Option(discord.Member, '언뮤트할 유저', required=False, default=None)):
        """소리가 조용해진 사람들을 말할 수 있게 해줄게요."""
        
        unmuteChannel = ctx.author.voice.channel
        
        if unmuted_user == None:
            members = unmuteChannel.members
            initMember = members[0]
            for member in members:
                await member.edit(mute=False)
            await ctx.respond(embed=discord.Embed(title='음성 언뮤트', description=f'뮤트 대상 : {initMember.mention} 외 {len(members)-1}명\n언뮤트 채널 : {unmuteChannel.mention}\n`언뮤트했습니다`', color=CoCoColor))
        else:
            await unmuted_user.edit(mute=False)
            await ctx.respond(embed=discord.Embed(title='음성 언뮤트', description=f'언뮤트 대상 : {unmuted_user.mention}\n언뮤트 채널 : {unmuteChannel.mention}\n`언뮤트했습니다`', color=CoCoColor))

    @slash_command(guild_ids = [675171256299028490])
    @has_permissions(administrator=True)
    async def restrict(self, ctx, sinner: Option(discord.Member, '감금시킬 유저', required=True)):
        """중한 죄를 저지른 사람들을 뒤주에 보내줄게요."""
        
        memberRole = sinner.roles[1:]
        for roleIndex in memberRole:
            role = get(ctx.guild.roles, name=roleIndex.name)
            
            await sinner.remove_roles(role)
        
        sinnerRole = get(ctx.guild.roles, name='죄인')    
        await sinner.add_roles(sinnerRole)
        
        await ctx.delete()

    @slash_command()
    @has_permissions(administrator=True)
    async def move(self, ctx, channel: Option(discord.VoiceChannel, '이동 채널', required=True), members: Option(str, '이동시킬 유저들', required=True)):
        """원하는 음성 채널로 사람들을 보내줄게요."""
        
        for member in members.split():
            member = await ctx.guild.fetch_member(int(member[3:-1]))

            await member.move_to(channel)
            
        await ctx.delete()

    @slash_command(guild_ids = [675171256299028490])
    @has_permissions(administrator=True)
    async def submarine(self, ctx, members: Option(str, '잠수시킬 유저들', required=True)):
        """조용해보이는 사람들을 잠수함에 보내줄게요."""
        
        channel = ctx.guild.get_channel(886321655306129430) 

        for member in members.split():
            member = await ctx.guild.fetch_member(int(member[3:-1]))

            await member.move_to(channel)
            
        await ctx.delete()

    @slash_command()
    @has_permissions(administrator=True)
    async def clear(self, ctx, amount: Option(int, '삭제할 개수', required=False, default=None), name: Option(discord.TextChannel, '채널 이름', required=False, default=None)):
        """많은 메세지를 한번에 삭제시켜줄게요. 개수를 입력하지 않으면 10개를, -1을 입력하면 다 삭제할게요."""
        
        if amount == None:
            await ctx.channel.purge(limit=10)
        elif amount == -1:
            if name == ctx.channel:
                position = ctx.channel.position
                newChannel = await ctx.channel.clone()
                await ctx.channel.delete()
                await newChannel.edit(position=position)
            elif name == None:
                await ctx.respond('사고 대비를 위해 채널을 멘션해주세요')
        else:
            await ctx.channel.purge(limit=amount)

        await ctx.delete()

    @slash_command()
    @has_permissions(administrator=True)
    async def reset(self, ctx, name: Option(discord.TextChannel, '채널 이름', required=False, default=None)):
        """채팅방을 맨 처음의 모습으로 돌려줄게요."""
        
        if name == ctx.channel:
            position = ctx.channel.position
            newChannel = await ctx.channel.clone()
            await ctx.channel.delete()
            await newChannel.edit(position=position)
        elif name == None:
            await ctx.respond('사고 대비를 위해 채널을 멘션해주세요')

    @slash_command()
    @has_permissions(administrator=True)
    async def log(self, ctx, amount: Option(int, '로그 갯수', required=False, default=10), moderator: Option(discord.Member, '로그 주체', required=False, default=None)):
        """이 서버의 감사 로그를 보여줄게요."""
        
        log = ''                                         # 로그 (10개 단위)  
        logList = []                                     # log 10개씩 하나로 담은 리스트
        logIndex = 1                                     # log 개수 (10개씩 끊어서 logList에 담기)

        embedPage = 0                                    # 임베드 페이지 (0에서 시작)
        
        def editPage(moderator, embedPage):              # 임베드 정의 함수 (사용자 및 페이지 정의)
            if moderator == None:
                return discord.Embed(title='감사로그', description='\n\n' + logList[embedPage], color=CoCoColor)
            else:
                return discord.Embed(title=moderator.name + '님의 감사로그', description='\n\n' + logList[embedPage], color=CoCoColor)
        
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
            await ctx.respond(embed=embed)
        else:
            embed.set_footer(text=f'페이지 {embedPage + 1}/{len(logList)}\n' + CoCoVER)
            page = await ctx.respond(embed=embed)
            
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
        
    @slash_command(guild_ids = [675171256299028490])
    @has_permissions(administrator=True)
    async def ccc(self, ctx):
        """모든 어드민들을 불러줄게요."""
        
        admin = get(ctx.guild.roles, name='Admin')
        await ctx.respond(ctx.author.mention + '님이 불렀습니다 : ' + str(admin.mention))
        
def setup(bot):
    bot.add_cog(Admin(bot))