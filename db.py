from os import curdir
import sqlite3

DATABASE_NAME = "fiap.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS recibo( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_estabelecimento TEXT NOT NULL,
            total REAL NOT NULL,
            rate INTEGER NOT NULL)"""
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)