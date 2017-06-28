import discord
from collections import namedtuple
from configparser import ConfigParser
from os import path
import sys
import re
import asyncio
from threading import Thread

Command = namedtuple('Command', ['name', 'arg_func', 'aliases'])

class Router():
    aliases = {}
    commands = {}
    
    def __init__(self, client, commandPrefix):
        self.client = client
        self.commandPrefix = commandPrefix;

    """
    Route message from client's on_message()
    """
    def route(self, message):
        # text command
        if(message.content.startswith(self.commandPrefix)):
            self.run_command(message)

        # TODO: reactions to images and files..
    
    """
    Runs a text command
    """
    def run_command(self, message):
        cmd_name, *args = message.content.split(' ')
        cmd_name = cmd_name[1:]
        args = ' '.join(args).strip()

        if cmd_name in self.aliases:
            cmd = self.commands[self.aliases[cmd_name]]
            args = cmd.arg_func(args)
            # start command as a new thread
            Thread(target=getattr(self, cmd.name),
                   args=(args, message)).start()

    """
    Register routes from routes.py
    """
    @classmethod
    def register_command(cls, name, aliases=None, arg_func=lambda args: args):
        if aliases is None:
            aliases = []
        aliases.append(name)

        def wrapper(func):
            func_name = '_cmd_' + func.__name__
            while func_name in cls.commands:
                func_name += '_'

            setattr(cls, func_name, func)
            cls.commands[func_name] = Command(func_name, arg_func, aliases)
            # associate the given aliases with the command
            for alias in aliases:
                if alias in cls.aliases:
                    print('The alias "{}"'.format(alias),
                          'is already in use for command',
                          cls.aliases[alias][:5].strip('_'))
                    sys.exit(-1)

                cls.aliases[alias] = func_name

        return wrapper
