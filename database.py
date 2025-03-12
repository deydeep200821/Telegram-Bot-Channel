from config import DB_URL, USE_SQLITE, USE_MONGODB, USE_POSTGRES, MONGO_URI, POSTGRES_URL
import sqlite3
from pymongo import MongoClient
import psycopg2

# SQLite Setup (Default)
if USE_SQLITE:
    conn = sqlite3.connect("bot_database.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            role TEXT
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS logs (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            log_message TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()

# MongoDB Setup (Optional)
elif USE_MONGODB:
    client = MongoClient(MONGO_URI)
    db = client["telegram_bot"]
    users_collection = db["users"]
    logs_collection = db["logs"]

# PostgreSQL Setup (Optional)
elif USE_POSTGRES:
    conn = psycopg2.connect(POSTGRES_URL)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id BIGINT PRIMARY KEY,
            username TEXT,
            role TEXT
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS logs (
            log_id SERIAL PRIMARY KEY,
            log_message TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()

# Function to Add User to Database
def add_user(user_id, username, role="user"):
    if USE_SQLITE or USE_POSTGRES:
        cursor.execute("INSERT OR IGNORE INTO users (user_id, username, role) VALUES (?, ?, ?)", (user_id, username, role))
        conn.commit()
    elif USE_MONGODB:
        users_collection.update_one(
            {"user_id": user_id},
            {"$set": {"username": username, "role": role}},
            upsert=True,
        )

# Function to Log Actions
def add_log(message):
    if USE_SQLITE or USE_POSTGRES:
        cursor.execute("INSERT INTO logs (log_message) VALUES (?)", (message,))
        conn.commit()
    elif USE_MONGODB:
        logs_collection.insert_one({"log_message": message})

# Function to Get User Role
def get_user_role(user_id):
    if USE_SQLITE or USE_POSTGRES:
        cursor.execute("SELECT role FROM users WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        return result[0] if result else "user"
    elif USE_MONGODB:
        user = users_collection.find_one({"user_id": user_id})
        return user["role"] if user else "user"

# Function to Get All Users
def get_all_users():
    if USE_SQLITE or USE_POSTGRES:
        cursor.execute("SELECT user_id, username, role FROM users")
        return cursor.fetchall()
    elif USE_MONGODB:
        return list(users_collection.find({}, {"_id": 0}))

# Function to Get Logs
def get_logs():
    if USE_SQLITE or USE_POSTGRES:
        cursor.execute("SELECT log_message, timestamp FROM logs")
        return cursor.fetchall()
    elif USE_MONGODB:
        return list(logs_collection.find({}, {"_id": 0}))

