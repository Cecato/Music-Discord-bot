import discord
from dotenv import dotenv_values

TOKEN = dotenv_values(".env")['TOKEN']

class login:
    intents = discord.Intents()
    client = discord.Client(intents=intents)
    
    client.run(TOKEN)