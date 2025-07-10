import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Connect to database (creates users.db if it doesn't exist)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
''')

# Insert a test user (username: sanha, password: sss@123)
username = "sanha"
password = "sss@123"
hashed_pw = hash_password(password)

try:
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
    print("Test user added successfully.")
except sqlite3.IntegrityError:
    print("User already exists.")

conn.commit()
conn.close()
