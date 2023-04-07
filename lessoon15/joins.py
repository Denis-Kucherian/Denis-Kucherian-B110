import sqlite3


with sqlite3.connect('db.sqlite3') as con:
    cur = con.cursor()

    cur.execute("""
    SELECT city.name, carfactory.name
    FROM city, carfactory
    WHERE city.id = carfactory.city_id
    """)

    cur.execute("""
    SELECT city.name, carfactory.name
    FROM city
    LEFT OUTER JOIN city_shop
    ON city.id = city_shop.city_id
    LEFT OUTER JOIN shop
    ON city_shop.shop_id = shop.id
    """)


    con.commit()