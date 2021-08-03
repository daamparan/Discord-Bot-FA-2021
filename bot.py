import os
import discord #access all API calls for discord 
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD TOKEN') #Authentication token for the server

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)