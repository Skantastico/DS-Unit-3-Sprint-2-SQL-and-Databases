"""
PART 1 - Making and Populating a Database
"""

import sqlite3

print('Part 1: Making and Populating a Database')
print('-'*80)

# Give database a name

db_name = 'demo_data.sqlite3'

# Try connecting

conn = sqlite3.connect(db_name)
curs = conn.cursor()

# Create the Table and Insert Data

curs.execute("""CREATE TABLE demo(
    s CHAR(1) PRIMARY KEY,
    x INT NOT NULL,
    y INT NOT NULL
    );""")

curs.execute("""INSERT INTO demo (s,x,y) VALUES ('g', 3, 9);""")
curs.execute("""INSERT INTO demo (s,x,y) VALUES ('v', 5, 7);""")
curs.execute("""INSERT INTO demo (s,x,y) VALUES ('f', 8, 7);""")

# Answer questions

# Count number of Rows

curs.execute("""SELECT COUNT(*) FROM demo;""")
print('Number of Rows:')
print(curs.fetchall())

# Minimum 5 in x and y

curs.execute("""SELECT COUNT(*) FROM demo
             WHERE x >= 5 and y >= 5;""")
print('Rows where x and y are 5 or greater:')
print(curs.fetchall())

# unique values of y

curs.execute("""SELECT COUNT(DISTINCT y) FROM demo""")
print("Unique values of y:")
print(curs.fetchall())
