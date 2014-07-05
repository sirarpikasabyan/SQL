import sqlite3

conn=sqlite3.connect("data.sqlite")
with conn:
    c=conn.cursor()
    #c.execute("select sqlite_version()")
    c.execute("drop table if exists friends")

    c.execute('''
    create table if not exists friends(
    id integer primary key,
    name text,
    age int
    )''')
    #c.execute("tables")


    c.execute('''
    insert into friends(name, age)
    values('Susik', 25)
    ''')

    c.execute('''
    insert into friends(name)
    values('Valod')
    ''')

    c.execute('''
    insert into friends(name, age)
    values(?, ?)''',
    ("Levon", 28))

    two_friends = [("Amy", 19),("Bill",23)]
    c.executemany('''
    insert into friends (name, age)
    values(?,?)''', two_friends)

    c.execute('''
    select * from friends''')
    data = c.fetchall()
    print (data)

conn.close()