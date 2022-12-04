import discord
from dotenv import dotenv_values

def configIntents():

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

    return intents

def configToken():
    TOKEN = dotenv_values()['TOKEN']
    return TOKEN

def configClient():
    client = discord.Client(intents=configIntents())
    return client
