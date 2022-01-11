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
            cnpj text not null,
            nome_estabelecimento TEXT NOT NULL,
            descricao TEXT null
            total REAL NOT NULL,
            imagem BLOB NULL)"""
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)