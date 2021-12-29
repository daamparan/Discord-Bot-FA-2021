import os
import discord # access all API calls for discord
from discord.ext import commands 
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')   #Authentication token for the bot 
GUILD = os.getenv('DISCORD_GUILD')   #Authentication used for the server | server name

intents = discord.Intents.all() #enable intents
intents.members = True
client = discord.ext.commands.Bot(command_prefix='!')   #create with the intents

@client.event
async def on_ready():  # will track the connection event; once ran it is ready for further processing
    for guild in client.guilds:  # go thorugh the servers bots are added for
        if guild.name == GUILD:  # once it matches with one of the servers in .env 
            break
    print(f'\n{client.user} has connected to Discord!')
    print(f'{guild.name}(id: {guild.id})')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

connected = False  # used to identifiy the connection to voice channel

@client.command(name='join')
async def join(ctx):
    connected = ctx.author.voice  # attains the members and the channel they are connected to
    if not connected:  # if we are not connected WHO EVER IS CALLING THE COMMAND
        await ctx.send('You need to connect to a voice channel to use this command')
        return
    await connected.channel.connect()  # join the voice channel

@client.command(name='leave')
async def leave(ctx):
    server = ctx.message.guild.voice_client  # attain the voice channel in the server and disconnect from it
    await server.disconnect()
    
@client.command(name='play')
async def play(ctx):
    connected = ctx.author.voice  # member who has called commmand
    if not connected:
        await ctx.send('You need to connect to a voice channel to use this command')
    else:
        await ctx.send(ctx.message.content.replace('!play', ''))

@client.event
async def on_voice_state_update(member, before, after):
    state_voice = member.guild.voice_client # get the member of the channel
    if state_voice is not None and len(state_voice.channel.members) == 1:
        await state_voice.disconnect()

    

        
client.run(TOKEN)