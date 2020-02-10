"""
Part 2 - The Northwind Database
"""

import sqlite3

# Establish connection
db_name = 'northwind_small.sqlite3'

conn = sqlite3.connect(db_name)
curs = conn.cursor()

# Answering Questions

print("Part 2 \n")

# What are the 10 most expensive items?

print('What are the ten most expensive items?\n')

ten_most = curs.execute("""
SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
;""").fetchall()
print(f'The ten most expensive items are: {list(ten_most)}')
print('-'*80)

# What is the average age of an employee at time of hiring?

print("What is the average age of an employee at time of hiring?\n")

avg_age = curs.execute("""
SELECT AVG(HireDate - BirthDate)
FROM Employee
;""").fetchall()
print(f'The average age at time of hiring is {list(avg_age)}')
print('-'*80)

# (Stretch) What is average age of employee by city?

print("What is average age of employee by city?\n")

avg_age_cty = curs.execute("""
SELECT City, AVG(HireDate - BirthDate) as Age
FROM Employee
GROUP BY City
ORDER BY Age
;""").fetchall()

print(f'Average age of employee by city: {list(avg_age_cty)}')
print('-'*80)

# Part 3 - Sailing the Northwind Seas

print("Part 3\n")

# What are the ten most expensive items AND their suppliers?

print("What are the 10 most expensive items AND their suppliers?\n")

ten_most_suppliers = curs.execute("""
SELECT ProductName, UnitPrice, CompanyName
FROM Product
Join Supplier
    ON Product.SupplierID = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10
;""").fetchall()

print(
f'The ten most expensive items and suppliers are: {list(ten_most_suppliers)}'
)
print('-'*80)

# What is the largest category (by number of unique products in it)?

print("What is the largest category (by # unique products)?\n")

larg_cat = curs.execute("""
SELECT CategoryName, COUNT(DISTINCT ProductName) AS Count
FROM Category
JOIN Product
    ON Category.Id = Product.CategoryId
GROUP BY CategoryName
ORDER BY Count DESC
LIMIT 1
;""").fetchall()

print(f'The largest category by number of unique products is: {list(larg_cat)}')
print('-'*80)

# (Stretch) Who is the Employee with the Most territories?

print("Who is the employee with the most territories?\n")

most_terr = curs.execute("""
SELECT FirstName, LastName, COUNT(TerritoryId) as TC
FROM Employee
JOIN EmployeeTerritory as ET
ON Employee.Id = ET.EmployeeId
GROUP BY Employee.Id
ORDER BY TC DESC
LIMIT 1
;""").fetchall()  # wow can't believe I got this to work, seems right

print(f'Employee with most territory is {list(most_terr)}')
print('-'*80)

# Part 4 Questions!

print("Part 4: Questions and Answers\n")

# In northwind database, what is relationship between Employee and Territory?

print("In the Northwind DB, what is the relationship between"
      " Employee and Territory labels?\n")

print("The relationship between these two is many-to-many. They are connected "
      "by the EmployeeTerritories \ntable according to the diagram, which is "
      "connected to both of them by a one-to-many connection.  \nWhen two tables"
      "are connected in this way by one-to-many, it can be considered many-"
      "to-many.")

print('-'*80)

# What is a situation where a document store (like MongoDB) is appropriate,
# and what is a situation where it is not appropriate.

print("What are situations in which a document store like MongoDB are"
      " and are not approrpriate?\n")

print("A database system like MongoDB is good for when you need something that"
      " is scalable and dynamic: that is \nto say that it can grow to be both "
      " very large while losing minimal querying ability as it gets more and\n"
      "more requests. It is perfect for cloud distributions such as those "
      "using AWS, Azure, etc.  It is not so\ngood for circumstances where you"
      "need strict ACID (atomic, consistency, isolation, durability)\nadherence,"
      "and it does not inherently support Joins.")

print('-'*80)

# What is NewSQL and what is it trying to achieve?

print("What is NewSQL and what is it trying to achieve?\n")

print("'NewSQL' is an attempt to combine all the benefits of traditional NoSQL"
      " systems like MongoDB, while still\nbeing able to maintain the ACID"
      " guarauntees of a traditional database system. This means in essence\n"
      "that it wants to be both scalable and highly available, when before "
      "after a certain point those two\npoints became tradeoffs (inversely"
      " proportional of one another).")
