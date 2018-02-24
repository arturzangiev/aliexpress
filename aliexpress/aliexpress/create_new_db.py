import sqlite3
sqlite_file = 'aliexpress_db.sqlite'    # name of the sqlite database file

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('CREATE TABLE products (name VARCHAR, orders VARCHAR, url VARCHAR, Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)')

conn.commit()
conn.close()