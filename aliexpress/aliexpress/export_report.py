import sqlite3
import csv

sqlite_file = 'aliexpress_db.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


query = '''SELECT
  present_table.name,
  past_table.orders,
  present_table.orders,
  present_table.orders - past_table.orders AS dif,
  present_table.url,
  past_table.Timestamp,
  present_table.Timestamp
FROM
  (SELECT * FROM products WHERE DATE(Timestamp)="2018-02-23") as past_table
JOIN
  (SELECT * FROM products WHERE DATE(Timestamp)="2018-02-24") as present_table
ON
  past_table.name = present_table.name
GROUP BY
  present_table.name
ORDER BY dif DESC'''

c.execute(query)

with open("out.csv", "w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in c.description])
    csv_writer.writerows(c)

conn.close()