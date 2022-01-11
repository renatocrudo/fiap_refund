from db import get_db

def insert_recibo(cnpj, nome_estabelecimento, descricao, total, imagem):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO recibo (cnpj, nome_estabelecimento, descricao, total, imagem) VALUES (?,?,?,?,?)"
    cursor.execute(statement, [cnpj, nome_estabelecimento, descricao, total, imagem])
    db.commit()
    return True

def update_recibo(id, cnpj, nome_estabelecimento, descricao, total, imagem):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE recibo SET cnpj = ?, nome_estabelecimento=?, descricao=?, total=?, imagem=? WHERE id=?"
    cursor.execute(statement, [cnpj, nome_estabelecimento, descricao, total, imagem, id])
    db.commit()
    return True


def delete_recibo(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM recibo WHERE id=?"
    cursor.execute(statement, [id])
    db.commit()
    return True

def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, cnpj, nome_estabelecimento, descricao, total, imagem FROM recibo WHERE id=?"
    cursor.execute(statement, [id])
    
    return cursor.fetchone()

def get_recibo():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, cnpj, nome_estabelecimento, descricao, total, imagem FROM recibo"
    cursor.execute(query)
    
    return cursor.fetchall()