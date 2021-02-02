import discord
import asyncio
from discord.ext import commands
from config import CoCo_VER

import youtube_dl

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
        load_opus_lib()
        link = ["", 
                "https://www.youtube.com/playlist?list=PLylf8Ved3tAFtRQRTgx78KcG2NPdnyzyP", 
                "https://www.youtube.com/playlist?list=PLylf8Ved3tAEGE_f0734AmuQyFWcY0r4T", 
                "https://www.youtube.com/playlist?list=PLylf8Ved3tAFM2-5BpAhUJzQKjXd0i_Ta", 
                "https://www.youtube.com/playlist?list=PLylf8Ved3tAHdLCjFZJJsLAHkjj8yX6J8", 
                "https://youtube.com/playlist?list=PLylf8Ved3tAF6Xhb_63e9tv3TBfmKB0wE", 
                "https://www.youtube.com/playlist?list=PLylf8Ved3tAH2O8mPPgtHTX8Wx_bbkjDf", 
                "https://youtube.com/playlist?list=PLVW_htI5V49iz9Z38iaKOoS8JByghA0cb",
                "https://www.youtube.com/playlist?list=PLFxP7Xv4aTr09edNKmWntSsvbtgooHDsj"]

        if seq == None:
            embed = discord.Embed(title="코양이 유튜브 재생목록", description="유튜브 재생목록 모음입니다.", color=0xffffff)
            embed.add_field(name=":one: `코양이 노동요`", value=link[1], inline=False)
            embed.add_field(name=":two: `코양이 재즈`", value=link[2], inline=False)
            embed.add_field(name=":three: `코양이 캐롤`", value=link[3], inline=False)
            embed.add_field(name=":four: `코양이 힙합`", value=link[4], inline=False)
            embed.add_field(name=":five: `코양이 팝`", value=link[5], inline=False)
            embed.add_field(name=":six: `코양이 올드팝`", value=link[6], inline=False)
            embed.add_field(name=":seven: `루 뮤직 리스트`", value=link[7], inline=False)
            embed.add_field(name=":eight: `오늘의 노래`", value=link[8], inline=False)
            embed.set_footer(text=CoCo_VER)
            
            return await ctx.send(embed=embed)
        else:
            async with ctx.typing():
                player = await YTDLSource.from_url(link[seq], loop=self.bot.loop, stream=True)
                ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

            await ctx.send('다음 곡 : {}'.format(player.title))

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