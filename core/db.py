import sqlite3, threading, queue

class Database():

    def __init__(self, dbfile):
        self.dbfile = dbfile
        self.conn = sqlite3.connect(self.dbfile)
        self.check_table()
        self.db_queue = queue.Queue()

        t = threading.Thread(target = self.db_queue_worker)
        t.daemon = True
        t.start()

    def db_queue_worker(self):
        conn = sqlite3.connect(self.dbfile)
        while True:
            (finish_event, workrequest) = self.db_queue.get()
            cur = conn.cursor()
            workrequest(cur)
            finish_event.set()

    def check_table(self):
        c = self.conn.cursor()

        # create table for remember.py
        c.execute('CREATE TABLE IF NOT EXISTS remember_tbl (id INTEGER PRIMARY KEY, key text NOT NULL, value text NOT NULL)')

        self.conn.commit()


