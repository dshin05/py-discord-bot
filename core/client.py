import discord
import asyncio
import json
import asyncio
from .router import Router

modules = {}

class Client(discord.Client):
    def __init__(self):
        super().__init__()
        
        self.config = self.loadJson()
        
        self.prefix = self.config["commands"]["prefix"]
        self.nickname = self.config["client"]["nickname"]
        self.token = self.config["client"]["token"]

        self.router = Router(self, self.prefix)

        self.run(self.token)

    def loadJson(self):
        with open("config.json") as json_data:
            d = json.load(json_data)
            json_data.close
            return d

    """
    Register non-text related client modules
    """
    def register_modules(self):
        pass

    def run_modules(self):
        pass
    
    """
    Async wrapper
    """
    def run_async(self, callback):
        f = asyncio.run_coroutine_threadsafe(callback, self.loop)

        try:
            f.result()
        except Exception as e:
            print(e)

    """
    Bot ready event
    """
    def on_ready(self):
        print("bot is ready!")

    """
    New message event
    """
    async def on_message(self, message):
        if(message.author != self.user):
            self.router.route(message)
