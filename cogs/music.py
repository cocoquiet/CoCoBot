import discord
import asyncio
from discord.ext import commands

from config import CoCo_VER

import youtube_dl


musicList = None

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']

def load_opus_lib():
    if discord.opus.is_loaded():
        return True

    for opus_lib in OPUS_LIBS:
        try:
            discord.opus.load_opus(opus_lib)
            return
        except OSError:
            pass
        

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="play", aliases=["p", "ㅔ"])
    async def play(self, ctx, *, url):
        load_opus_lib()
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send('다음 곡 : {}'.format(player.title))

    @commands.command(name="stop", aliases=["st", "ㄴㅅ", "disconnect", "dc", "ㅇㅊ"])
    async def stop(self, ctx):
        await ctx.voice_client.disconnect()
    
    @commands.command(name="volume", aliases=["vol"])
    async def volume(self, ctx, volume : int):
        if ctx.voice_client is None:
            return await ctx.send("음성 채팅방을 들어오고 말해ㅡㅡ")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send("볼륨이 {}%로 설정되었습니다!".format(volume))

    @commands.command(name="음악목록", aliases=["음목", "playlist", "pl", "ㅔㅣ"])
    async def playlist(self, ctx, seq : int = None):
        global musicList

        musicListTitle =    {
                                1: {
                                    0: "코양이 재생목록입니다.", 
                                    1: ":one: `코양이 노동요`", 
                                    2: ":two: `코양이 재즈`", 
                                    3: ":three: `코양이 피아노`", 
                                    4: ":four: `코양이 캐롤`", 
                                    5: ":five: `코양이 힙합`", 
                                    6: ":six: `코양이 팝`", 
                                    7: ":seven: `코양이 올드팝`"
                                    }, 

                                2: {
                                    0: "관리자들의 재생목록입니다.", 
                                    1: ":one: `루 뮤직 리스트`", 
                                    2: ":two: `고수 개인 소장`", 
                                    3: ":three: `양사 오늘의 노래`"
                                    }
                            }

        musicListLink =     {
                                1: {
                                    1: "https://www.youtube.com/playlist?list=PLylf8Ved3tAFtRQRTgx78KcG2NPdnyzyP",  # 코양이 노동요
                                    2: "https://www.youtube.com/playlist?list=PLylf8Ved3tAEGE_f0734AmuQyFWcY0r4T",  # 코양이 재즈
                                    3: "https://youtube.com/playlist?list=PLylf8Ved3tAE4jbtyi8dg5MDF_zv_leLM",      # 코양이 피아노
                                    4: "https://www.youtube.com/playlist?list=PLylf8Ved3tAFM2-5BpAhUJzQKjXd0i_Ta",  # 코양이 캐롤
                                    5: "https://www.youtube.com/playlist?list=PLylf8Ved3tAHdLCjFZJJsLAHkjj8yX6J8",  # 코양이 힙합
                                    6: "https://youtube.com/playlist?list=PLylf8Ved3tAF6Xhb_63e9tv3TBfmKB0wE",      # 코양이 팝
                                    7: "https://www.youtube.com/playlist?list=PLylf8Ved3tAH2O8mPPgtHTX8Wx_bbkjDf"   # 코양이 올드팝
                                    }, 

                                2: {
                                    1: "https://youtube.com/playlist?list=PLVW_htI5V49iz9Z38iaKOoS8JByghA0cb",      # 루 뮤직 리스트
                                    2: "https://youtube.com/playlist?list=PL_Z2oxKB4fpa4zLdjaFX6ln2jX0t6ssmm",      # 고수 개인 소장
                                    3: "https://www.youtube.com/playlist?list=PLFxP7Xv4aTr09edNKmWntSsvbtgooHDsj"   # 양사 오늘의 노래
                                    }
                            }

        musicListIndex = None

        def setMusicList(index):
            global musicList

            musicList = discord.Embed(title="음악 재생목록", description=musicListTitle[index][0], color=0xFFFFFE)

            for link in range(1, len(musicListTitle[musicListIndex])):
                musicList.add_field(name=musicListTitle[musicListIndex][link], 
                                value=musicListLink[musicListIndex][link], 
                                inline=False)

            musicList.set_footer(text=f"페이지 {musicListIndex}/{len(musicListTitle)}\n" + CoCo_VER)


        if seq == None:
            musicListIndex = 1

            setMusicList(musicListIndex)
            page = await ctx.send(embed=musicList)

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
                    break
                    page.clear_reactions()
                    musicListIndex = None
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

        else:
            if musicListIndex != None:
                async with ctx.typing():
                    player = await YTDLSource.from_url(musicListLink[musicListIndex][seq], loop=self.bot.loop, stream=True)
                    ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

                await ctx.send('다음 곡 : {}'.format(player.title))
            else:
                await ctx.send("`/playlist` 명령어로 먼저 음악 리스트를 열어주세요.")

    @play.before_invoke
    @playlist.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("음성 채팅방을 들어오고 말해ㅡㅡ")
                raise commands.CommandError("음성 채팅방을 들어오고 말해ㅡㅡ")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

def setup(bot):
    bot.add_cog(Music(bot))