import sqlite3

def create_user_table():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (username TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()

def sign_up(username, password):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("User created successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists!")
    conn.close()

def login(username, password):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

create_user_table()
username = input("Enter username: ")
password = input("Enter password: ")

if login(username, password):
    print("Login successful!")
else:
    sign_up(username, password)
