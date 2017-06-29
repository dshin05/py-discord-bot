from .router import Router
import re
import requests
import asyncio
import random


@Router.register_command("기억")
def _remember(self, args, message):

    c = self.client.db.conn.cursor()

    if (len(args) == 2):
        c.execute("INSERT INTO remember_tbl(key, value) VALUES (?, ?)", args[1], args[2])

        print("Insert successful")

@Router.register_command("remembertest")
def _remembertest(self, args, message):
    c = self.db.cursor()


    for row in c.execute('SELECT * FROM q1_person_name'):
        print(row)




