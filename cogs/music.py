import discord
import asyncio
from discord.ext.commands import Cog
from discord.commands import slash_command
from discord.ui import Select, View

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
                                '코코조용 리스트': {
                                    0: '코코조용 재생목록입니다.', 
                                    1: ':one: `코코조용 아히사`', 
                                    2: ':two: `코코조용 재즈`', 
                                    3: ':three: `코코조용 로파이`', 
                                    4: ':four: `코코조용 메이플`', 
                                    5: ':five: `코코조용 피아노`', 
                                    6: ':six: `코코조용 캐롤`', 
                                    7: ':seven: `코코조용 팝`', 
                                    8: ':eight: `코코조용 올드팝`'
                                    }, 

                                '관리자 리스트': {
                                    0: '관리자들의 재생목록입니다.', 
                                    1: ':one: `루 뮤직 리스트`', 
                                    2: ':two: `루 뮤직 리스트2`', 
                                    3: ':three: `고수 개인 소장`', 
                                    4: ':four: `양사 오늘의 노래`'
                                    }, 

                                '아티스트 리스트': {
                                    0: '인기 가수들의 재생목록입니다.', 
                                    1: ':one: `아이유 리스트`', 
                                    2: ':two: `브루노 마스 리스트`',
                                    3: ':three: `방탄소년단 리스트`',
                                    }
                            }

        musicListLink =     {                                                                   # 리스트별 링크
                                '코코조용 리스트': {
                                    1: 'https://www.youtube.com/playlist?list=PLylf8Ved3tAFtRQRTgx78KcG2NPdnyzyP',  # 코코조용 아히사
                                    2: 'https://www.youtube.com/playlist?list=PLylf8Ved3tAEGE_f0734AmuQyFWcY0r4T',  # 코코조용 재즈
                                    3: 'https://www.youtube.com/playlist?list=PLylf8Ved3tAFktv4q2g8deFehMLSsUnJK',  # 코코조용 로파이
                                    4: 'https://www.youtube.com/playlist?list=PLylf8Ved3tAEDzjsv-yuPCslGUXW1JFIG',  # 코코조용 메이플
                                    5: 'https://youtube.com/playlist?list=PLylf8Ved3tAE4jbtyi8dg5MDF_zv_leLM',      # 코코조용 피아노
                                    6: 'https://www.youtube.com/playlist?list=PLylf8Ved3tAFM2-5BpAhUJzQKjXd0i_Ta',  # 코코조용 캐롤
                                    7: 'https://youtube.com/playlist?list=PLylf8Ved3tAF6Xhb_63e9tv3TBfmKB0wE',      # 코코조용 팝
                                    8: 'https://www.youtube.com/playlist?list=PLylf8Ved3tAH2O8mPPgtHTX8Wx_bbkjDf'   # 코코조용 올드팝
                                    }, 

                                '관리자 리스트': {
                                    1: 'https://youtube.com/playlist?list=PLVW_htI5V49iz9Z38iaKOoS8JByghA0cb',      # 루 뮤직 리스트
                                    2: 'https://www.youtube.com/playlist?list=PLVW_htI5V49i9h4rCNvMl4fQh66HN2dyP',  # 루 뮤직 리스트2
                                    3: 'https://youtube.com/playlist?list=PL_Z2oxKB4fpa4zLdjaFX6ln2jX0t6ssmm',      # 고수 개인 소장
                                    4: 'https://www.youtube.com/playlist?list=PLFxP7Xv4aTr09edNKmWntSsvbtgooHDsj'   # 양사 오늘의 노래
                                    }, 

                                '아티스트 리스트': {
                                    1: 'https://youtube.com/playlist?list=PLylf8Ved3tAExS3iiNrr4FxCqCCpOASyw',      # 아이유 리스트
                                    2: 'https://youtube.com/playlist?list=PLylf8Ved3tAEFnjSzMGokFJlD0d25ZSua',      # 브루노 마스 리스트
                                    3: 'https://youtube.com/playlist?list=PLylf8Ved3tAEb9LVlk5wXlzzIo9orTGYb'       # 방탄소년단 리스트
                                    }
                            }

        def setMusicList(category):    # 플레이 리스트 임베드 정의 함수
            global musicList

            musicList = discord.Embed(title='음악 재생목록', description=musicListTitle[category][0], color=CoCoColor)

            for link in range(1, len(musicListTitle[category])):
                musicList.add_field(name=musicListTitle[category][link], 
                                    value=musicListLink[category][link], 
                                    inline=False)

            musicList.set_footer(text=CoCoVER)

        setMusicList('코코조용 리스트')
        
        view = View()
        category = Select(
            placeholder='카테고리를 선택하세요.', 
            options=[ 
            discord.SelectOption(label='코코조용 리스트', description='코코조용 재생목록입니다.'), 
            discord.SelectOption(label='관리자 리스트', description='관리자들의 재생목록입니다.'), 
            discord.SelectOption(label='아티스트 리스트', description='인기 가수들의 재생목록입니다.')
        ])
        
        async def category_callback(interaction):
            setMusicList(category.values[0])
            await interaction.response.edit_message(embed=musicList, view=view)
            
        category.callback = category_callback
        
        view.add_item(category)
        
        await ctx.respond(embed=musicList, view=view)

def setup(bot):
    bot.add_cog(Music(bot))