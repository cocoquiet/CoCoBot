import discord
import asyncio
from discord.ext import commands

import numpy as np

EmojiDict = {
                0: {
                    '-': '⚫',
                    '1': '⚪',
                    '2': '🔴',
                    '3': '🟠',
                    '4': '🟡',
                    '5': '🟢',
                    '6': '🔵',
                    '7': '🟣',
                    '8': '🟤'},
                1: {
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
                    'a': '⚫',
                    'A': ':cd:',
                    'b': '⚪',
                    'B': ':dvd:'}, 
                2: {
                    '-': '⬛',
                    '1': '⬜',
                    '2': '🟥',
                    '3': '🟧',
                    '4': '🟨',
                    '5': '🟩',
                    '6': '🟦',
                    '7': '🟪',
                    '8': '🟫'}
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

OmokPlayer1 = None
OmokPlayer2 = None
OmokTurn = None

is_playing = False

def changeTurn():
    global OmokPlayer1
    global OmokPlayer2
    global OmokTurn

    if OmokTurn == OmokPlayer1:
        OmokTurn = OmokPlayer2
    elif OmokTurn == OmokPlayer2:
        OmokTurn = OmokPlayer1

def drawBoard():
    global newBoard
    global Board

    Board = ""
    for r in range(0, 14):
        for c in range(0, 14):
            char = chr(newBoard[r, c])
            if char in EmojiDict[1].keys():
                Board += EmojiDict[1][char]
        Board += "\n"
    
def endGame():
    global OmokPlayer1
    global OmokPlayer2
    global OmokTurn

    global is_playing

    global newBoard

    OmokPlayer1 = None
    OmokPlayer2 = None
    OmokTurn = None

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

    @commands.command(name="오목")
    async def omok(self, ctx, opponent : discord.Member):
        global OmokPlayer1
        global OmokPlayer2
        
        global newBoard
        global Board

        OmokPlayer1 = ctx.author
        OmokPlayer2 = opponent

        if OmokPlayer1 == OmokPlayer2:
            await ctx.send("혼자서 하는거야?\n아싸야?\nㅋ")
        else:
            drawBoard()

            embed = discord.Embed(title="오목", color=0x000000)
            embed.add_field(name="플레이어", value="Player 1: " + OmokPlayer1.mention + "\nPlayer 2: " + OmokPlayer2.mention, inline=False)
            embed.add_field(name="현재 오목판", value=Board, inline=False)

            await ctx.send(embed=embed)

    @commands.command(name="참가")
    async def admit(self, ctx):
        global OmokPlayer1
        global OmokPlayer2
        global OmokTurn

        global is_playing

        if ctx.message.reference != None:
            replied_msg = await self.bot.get_channel(ctx.message.reference.channel_id).fetch_message(ctx.message.reference.message_id)
            if (replied_msg.author == self.bot.user) and (is_playing == False):
                if ctx.author == OmokPlayer2:
                    await ctx.message.reply(OmokPlayer2.mention + "님 준비완료!!\n" + OmokPlayer1.mention + "님 선공입니다!!")
                    is_playing = True
                    OmokTurn = OmokPlayer1
                elif ctx.author == OmokPlayer1:
                    await ctx.message.reply("너가 게임을 신청했는데 왜 너가 입장을 해ㅡㅡ")
                else:
                    await ctx.send("넌 누구야ㅡㅡ")
            else:
                await ctx.send("뭐래 이미 게임 시작했는데ㅡㅡ")


    @commands.command(name="기권")
    async def GG(self, ctx):
        global OmokPlayer1
        global OmokPlayer2
        global OmokTurn

        global is_playing

        if ctx.message.reference != None:
            replied_msg = await self.bot.get_channel(ctx.message.reference.channel_id).fetch_message(ctx.message.reference.message_id)
            if replied_msg.author == self.bot.user:
                if ctx.author == OmokPlayer1:
                    embed = discord.Embed(color=0x000000)
                    embed.add_field(name=OmokPlayer1.mention + ": `GG`", value=OmokPlayer2.mention + " 승리!!!")
                elif ctx.author == OmokPlayer2:
                    embed = discord.Embed(color=0x000000)
                    embed.add_field(name=OmokPlayer2.mention + ": `GG`", value=OmokPlayer1.mention + " 승리!!!")
                else:
                    embed = discord.Embed(color=0x000000)
                    embed.add_field(name="넌 누구냐", value="오목 하지도 않으면서 뭔 기권이야ㅡㅡ")

                await ctx.send(embed=embed)

                endGame()

    @commands.command(name="돌")
    async def stone(self, ctx, row : int, col : int):
        global OmokPlayer1
        global OmokPlayer2
        global OmokTurn

        global newBoard
        global Board

        WINNER = None

        if ctx.message.reference != None:
            replied_msg = await self.bot.get_channel(ctx.message.reference.channel_id).fetch_message(ctx.message.reference.message_id)
            if replied_msg.author == self.bot.user:
                if ctx.author == OmokTurn:
                    if newBoard[row, col] != 61:
                        await ctx.send("제대로 둬라ㅡㅡ")
                    else:
                        if OmokTurn == OmokPlayer1:
                            newBoard[row, col] = 97
                            OmokTurn = OmokPlayer2
                        elif OmokTurn == OmokPlayer2:
                            newBoard[row, col] = 98
                            OmokTurn = OmokPlayer1
                elif (ctx.author == OmokPlayer1) or (ctx.author == OmokPlayer2):
                    await ctx.send("아직 차례 안 됐다ㅡㅡ")
                else:
                    await ctx.send("넌 누구야ㅡㅡ")

        for row in range(1, 14):
            for col in range(1, 10):
                if np.sum(newBoard[row, col:col+5]) == 485:
                    WINNER = OmokPlayer1
                elif np.sum(newBoard[row, col:col+5]) == 490:
                    WINNER = OmokPlayer2

        for col in range(1, 14):
            for row in range(1, 10):
                if np.sum(newBoard[row:row+5, col]) == 485:
                    WINNER = OmokPlayer1
                elif np.sum(newBoard[row:row+5, col]) == 490:
                    WINNER = OmokPlayer2

        for row in range(1, 10):
            for col in range(1, 10):
                if newBoard[row+0, col+0] + newBoard[row+1, col+1] + newBoard[row+2, col+2] + newBoard[row+3, col+3] + newBoard[row+4, col+4] == 485:
                    WINNER = OmokPlayer1
                elif newBoard[row+0, col+0] + newBoard[row+1, col+1] + newBoard[row+2, col+2] + newBoard[row+3, col+3] + newBoard[row+4, col+4] == 490:
                    WINNER = OmokPlayer2

        for row in range(1, 10):
            for col in range(1, 10):
                if newBoard[row+4, col+0] + newBoard[row+3, col+1] + newBoard[row+2, col+2] + newBoard[row+1, col+3] + newBoard[row+0, col+4] == 485:
                    WINNER = OmokPlayer1
                elif newBoard[row+4, col+0] + newBoard[row+3, col+1] + newBoard[row+2, col+2] + newBoard[row+1, col+3] + newBoard[row+0, col+4] == 490:
                    WINNER = OmokPlayer2
                
        if WINNER == None:
            drawBoard()
            embed = discord.Embed(color=0x000000)
            embed.add_field(name="현재 오목판", value=Board, inline=False)

        elif WINNER == OmokPlayer1:
            drawBoard()
            await ctx.send(OmokPlayer1.mention + "승리!!!")
            embed = discord.Embed(color=0x000000)
            embed.add_field(name="최종 오목판", value=Board, inline=False)

        elif WINNER == OmokPlayer2:
            drawBoard()
            await ctx.send(OmokPlayer2.mention + "승리!!!")
            embed = discord.Embed(color=0x000000)
            embed.add_field(name="최종 오목판", value=Board, inline=False)

        await ctx.send(embed=embed)

        if WINNER != None:
            endGame()

def setup(bot):
    bot.add_cog(Omok(bot))