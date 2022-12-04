import youtube_dl
import asyncio
import discord

ydl_options = {
    'format': 'bestaudio',
    'noplaylist': 'true',
}
ytdl = youtube_dl.YoutubeDL(ydl_options)

ffmpeg_options = {
   'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
   'options': '-vn' 
}

class youtube_music:
    async def play_url(url):

        try:

            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

            player = discord.FFmpegPCMAudio(data['url'], **ffmpeg_options)

        except Exception as err:
            print(err)

        return player

    async def play_search_music(music):
        with youtube_dl.YoutubeDL(ydl_options) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % music, download=False)['entries'][0]
                player = discord.FFmpegPCMAudio(info['url'], **ffmpeg_options)

            except Exception as err:
                print(err)

        return player
