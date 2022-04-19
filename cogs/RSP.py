import discord
import asyncio
from discord.ext.commands import Cog
from discord.commands import slash_command, Option

import random

class RSP(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='가위바위보')
    async def rock_scissors_paper(self, ctx, selection: Option(str, '선택', choices=['가위', '바위', '보'], required=True)):
        """가위바위보를 해줄게요."""
        
        botSelection = random.randint(1, 3)

        if selection == '가위':            
            if  botSelection== 1:
                await ctx.respond('당신은 가위를 냈습니다. \n저도 가위를 냈습니다. 비겼습니다')
            elif botSelection == 2:
                await ctx.respond('당신은 가위를 냈습니다. \n저는 바위를 냈습니다. 제가 이겼습니다')
            elif botSelection == 3:
                await ctx.respond('당신은 가위를 냈습니다. \n저는 보를 냈습니다. 제가 졌습니다')
                
        elif selection == '바위':
            if botSelection == 1:
                await ctx.respond('당신은 바위를 냈습니다. \n저는 가위를 냈습니다. 제가 졌습니다')
            elif botSelection == 2:
                await ctx.respond('당신은 바위를 냈습니다. \n저도 바위를 냈습니다. 비겼습니다')
            elif botSelection == 3:
                await ctx.respond('당신은 바위를 냈습니다. \n저는 보를 냈습니다. 제가 이겼습니다')

        elif selection == '보':
            if botSelection == 1:
                await ctx.respond('당신은 보를 냈습니다. \n저는 가위를 냈습니다. 제가 이겼습니다')
            elif botSelection == 2:
                await ctx.respond('당신은 보를 냈습니다. \n저는 바위를 냈습니다. 제가 졌습니다')
            elif botSelection == 3:
                await ctx.respond('당신은 보를 냈습니다. \n저도 보를 냈습니다. 비겼습니다')

def setup(bot):
    bot.add_cog(RSP(bot))