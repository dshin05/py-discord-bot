from .router import Router
import re
import requests
import asyncio
import random
import threading


@Router.register_command("기억")
def _remember(self, args, message):

    toks = args.split(' ')

    if (len(toks) == 2):
        finish_event = threading.Event()

        self.client.db.db_queue.put((finish_event, lambda cur: cur.execute("INSERT INTO remember_tbl(key, value) VALUES (?, ?)", args[0], args[1])))

        finish_event.wait(5)

@Router.register_command("알려")
def _recall(self, args, message):

    toks = args.split(' ')

    if (len(toks) == 1):
        finish_event = threading.Event()

        # how do you get a value back from the db worker thread??? architecture needs major redesign
        self.client.db.db_queue.put((finish_event, lambda cur: cur.execute("SELECT * FROM remember_tbl WHERE key = ?", args[0])))

@Router.register_command("remembertest")
def _remembertest(self, args, message):
    self.client.db.wrapper_test()






