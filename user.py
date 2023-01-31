import sqlite3

conn = sqlite3.connect('user.db')

c = conn.cursor()

c.execute("""CREATE TABLE customers (
        first_name text,
        last_name text,
        email text,
        password text
    )""")

# c.execute("INSERT INTO user VALUES ('Antony', 'Yu', 'antony@gmail.com', 1234'")

# print("committed")

# conn.commit()

# conn.close()

