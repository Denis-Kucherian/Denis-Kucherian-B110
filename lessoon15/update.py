import sqlite3


with sqlite3.connect('db.sqlite3') as con:
    cur = con.cursor()

    # cur.execute('''
    # UPDATE city
    # SET name = 'Привет';
    # ''')

    cur.execute('''
    UPDATE city set name = 'Казань' WHERE id = 4;
    ''')

    cur.execute('''
    SELECT name
    FROM city;
    ''')

    for i in cur:
        print(i)
