import discord
import os
import asyncio
import youtube_dl
from dotenv import dotenv_values

TOKEN = dotenv_values()['TOKEN']

intents = discord.Intents()
intents.members = True
intents.reactions = True
intents.typing = True
intents.presences = True
intents.messages = True
intents.message_content = True
intents.guild_messages = True
intents.guilds = True
intents.guild_typing = True
intents.voice_states = True


client = discord.Client(intents=intents)

voice_clients = {}

yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_option = {'options': "-vn"}

@client.event
async def on_ready():
    print(f"Bot looged in as {client.user}")


@client.event
async def on_message(message):

    msg = message.content

    if(msg.startswith("tocar")):
        try:
            voice_client = await message.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client
        except:
            print("error")
        
        try:
            url = msg.split()[1]

            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
            song = data['url']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_option)

            voice_client.play(player)

        except Exception as err:
            print(err)

        

client.run(TOKEN)