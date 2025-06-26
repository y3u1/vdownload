import sqlite3


class Sqlquery:
    def __init__(self, db_path='data.db'):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def close(self):
        self.conn.close()
    def query_before(self,time):
        self.cursor.execute(f'''
            SELECT id, name, date 
            FROM items
            ORDER BY date DESC
            WHERE ? <= date
        ''', (time))
        self.conn.commit()
        return self.cursor.fetchall()