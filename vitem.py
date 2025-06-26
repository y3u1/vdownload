import sqlite3
class vitem:
    def __init__(self,name, link, infoHash, size,date,category):
        self.name = name
        self.link = link
        self.infoHash = infoHash
        self.size = size
        self.date = date
        self.category = category  # Category is not used in the current implementation
    def save_to_db(self, db_path='data.db'):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                link TEXT,
                infoHash TEXT UNIQUE,
                size TEXT,
                date INTEGER,
                category TEXT
            )
        ''')
        cursor.execute('''
            INSERT INTO items (name, link, infoHash, size, date, category)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(infoHash) DO NOTHING
        '''
        , (self.name, self.link, self.infoHash, self.size, self.date, self.category))
        conn.commit()
        conn.close()
