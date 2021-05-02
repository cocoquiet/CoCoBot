import discord
import asyncio
from discord.ext import commands
from discord.utils import get

from logTranslation import translateLog

from config import CoCo_VER

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick", aliases=["강퇴", "추방"])
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, user : discord.Member, *, reason=None):
        await user.kick(reason=reason)

    @commands.command(name="ban", aliases=["차단"])
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, user : discord.Member, *, reason=None):
        await user.ban(reason=reason)

    @commands.command(name="청소", aliases=["clean", "clear", "purge"])
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
                await ctx.send("사고 대비를 위해 채널을 멘션해주세요")
        else:
            await ctx.channel.purge(limit=amount + 1)

    @commands.command(name="초기화", aliases=["reset", "리셋", "delall"])
    @commands.has_permissions(administrator=True)
    async def reset(self, ctx, name : discord.TextChannel = None):
        if name == ctx.channel:
            position = ctx.channel.position
            newChannel = await ctx.channel.clone()
            await ctx.channel.delete()
            await newChannel.edit(position=position)
        elif name == None:
            await ctx.send("사고 대비를 위해 채널을 멘션해주세요")

    @commands.command(name="고코위", aliases=["관리자"])
    @commands.has_permissions(administrator=True)
    async def CCC(self, ctx):
        admin = get(ctx.guild.roles, name="Admin")
        await ctx.send(ctx.message.author.mention + "님이 불렀습니다 : " + str(admin.mention))
        
    @commands.command(name="로그", aliases=["log", "감사로그"])
    @commands.has_permissions(administrator=True)
    async def log(self, ctx, amount : int = None, moderator : discord.Member = None):
        log = ""                                         # 로그 (10개 단위)  
        logList = []                                     # log 10개씩 하나로 담은 리스트
        logIndex = 1                                     # log 개수 (10개씩 끊어서 logList에 담기)

        embedPage = 0                                    # 임베드 페이지 (0에서 시작)
        
        def editPage(moderator, embedPage):              # 임베드 정의 함수 (사용자 및 페이지 정의)
            if moderator == None:
                return discord.Embed(title="감사로그", description="\n\n" + logList[embedPage], color=0xFFFFFE)
            else:
                return discord.Embed(title=moderator.name + "님의 감사로그", description="\n\n" + logList[embedPage], color=0xFFFFFE)
        
        if amount == None:
            amount = 100

        async for entry in ctx.guild.audit_logs(user=moderator, limit=amount):
            translatedAction = translateLog(entry, entry.action)
            if entry.target == None:
                log += "`" + str(logIndex) + ".` " + entry.user.mention + "님이 " + translatedAction + "\n"
            else:
                log += "`" + str(logIndex) + ".` " + entry.user.mention + "님이 " + translatedAction + "\n"
                
            if logIndex % 10 == 0:
                logList.append(log)
                log = ""
                logIndex += 1
            elif logIndex != amount:
                logIndex += 1
            else:
                logList.append(log)

        embed = editPage(moderator, embedPage)
        embed.set_footer(text=f"페이지 {embedPage + 1}/{len(logList)}\n" + CoCo_VER)
        page = await ctx.send(embed=embed)
        
        if len(logList) == 1:
            return
        else:
            reaction = None                              # 이모지 반응

            await page.add_reaction("⏮")
            await page.add_reaction("◀")
            await page.add_reaction("▶")
            await page.add_reaction("⏭")

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
                    embed.set_footer(text=f"페이지 {embedPage + 1}/{len(logList)}\n" + CoCo_VER)
                    await page.edit(embed = embed)
        
        @commands.command(name="고코위", aliases=["관리자"])
        @commands.has_permissions(administrator=True)
        async def CCC(self, ctx):
            admin = get(ctx.guild.roles, name="Admin")
            await ctx.send(ctx.message.author.mention + "님이 불렀습니다 : " + str(admin.mention))
        
def setup(bot):
    bot.add_cog(Admin(bot))