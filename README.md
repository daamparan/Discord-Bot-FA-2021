# Discord Bot FA 2021
## Discord Bot Side Project 

Discord Bot will be responsible for greeting and generating custom messages to each server member of 
server be it an annoucement by the owner or important members. Its responsibilities may evolve as well and 
this repo will be updated with all of those changes. So far this bot is private to myself only.

## File Descriptions
### bot.py 
This python file holds the main components which creates the client session for the bot and give it 
commands from there on out. API used includes os, discord, and dotenv which must be installed onto the 
conda base enviorment if not installed of course. The intial step is to aquire your bot token from the .env
file which must be created by you within the same directory of bot.python. From there we define an async method which 
runs at the time of an event occuring within the Client connection. 

### .env
The .env file will be a user created text file with the Discord Token for the bot which can be found in the 
Discord Development page after the creation of the Discord Bot.


