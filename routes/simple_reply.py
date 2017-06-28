import discord

def invoke(message, client):
    keyword = "!reply"

    if(message.content.startswith(keyword)):
        print(message.content)
        client.send_message(message.channel, message.content)