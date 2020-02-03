import sqlite3

"""Assignment 1 Questions."""

conn = sqlite3.connect('rpg_db.sqlite3')

conn.row_factory = sqlite3.Row

curs = conn.cursor()

# How many characters are there?

print('-'*80)
print("How many characters are there?\n")

query = """ SELECT name FROM charactercreator_character;"""
ans = curs.execute(query)
characters = len(ans.fetchall())
print(f'There are {characters} total characters. \n')

# How many of each specific subclass?

print('-'*80)
print("How many of each specific subclass? \n")

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

# How many total items?

print('-'*80)
print("How many total items?\n")

query = '''SELECT item_id FROM armory_item'''
qi = curs.execute(query)
items = len(qi.fetchall())

print(f'There are {items} items.')

# How many items are weapons? How many are not?

print('-'*80)
print("How many items are weapons? How many are not?\n")

query = '''SELECT item_ptr_id FROM armory_weapon'''
qw = curs.execute(query)
weaps = len(qw.fetchall())
non_weaps = items - weaps

print(f'There are {weaps} weapons.')
print(f'There are {non_weaps} non-weapons.')

# How many items does each character have?

print('-'*80)
print("How many items does each character have? (Return first 20 rows)")

query ='''SELECT character_id as `Character Id`,
COUNT(item_id) as `Item Count`
FROM charactercreator_character_inventory
GROUP BY character_id LIMIT 20 '''

# On average?

qic = curs.execute(query)
data = qic.fetchall()
df = pd.read_sql(query, data)
print(df)

# How many weapons does each character have?

print('-'*80)
print("How many weapons does each character have? (Return first 20 rows)")

# On average?
