import sqlite3



def query_before(time):
    q = f'''
    SELECT id, name, date 
    FROM items
    WHERE {{time}} <= date
    '''
