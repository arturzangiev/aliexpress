import sqlite3

sqlite_file = 'aliexpress_db.sqlite'
# table_name = 'my_table_2'
# id_column = 'my_1st_column'
# column_name = 'my_2nd_column'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


c.execute('insert into products (name, orders, url) VALUES ("test1", "test2", "test2")')

# B) Tries to insert an ID (if it does not exist yet)
# with a specific value in a second column
# c.execute("INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".format(tn=table_name, idf=id_column, cn=column_name))

conn.commit()
conn.close()