import psycopg2
import os
from dotenv import load_dotenv


DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

connection = psycopg2.connect(
    dbname="yowekqov",
    user="yowekqov",
    password="6zYeZqDtoSGhU_wDwHisgx_0UCFjABii",
    host=DB_HOST
)

cursor = connection.cursor()


insert_query = """
INSERT INTO test_table (name, data) VALUES
(
    'A row name',
    null
),
(
    'Another row, with JSON',
    '{"a": 1, "b": ["dog", "cat", 42], "c": true}'::JSONB

);
"""

cursor.execute(insert_query)


print(results)
