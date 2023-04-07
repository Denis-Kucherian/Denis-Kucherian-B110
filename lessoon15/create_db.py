import sqlite3


with sqlite3.connect('db.sqlite3') as con:
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS city(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT(20) UNIQUE
    );
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS avtosalon (
        id INTEGER PRIMARY KEY,
        name TEXT,
        city_id INTEGER NOT NULL UNIQUE,
        rating INTEGER NOT NULL,
        FOREIGN KEY(city_id) REFERENCES city(id)
    );
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS avtobrand (
            id INTEGER PRIMARY KEY,
            name TEXT
        );
        ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS avtosalon_avtobrand (
            avtosalon_id INTEGER NOT NULL,
            avtobrand_id INTEGER NOT NULL,
            PRIMARY KEY (avtosalon_id, avtobrand_id),
            FOREIGN KEY(avtosalon_id) REFERENCES avtosalon(id),
            FOREIGN KEY(avtobrand_id) REFERENCES avtobrand(id)
        );
        ''')


    cur.execute('''
        SELECT * FROM city;
    ''')

    for i in cur:
        print(i)

    con.commit()
