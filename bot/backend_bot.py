import os
import discord  # importing discord api 
from dotenv import load_dotenv

class BotDiscord:
    def __init__(self):
        self.TOKEN = None  # attributes needed for later
        self.GUILD = None 
        self.intents = None
        self.client = None