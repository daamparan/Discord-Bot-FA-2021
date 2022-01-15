import discord
from discord.ext import commands

from youtube_dl import YoutubeDL

class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        #  music related items
        self.is_playing = False
        
        #  queue array for music 
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        self.FFFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        
        #  voice channel hold for the music is is_playing
        self.vc = ''
    
    '''
    Sig: search_yt(self, item)
    Pre: True
    Post: Will find the item given as a url 
    '''
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info('ytsearch:%s' %item, download=False,)['entries'][0]
            except Exception:
                return False
        return {'source': info['formats'][0]['url'], 'title': info['title']}

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True
            
            #  get the first url
            m_url = self.music_queue[0][0]['source']
            
            #  remove the first element to play item
            self.music_queue.pop(0)
            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFFMPEG_OPTIONS), after=lambda e: self.play_next())
            
        else:
            self.is_playing = False
    
    async def play_music(self):
        if len(self.music_queue) > 0:
            self.is_playing = True
            
            m_url = self.music_queue[0][0]['source']
            
            #  try to connect to the voice channel if not connected
            if self.vc == '' or not not self.vc.is_connected(): 
                self.vc = await self.music_queue[0][1].connect()  # 1 stores the channel and joins it
            else:
                self.vc = await self.bot.move_to(self.music_queue[0][1])  # move if we are in another voice channel
            
            #  removes the first element to play item
            self.music_queue.pop(0)
            
            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
             self.is_playing = False
             
    @commands.command()
    async def play(self, ctx, *args):
        query = ' '.join(args)  # convert to string that we can pass as URL
        voice_channel = ctx.author.voice.channel
        
        if voice_channel is None:  # no connection to a voice channel
            await ctx.send('Join a channel before using this command')
        else:  #connected
            song = self.search_yt(query)  # using the search function
            if type(song) == type(True):
                await ctx.send('Could not download the song, incorrect format and try another keyword')
                
            else:
                await ctx.send('Song added to the Queue')
                self.music_queue.append([song, voice_channel])
                
                if self.is_playing == False:
                    await self.play_music()

    @commands.command()
    async def list(self, ctx):
        ret = ''
        for i in range(0, len(self.music_queue)):
            ret += self.music_queue[i][0]['title'] + '\n'
        if ret != '':
            await ctx.send(ret)
        else:
            await ctx.send('Queue is empty')
            
    @commands.command()
    async def skip(self, ctx):
        if self.vc != '':
            self.vc.stop()
            await ctx.send('Skipped')
            #  try to play the enxt 
            await self.play_music()
            
        