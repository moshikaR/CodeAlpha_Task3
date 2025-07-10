import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
""")

# Create one test user: admin / admin123
username = "admin"
password = "admin123"
hashed_pw = hash_password(password)

try:
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
    print("Test user created successfully.")
except sqlite3.IntegrityError:
    print("User already exists.")

conn.commit()
conn.close()
