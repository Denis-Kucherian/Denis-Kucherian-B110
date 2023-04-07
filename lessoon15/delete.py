import sqlite3


with sqlite3.connect('db.sqlite3') as con:
    cur = con.cursor()

    cur.execute('''
    DELETE FROM city;
    ''')
