from .router import Router
import re
import requests
import asyncio

@Router.register_command("test")
async def _reply(self, args, message):
    # TODO: not working
    await self.client.send_message(message.channel, 'asdf')
    print("reply function called")
