import discord
from config import *
from commands.voice_channel import discordChannel

client = configClient()

@client.event
async def on_message(message):
    if(message.content.startswith("!play")):
        await discordChannel.join(message)


if __name__ == "__main__":
    client.run(configToken())