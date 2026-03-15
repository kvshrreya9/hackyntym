import sqlite3

conn = sqlite3.connect("donors.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE donors(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
blood TEXT,
phone TEXT,
city TEXT,
area TEXT,
availability TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")