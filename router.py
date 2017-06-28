import discord

import routes.simple_reply as simple_reply

def route(message, client):
    simple_reply.invoke(message, client)