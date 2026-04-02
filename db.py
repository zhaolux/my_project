import sqlite3

def get_conn():
    return sqlite3.connect("data.db", check_same_thread=False)

def create_tables():
    conn = get_conn()
    c = conn.cursor()

    # 用户表
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
    """)

    # 数据表
    c.execute("""
    CREATE TABLE IF NOT EXISTS sales_data (
        username TEXT,
        date TEXT,
        product TEXT,
        quantity INTEGER
    )
    """)

    conn.commit()
    conn.close()
