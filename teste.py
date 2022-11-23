import discord
from dotenv import dotenv_values
TOKEN = dotenv_values()['TOKEN']
print(TOKEN)

intents = discord.Intents()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot looged in as {client.user}")

client.run(TOKEN)











""""#import youtube_dl

#voice_clients = {}

#yt_dl_opts = {'format': 'bestaudio/best'}
#ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

#ffmpeg_option = {'options': "-vn"}

#url = 'https://www.youtube.com/watch?v=cE-mBCBuxYQ'

#data = ytdl.extract_info(url, download=False)

#from youtubesearchpython import VideosSearch

#videosSearch = VideosSearch(query='6. Dfideliz - 66 (Clipe Oficial)', limit=1)

#print(videosSearch.result(mode=0))"""