import os
import discord #access all API calls for discord 
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #Authentication token for the bot 
GUILD = os.getenv('DISCORD_GUILD') #Authentication used for the server | server name

intents = discord.Intents.all() #enable intents
intents.members = True
client = discord.Client(intents=intents) #create with the intents

@client.event
async def on_ready(): #will track the connection event; once ran it is ready for further processing
    for guild in client.guilds: #go thorugh the servers bots are added for
        if guild.name == GUILD: #once it matches with one of the servers in .env 
            break
    print(f'\n{client.user} has connected to Discord!')
    print(f'{guild.name}(id: {guild.id})')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


client.run(TOKEN)