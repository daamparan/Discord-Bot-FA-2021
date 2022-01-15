# PGMusicBot

## Introduction
Serves as a personal Discord bot created for the purpose of listening to music while in a voice channel. 
Can play either a link given or the name of the audio/video you would like to listen to. 
Is not for monetary use or purposes. 
All commands must be contain the pre-fix "!" 
Ex. 
!play [enter song/link]

## Installation
'Two major components will be needed for this bot to work properly' 

* youtube_dl
youtube_dl will be the library which will allow you to search your query from youtube. 
From here, it will attain it and play it back once it is found. youtube_dl only offers functions 
to complete the search not to fully implement the search and play functionality. 

* FFmpeg 
Allows for the recording and play back opf the audio that you will be selecting via your query. 
FFmpeg will directly output the audio via the bot and be heard within your channel (if joined). Furthermore, 
installion can be performed in one of two ways. 
Using the commad: 'pip install ffmpeg' or going to ffmpeg and downloading its latest compatible
version with your system. 

Link: 'https://ffmpeg.org/' 


## Commands and Usage
Commands are broken down into two sepereate cog python files; cog being a collection of commands. 
###### * music_Cog.py

Holds all commands related to the music portion of the bot. For example, the play command: '!play [name]'

**!play**

Please enter the arguements as a link or the name of the audio you would like to listen to.
Keep in mind, the bot will select the first item matching the query you give, thus try to include 
as much detail of the audio, for example artist name and song name. 

**!list**

List command requires no arguements and allows you to list all the items that are pending to be played 
within the Queue. If nothing is pending the message will be given as such. 

**!skip**

Skip commands requires no arguements and allows us to skip the current song and play the next song, if any. If nothing is present it will simply
stop the audio playback. 

##### * general_Cog.py

Holds all genereal commands, such as joining a voice channel and leaving.

**!join**

Requires no arguments and will allow the bot to join the voice channel where the author
is in. If no voice channel is found then an error will be issued to the user(s). 

**!leave**

Requires no arguments and will allow the bot to leave the voice channel where the author is in. 
If not voice channel is found then an error will be issued to the user(s) 