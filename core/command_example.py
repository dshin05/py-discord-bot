from .router import Router
import re
import requests
import asyncio
import random

@Router.register_command("test")
def _reply(self, args, message):
    channel = message.channel
    text = args
    self.client.run_async(self.client.send_message(channel, text))

@Router.register_command("선택")
def _choose(self, args, message):
    channel = message.channel
    arr = args.split(" ")
    pick = random.choice(arr)

    self.client.run_async(self.client.send_message(channel, pick))
