import sqlite3


with sqlite3.connect('db.sqlite3') as con:
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS city(
        id INTEGER PRIMARY KEY,
        name TEXT(30) NOT NULL UNIQUE
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS shop(
        id INTEGER PRIMARY KEY,
        name TEXT(50) NOT NULL UNIQUE
    );
    """)


    cur.execute("""
    CREATE TABLE IF NOT EXISTS city_shop(
        city_id INTEGER NOT NULL,
        shop_id INTEGER NOT NULL,
        address TEXT,
        PRIMARY KEY (city_id, address),
        FOREIGN KEY(city_id) REFERENCES city(id),
        FOREIGN KEY(shop_id) REFERENCES shop(id)
    );
    """)


    cur.execute("""
    CREATE TABLE IF NOT EXISTS carfactory(
        id INTEGER PRIMARY KEY,
        name TEXT(50) NOT NULL UNIQUE,
        city_id INTEGER NOT NULL,
        FOREIGN KEY(city_id) REFERENCES city(id)
    );
    """)

    con.commit()