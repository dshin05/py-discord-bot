import discord
import asyncio
import json
import asyncio
from .router import Router

class Client(discord.Client):
    def __init__(self):
        super().__init__()
        
        self.config = self.loadJson()
        
        self.commandPrefix = self.config["commands"]["commandPrefix"]
        self.nickname = self.config["client"]["nickname"]
        self.token = self.config["client"]["token"]

        self.router = Router(self, self.commandPrefix)

        self.run(self.token)

    def loadJson(self):
        with open("config.json") as json_data:
            d = json.load(json_data)
            json_data.close
            return d
    
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
    async def on_ready(self):
        self.change_nickname(self.user.id, self.nickname)
        print("bot is ready!")

    async def on_message(self, message):
        if(message.author != self.user):
            self.router.route(message)

    