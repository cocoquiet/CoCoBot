import discord
import asyncio
from discord.ext.commands import Cog
from discord.commands import slash_command

from config import CoCoColor
from config import CoCoVER


musicList = None                    # 플레이 리스트 임베드

class Music(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def playlist(self, ctx):
        """기본으로 내장되어있는 플레이리스트를 보여줄게요."""
        
        global musicList

        musicListTitle =    {       # 플레이 리스트 제목
                                1: {
                                    0: '코양이 재생목록입니다.', 
                                    1: ':one: `코양이 아히사`', 
                                    2: ':two: `코양이 재즈`', 
                                    3: ':three: `코양이 로파이`', 
                                    4: ':four: `코양이 메이플`', 
                                    5: ':five: `코양이 피아노`', 
                                    6: ':six: `코양이 캐롤`', 
                                    7: ':seven: `코양이 팝`', 
                                    8: ':eight: `코양이 올드팝`'
                                    }, 

                                2: {
                                    0: '관리자들의 재생목록입니다.', 
                                    1: ':one: `루 뮤직 리스트`', 
                                    2: ':two: `루 뮤직 리스트2`', 
                                    3: ':three: `고수 개인 소장`', 
                                    4: ':four: `양사 오늘의 노래`'
                                    }, 

                                3: {
                                    0: '인기 가수들의 재생목록입니다.', 
                                    1: ':one: `아이유 리스트`', 
                                    2: ':two: `브루노 마스 리스트`',
                                    3: ':three: `방탄소년단 리스트`',
                                    }
                            }

        musicListLink =     {                                                                   # 리스트별 링크
                                1: {
                                    1: 'https://www.youtube.com/playlist?list=PLylf8Ved3tAFtRQRTgx78KcG2NPdnyzyP',  # 코양이 아히사
                                    2: 'https://www.youtube.com/playlist?list=PLylf8Ved3tAEGE_f0734AmuQyFWcY0r4T',  # 코양이 재즈
                                    3: 'https://www.youtube.com/playlist?list=PLylf8Ved3tAFktv4q2g8deFehMLSsUnJK',  # 코양이 로파이
                                    4: 'https://www.youtube.com/playlist?list=PLylf8Ved3tAEDzjsv-yuPCslGUXW1JFIG',  # 코양이 메이플
                                    5: 'https://youtube.com/playlist?list=PLylf8Ved3tAE4jbtyi8dg5MDF_zv_leLM',      # 코양이 피아노
                                    6: 'https://www.youtube.com/playlist?list=PLylf8Ved3tAFM2-5BpAhUJzQKjXd0i_Ta',  # 코양이 캐롤
                                    7: 'https://youtube.com/playlist?list=PLylf8Ved3tAF6Xhb_63e9tv3TBfmKB0wE',      # 코양이 팝
                                    8: 'https://www.youtube.com/playlist?list=PLylf8Ved3tAH2O8mPPgtHTX8Wx_bbkjDf'   # 코양이 올드팝
                                    }, 

                                2: {
                                    1: 'https://youtube.com/playlist?list=PLVW_htI5V49iz9Z38iaKOoS8JByghA0cb',      # 루 뮤직 리스트
                                    2: 'https://www.youtube.com/playlist?list=PLVW_htI5V49i9h4rCNvMl4fQh66HN2dyP',  # 루 뮤직 리스트2
                                    3: 'https://youtube.com/playlist?list=PL_Z2oxKB4fpa4zLdjaFX6ln2jX0t6ssmm',      # 고수 개인 소장
                                    4: 'https://www.youtube.com/playlist?list=PLFxP7Xv4aTr09edNKmWntSsvbtgooHDsj'   # 양사 오늘의 노래
                                    }, 

                                3: {
                                    1: 'https://youtube.com/playlist?list=PLylf8Ved3tAExS3iiNrr4FxCqCCpOASyw',      # 아이유 리스트
                                    2: 'https://youtube.com/playlist?list=PLylf8Ved3tAEFnjSzMGokFJlD0d25ZSua',      # 브루노 마스 리스트
                                    3: 'https://youtube.com/playlist?list=PLylf8Ved3tAEb9LVlk5wXlzzIo9orTGYb'       # 방탄소년단 리스트
                                    }
                            }

        musicListIndex = None       # 플레이 리스트 임베드 페이지값

        def setMusicList(index):    # 플레이 리스트 임베드 정의 함수
            global musicList

            musicList = discord.Embed(title='음악 재생목록', description=musicListTitle[index][0], color=CoCoColor)

            for link in range(1, len(musicListTitle[musicListIndex])):
                musicList.add_field(name=musicListTitle[musicListIndex][link], 
                                    value=musicListLink[musicListIndex][link], 
                                    inline=False)

            musicList.set_footer(text=f'페이지 {musicListIndex}/{len(musicListTitle)}\n' + CoCoVER)


        musicListIndex = 1

        setMusicList(musicListIndex)
        page = await ctx.respond(embed=musicList)

        reaction = None             # 이모지 반응

        await page.add_reaction('⏮')
        await page.add_reaction('◀')
        await page.add_reaction('▶')
        await page.add_reaction('⏭')

        def check(reaction, user):  # wait_for() 체크 함수
            return user == ctx.author

        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout = 300.0, check = check)
            except asyncio.TimeoutError:
                await page.clear_reactions()
                musicListIndex = None
                break
            else:
                if reaction.emoji == '⏮':
                    musicListIndex = 1
                elif reaction.emoji == '◀':
                    if musicListIndex > 1:
                        musicListIndex -= 1
                elif reaction.emoji == '▶':
                    if musicListIndex < len(musicListTitle):
                        musicListIndex += 1
                elif reaction.emoji == '⏭':
                    musicListIndex = len(musicListTitle)

                await page.remove_reaction(reaction, user)

                setMusicList(musicListIndex)
                await page.edit(embed = musicList)

def setup(bot):
    bot.add_cog(Music(bot))