import sqlite3
from datetime import datetime, timedelta

# Создаём соединение с базой данных
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Создаём таблицу пользователей
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        usage_count INTEGER DEFAULT 0,
        subscription_active INTEGER DEFAULT 0,
        subscription_end TEXT
    )
''')
conn.commit()

def add_user(user_id: int):
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    if user is None:
        cursor.execute('INSERT INTO users (user_id) VALUES (?)', (user_id,))
        conn.commit()

def get_user_data(user_id: int):
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    if user:
        return {
            'user_id': user[0],
            'usage_count': user[1],
            'subscription_active': bool(user[2]),
            'subscription_end': user[3]
        }
    return None

def increment_usage(user_id: int):
    cursor.execute('UPDATE users SET usage_count = usage_count + 1 WHERE user_id = ?', (user_id,))
    conn.commit()

def activate_subscription(user_id: int, days: int = 30):
    subscription_end = datetime.now() + timedelta(days=days)
    cursor.execute('''
        UPDATE users
        SET subscription_active = 1,
            subscription_end = ?
        WHERE user_id = ?
    ''', (subscription_end.isoformat(), user_id))
    conn.commit()

def is_subscription_active(user: dict) -> bool:
    if user['subscription_active']:
        if user['subscription_end']:
            end_time = datetime.fromisoformat(user['subscription_end'])
            if end_time > datetime.now():
                return True
    return False