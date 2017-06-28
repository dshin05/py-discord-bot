import discord
import asyncio
import json
import router


"""
Server class
"""

client = discord.Client()
config = []

def main():
    config = _loadJson()
    client.run(config["token"])

def _loadJson():
    with open("config.json") as json_data:
        d = json.load(json_data)
        json_data.close
        return d

@client.event
async def on_ready():
    print("Succesfully started server")
    print("User : " + client.user.name)
    print("ID: " + client.user.id)

@client.event
async def on_message(message):
    if(message.content.startswith("!")):
        router.route(message, client)

main()