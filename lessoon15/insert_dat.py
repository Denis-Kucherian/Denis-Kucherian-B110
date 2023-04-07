import sqlite3


with sqlite3.connect('db.sqlite3') as con:
    cur = con.cursor()

    cur.execute('''
    INSERT INTO city(name)
    VALUES ('Тольятти');
    ''')

    # for i in range(3):
    #     city = input("Введите город:")
    #     cur.execute(
    #         'INSERT INTO city(name) VALUES(?);',
    #         (city, )
    #     )

    # cities = [
    #     ("Санкт-Петербург", ),
    #     ("Нижний Новгород", ),
    #     ("Ярославль", )
    # ]
    #
    # cur.executemany('INSERT INTO city(name) VALUES(?);', cities)

    con.commit()
