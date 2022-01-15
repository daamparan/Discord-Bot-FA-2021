import discord # access all API calls for discord
from dotenv import load_dotenv
from music_Cog import music_cog
from general_Cog import general_cog
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')   #Authentication token for the bot 
GUILD = os.getenv('DISCORD_GUILD')   #Authentication used for the server | server name

intents = discord.Intents.all() #enable intents
intents.members = True

Bot = discord.ext.commands.Bot(command_prefix='!')   #create with the intents
Bot.add_cog(music_cog(Bot))
Bot.add_cog(general_cog(Bot))


# general disconnection commands
@Bot.event
async def on_voice_state_update(member, before, after):
    state_voice = member.guild.voice_client  # get the member of the channel
    if state_voice is not None and len(state_voice.channel.members) == 1:
        await state_voice.disconnect()
        
        
        
if __name__ == '__main__':    
    Bot.run(TOKEN)