import sqlite3

conn = sqlite3.connect("donors.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS donors(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
blood TEXT,
phone TEXT,
city TEXT,
area TEXT,
availability TEXT
)
""")

print("Database created successfully")

conn.commit()
conn.close()