import sqlite3
"""Assignment 1 Questions."""

conn = sqlite3.connect('rpg_db.sqlite3')

conn.row_factory = sqlite3.Row

curs = conn.cursor()

# How many of each specific subclass?

# cleric
query = '''SELECT character_ptr_id FROM charactercreator_cleric'''
q1 = curs.execute(query)
cleric = len(q1.fetchall())

print(f'There are {cleric} clerics.')

# fighters

query = '''SELECT character_ptr_id FROM charactercreator_fighter'''
q2 = curs.execute(query)
fighters = len(q2.fetchall())

print(f'There are {fighters} fighters.')

# necros

query = '''SELECT mage_ptr_id FROM charactercreator_necromancer'''
q3 = curs.execute(query)
necros = len(q3.fetchall())

print(f'There are {necros} necromancers.')

# mages

query = '''SELECT character_ptr_id FROM charactercreator_mage'''
q4 = curs.execute(query)
mages = len(q4.fetchall())

print(f'There are {mages} mages.')

# thief

query = '''SELECT character_ptr_id FROM charactercreator_thief'''
q5 = curs.execute(query)
thief = len(q5.fetchall())

print(f'There are {thief} thieves.')
