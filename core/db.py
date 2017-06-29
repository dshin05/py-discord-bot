import sqlite3

class Database(sqlite3):
    
    def __init__(dbfile):
        self.dbfile = dbfile
        self.check_table()

    def check_table(self):
        pass
    
    def open(self):
        self.connect(self.dbfile)
