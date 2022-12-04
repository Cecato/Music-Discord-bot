from config import *
from commands.youtube_play import youtube_music

ytb = "https://www.youtube.com/watch?"

class discordChannel:
    
    async def join(message):
        
        try:
            voice_client = await message.author.voice.channel.connect()

        except Exception as err:
            print(err)

        msg = (message.content).split()[1]

        if( msg.startswith(ytb)):
            try:
                voice_client.play( await youtube_music.play_url(msg) )

            except Exception as err:
                print(err)
        
        else:
            musicTitle = message.content.replace("!play", '')
            info = await youtube_music.play_search_music(musicTitle)

            voice_client.play(info)
            

