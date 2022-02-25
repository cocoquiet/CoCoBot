import discord
import asyncio
from discord.ext.commands import Cog
from discord.commands import slash_command

from datetime import datetime

class Secret(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='설빙')
    async def sulbing(self, ctx):
        """설빙"""
        
        remainder = (datetime.strptime('20221117', '%Y%m%d') - datetime.now()).days + 1
        
        await ctx.respond(f'설님 수능까지 {remainder}일 남았습니다!!!!!')

    @slash_command(name='러리')
    async def lery(self, ctx):
        """러리"""
        
        await ctx.respond('러리님 과제 화이팅하세요!!!!!!!!!!')

    @slash_command(name='암고')
    async def amgo(self, ctx):
        """암고"""
        
        await ctx.respond('암고님 공부하세요!!!')

    @slash_command(name='양사')
    async def yangsa(self, ctx):
        """양사"""
        
        remainder = (datetime.strptime('20221117', '%Y%m%d') - datetime.now()).days + 1
        
        await ctx.respond(f'양사님 수능까지 {remainder}일 남았습니다!!!!!')

def setup(bot):
    bot.add_cog(Secret(bot))