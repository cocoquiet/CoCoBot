import discord
import asyncio
from discord.ext import commands

import numpy as np

EmojiDict = {
                0: { # 기본
                    '1': ':one:',
                    '2': ':two:',
                    '3': ':three:',
                    '4': ':four:',
                    '5': ':five:',
                    '6': ':six:',
                    '7': ':seven:',
                    '8': ':eight:',
                    '9': ':nine:',
                    'q': ':regional_indicator_a:',
                    'w': ':regional_indicator_b:',
                    'e': ':regional_indicator_c:',
                    'r': ':regional_indicator_d:',
                    '-': ':black_large_square:',
                    '=': '🟧',
                    'a': ':new_moon:',
                    'A': ':cd:',
                    'b': '⚪',
                    'B': ':dvd:', 
                    'm': '기본'}, 
                1: { # 단색
                    '1': ':one:',
                    '2': ':two:',
                    '3': ':three:',
                    '4': ':four:',
                    '5': ':five:',
                    '6': ':six:',
                    '7': ':seven:',
                    '8': ':eight:',
                    '9': ':nine:',
                    'q': ':regional_indicator_a:',
                    'w': ':regional_indicator_b:',
                    'e': ':regional_indicator_c:',
                    'r': ':regional_indicator_d:',
                    '-': ':black_large_square:',
                    '=': '🟧',
                    'a': ':new_moon:',
                    'A': ':cd:',
                    'b': ':new_moon:',
                    'B': ':cd:', 
                    'm': '단색'}, 
                2: { # 맹기
                    '1': ':one:',
                    '2': ':two:',
                    '3': ':three:',
                    '4': ':four:',
                    '5': ':five:',
                    '6': ':six:',
                    '7': ':seven:',
                    '8': ':eight:',
                    '9': ':nine:',
                    'q': ':regional_indicator_a:',
                    'w': ':regional_indicator_b:',
                    'e': ':regional_indicator_c:',
                    'r': ':regional_indicator_d:',
                    '-': ':black_large_square:',
                    '=': '🟧',
                    'a': '🟧',
                    'A': '🟧',
                    'b': '🟧',
                    'B': '🟧', 
                    'm': '맹기'}, 
                3: { # 속기
                    '1': ':one:',
                    '2': ':two:',
                    '3': ':three:',
                    '4': ':four:',
                    '5': ':five:',
                    '6': ':six:',
                    '7': ':seven:',
                    '8': ':eight:',
                    '9': ':nine:',
                    'q': ':regional_indicator_a:',
                    'w': ':regional_indicator_b:',
                    'e': ':regional_indicator_c:',
                    'r': ':regional_indicator_d:',
                    '-': ':black_large_square:',
                    '=': '🟧',
                    'a': ':new_moon:',
                    'A': ':cd:',
                    'b': '⚪',
                    'B': ':dvd:', 
                    'm': '속기'} 
                }

newBoard = np.array([[45, 49, 50, 51, 52, 53, 54, 55, 56, 57, 113, 119, 101, 114], 
                    [49, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                    [50, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                    [51, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                    [52, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                    [53, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                    [54, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                    [55, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                    [56, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                    [57, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                    [113, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                    [119, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                    [101, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                    [114, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61]])

Board = ""

omokPlayer1 = None
omokPlayer2 = None
omokTurn = None

is_playing = False

modeNum = None

def DrawBoard(): # 보드 갱신 함수
    global EmojiDict

    global newBoard
    global Board

    global modeNum

    Board = ""
    for r in range(0, 14):
        for c in range(0, 14):
            char = chr(newBoard[r, c])
            if char in EmojiDict[modeNum].keys():
                Board += EmojiDict[modeNum][char]
        Board += "\n"
    
def reset(): # 게임 리셋 함수
    global modeNum

    global omokPlayer1
    global omokPlayer2
    global omokTurn

    global is_playing

    global newBoard

    modeNum = None

    omokPlayer1 = None
    omokPlayer2 = None
    omokTurn = None

    is_playing = False

    newBoard = np.array([[45, 49, 50, 51, 52, 53, 54, 55, 56, 57, 113, 119, 101, 114], 
                        [49, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                        [50, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                        [51, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                        [52, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                        [53, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                        [54, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                        [55, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                        [56, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                        [57, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                        [113, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                        [119, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                        [101, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61], 
                        [114, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61]])

class Omok(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="오목", aliases=["omok"])
    async def omok(self, ctx, opponent : discord.Member, mode : int = None):
        global EmojiDict

        global omokPlayer1
        global omokPlayer2
        
        global newBoard
        global Board

        global modeNum

        omokPlayer1 = ctx.author
        omokPlayer2 = opponent

        if omokPlayer1 == omokPlayer2: # 혼자 플레이하려고 할 때
            await ctx.send("아싸냐\n같이 할 친구 데리고 와라")
        else:
            if mode == None:
                mode = 0
            modeNum = mode

            DrawBoard()

            embed = discord.Embed(title="오목", color=0x000000)
            embed.add_field(name="플레이어", value="Player 1: " + omokPlayer1.mention + "\nPlayer 2: " + omokPlayer2.mention, inline=False)
            embed.add_field(name="모드", value=EmojiDict[mode]['m'], inline=False)
            embed.add_field(name="현재 오목판", value=Board, inline=False)
            await ctx.send(embed=embed)

            helpCommand = discord.Embed(title="명령어", description="모든 오목 명령어는 답장을 기본으로 합니다.", color=0x000000)
            helpCommand.add_field(name="`/오목 <다른 플레이어> <모드 번호>`", value="> 다른 사람과 오목을 하게 해줄게요.\n모드 번호는 `/오목 모드`로 알려줄게요.", inline=False)
            helpCommand.add_field(name="`/오목 모드`", value="> 오목의 여러 모드들을 알려줄게요.", inline=False)
            helpCommand.add_field(name="`/참가`", value="> 오목 대결 신청을 한 사람과 오목을 하게 해줄게요.", inline=False)
            helpCommand.add_field(name="`/거절`", value="> 오목 대결 신청을 한 사람과 오목을 하기 싫을 때 대신 거절해줄게요.", inline=False)
            helpCommand.add_field(name="`/돌`", value="> 오목판에 돌을 두게 해줄게요.", inline=False)
            helpCommand.add_field(name="`/기권`", value="> 오목을 할 때 수가 생각나지 않는다면 기권해줄게요.", inline=False)
            await ctx.send(embed=helpCommand)

    @commands.command(name="오목 모드", aliases=[])
    async def ExplainMode(self, ctx):
        embed = discord.Embed(title="모드 설명", color=0x000000)
        embed.add_field(name="0. `기본 모드`", value="> 기본적인 오목입니다.\n`/오목` 뒤에 모드 번호를 치지 않으면 자동으로 기본모드가 됩니다.", inline=False)
        embed.add_field(name="1. `단색 모드`", value="> 자신과 상대의 돌의 색이 같아집니다.\n돌의 색을 구분하지 못하는 게 이 모드의 묘미입니다.", inline=False)
        embed.add_field(name="2. `맹기 모드`", value="> 오목판에 돌이 가려집니다.\n단색 모드보다 더 까다로운 모드입니다.", inline=False)
        # embed.add_field(name="3. `속기 모드`", value="> 제한시간이 단축된 오목입니다.\n주어진 10초 안에 착수를 해야 합니다.", inline=False)

        await ctx.send(embed=embed)

    @commands.command(name="참가", aliases=["콜", "플레이", "덤벼", "ㄱㄱ"])
    async def admit(self, ctx):
        global omokPlayer1
        global omokPlayer2
        global omokTurn

        global is_playing

        if ctx.message.reference != None:
            replied_msg = await self.bot.get_channel(ctx.message.reference.channel_id).fetch_message(ctx.message.reference.message_id)
            if (replied_msg.author == self.bot.user) and (is_playing == False): # 오목 시작X 경우
                if ctx.author == omokPlayer2:
                    await ctx.message.reply(omokPlayer2.mention + "님 준비완료!!\n" + omokPlayer1.mention + "님 선공입니다!!")
                    is_playing = True
                    omokTurn = omokPlayer1
                elif ctx.author == omokPlayer1:
                    await ctx.message.reply("너가 게임을 신청했는데 왜 너가 입장을 해ㅡㅡ")
                else:
                    await ctx.send("넌 누구야ㅡㅡ")
            else: # 오목 시작O 경우
                await ctx.send("뭐래 이미 게임 시작했는데ㅡㅡ")

    @commands.command(name="거절", aliases=["노콜", "싫어", "ㅌㅌ"])
    async def refuse(self, ctx):
        global omokPlayer1
        global omokPlayer2

        global is_playing

        if ctx.message.reference != None:
            replied_msg = await self.bot.get_channel(ctx.message.reference.channel_id).fetch_message(ctx.message.reference.message_id)
            if (replied_msg.author == self.bot.user) and (is_playing == False): # 오목 시작X 경우
                if ctx.author == omokPlayer2:
                    await ctx.message.reply(omokPlayer1.mention + " 야야 쟤 하기싫다는데..?")
                elif ctx.author == omokPlayer1:
                    await ctx.message.reply("너가 게임을 신청했는데 왜 너가 거절을 해ㅡㅡ")
                else:
                    await ctx.send("넌 누구야ㅡㅡ")
            else: # 오목 시작O 경우
                await ctx.send("뭐래 이미 게임 시작했는데ㅡㅡ")
    
    @commands.command(name="돌", aliases=["stone", "ㄷ", "e", "착수", "ㅊㅅ"])
    async def stone(self, ctx, row : int, col : int):
        global omokPlayer1
        global omokPlayer2
        global omokTurn

        global newBoard
        global Board

        WINNER = None
        is_RightPlayer = None

        if ctx.message.reference != None:
            replied_msg = await self.bot.get_channel(ctx.message.reference.channel_id).fetch_message(ctx.message.reference.message_id)
            if replied_msg.author == self.bot.user:
                if ctx.author == omokTurn: # 다음 차례인 경우
                    if newBoard[row, col] != 61:
                        await ctx.send("제대로 둬라ㅡㅡ")
                    else:
                        if omokTurn == omokPlayer1:
                            newBoard[row, col] = 97
                            omokTurn = omokPlayer2
                        elif omokTurn == omokPlayer2:
                            newBoard[row, col] = 98
                            omokTurn = omokPlayer1
                        await ctx.channel.purge(after=replied_msg) # 이전 보드 삭제
                        await replied_msg.delete()
                        is_RightPlayer = True
                elif (ctx.author == omokPlayer1) or (ctx.author == omokPlayer2): # 자기 차례 아닌 경우
                    await ctx.send("아직 차례 안 됐다ㅡㅡ")
                    is_RightPlayer = False
                else: # Player가 아닌 경우
                    await ctx.send("넌 누구야ㅡㅡ")
                    is_RightPlayer = False


        # 오목 줄 확인(ㅡ)
        for row in range(1, 14):
            for col in range(1, 10):
                if np.sum(newBoard[row, col:col+5]) == 485:
                    WINNER = omokPlayer1
                elif np.sum(newBoard[row, col:col+5]) == 490:
                    WINNER = omokPlayer2

        # 오목 줄 확인(|)
        for col in range(1, 14):
            for row in range(1, 10):
                if np.sum(newBoard[row:row+5, col]) == 485:
                    WINNER = omokPlayer1
                elif np.sum(newBoard[row:row+5, col]) == 490:
                    WINNER = omokPlayer2

        # 오목 줄 확인(\)
        for row in range(1, 10):
            for col in range(1, 10):
                if newBoard[row+0, col+0] + newBoard[row+1, col+1] + newBoard[row+2, col+2] + newBoard[row+3, col+3] + newBoard[row+4, col+4] == 485:
                    WINNER = omokPlayer1
                elif newBoard[row+0, col+0] + newBoard[row+1, col+1] + newBoard[row+2, col+2] + newBoard[row+3, col+3] + newBoard[row+4, col+4] == 490:
                    WINNER = omokPlayer2

        # 오목 줄 확인(/)
        for row in range(1, 10):
            for col in range(1, 10):
                if newBoard[row+4, col+0] + newBoard[row+3, col+1] + newBoard[row+2, col+2] + newBoard[row+1, col+3] + newBoard[row+0, col+4] == 485:
                    WINNER = omokPlayer1
                elif newBoard[row+4, col+0] + newBoard[row+3, col+1] + newBoard[row+2, col+2] + newBoard[row+1, col+3] + newBoard[row+0, col+4] == 490:
                    WINNER = omokPlayer2
                
        # 승리 여부 확인 & 보드 업데이트
        if WINNER == None:
            DrawBoard()
            embed = discord.Embed(title="착수", description=omokTurn.mention + "님의 차례입니다", color=0x000000)
            embed.add_field(name="현재 오목판", value=Board, inline=False)

        elif WINNER == omokPlayer1:
            DrawBoard()
            await ctx.send(omokPlayer1.mention + "승리!!!")
            embed = discord.Embed(color=0x000000)
            embed.add_field(name="최종 오목판", value=Board, inline=False)

        elif WINNER == omokPlayer2:
            DrawBoard()
            await ctx.send(omokPlayer2.mention + "승리!!!")
            embed = discord.Embed(color=0x000000)
            embed.add_field(name="최종 오목판", value=Board, inline=False)

        if is_RightPlayer == True:
            await ctx.send(embed=embed)
        else:
            pass

        if WINNER != None:
            reset()

    @commands.command(name="기권", aliases=["gg", "항복"])
    async def GG(self, ctx):
        global omokPlayer1
        global omokPlayer2
        global omokTurn

        global is_playing

        if ctx.message.reference != None:
            replied_msg = await self.bot.get_channel(ctx.message.reference.channel_id).fetch_message(ctx.message.reference.message_id)
            if replied_msg.author == self.bot.user:
                if ctx.author == omokPlayer1: # Player1 기권
                    embed = discord.Embed(color=0x000000)
                    embed.add_field(name="기권", value=omokPlayer1.mention + " 기권\n" + omokPlayer2.mention + " 승리!!!")
                elif ctx.author == omokPlayer2: # Player2 기권
                    embed = discord.Embed(color=0x000000)
                    embed.add_field(name="기권", value=omokPlayer2.mention + " 기권\n" + omokPlayer1.mention + " 승리!!!")
                else:
                    embed = discord.Embed(color=0x000000) # Player가 아닌 경우
                    embed.add_field(name="넌 누구냐", value="오목 하지도 않으면서 뭔 기권이야ㅡㅡ")

                await ctx.send(embed=embed)

                reset()

def setup(bot):
    bot.add_cog(Omok(bot))