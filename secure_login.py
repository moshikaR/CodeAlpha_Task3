import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    hashed_pw = hash_password(password)
    cursor.execute(query, (username, hashed_pw))
    result = cursor.fetchone()
    if result:
        print("Login successful!")
    else:
        print("Login failed.")
    conn.close()

# Example usage
if __name__ == "__main__":
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    login(user, pwd)
