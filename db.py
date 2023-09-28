import sqlite3


class DB:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('contacts.sqlite')
        self.cur = self.conn.cursor()

    def execute(self, query, params=()):
        self.cur.execute(query, params)
        self.conn.commit()
        if not self.cur.description:
            return
        columns = [column[0] for column in self.cur.description]
        rows = self.cur.fetchall()
        result = [dict(zip(columns, row)) for row in rows]
        return result
    
    def __del__(self):
        self.cur.close()

