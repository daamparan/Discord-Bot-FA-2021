import discord
import youtube_dl

youtube_dl.utils.bug_reports_message = lambda: ''

class YTDLSource(discord.PCMVolumeTRansformer):
    def __init__(self,source, *, data, volume = 0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')
    
    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))