from discord.ext import commands


class general_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vc = ''  # holds the voice channel we joins
    
    @commands.command(name='join', help='Join a voice channel')
    async def join(self, ctx):
        connected = ctx.author.voice
        if not connected:
            await ctx.send('Connect to a voice channel to use this command')
            return
        else:
            self.vc = connected
            await connected.channel.connect()
            
    @commands.command(name='leave', help='Leave a voice channel')
    async def leave(self, ctx):
        connected = ctx.author.voice
        if not connected:
            await ctx.send('Connect to a voice channel to use this command')
        else:
            await connected.disconnect()