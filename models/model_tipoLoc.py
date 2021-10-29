import database.database as db
from clas.locacao import Tipo

def getTipos():
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Tipos;")
    lista_tipos = []
    for t in cursor.fetchall():
        id = t[0]
        ident = t[1]
        v_diaria = t[2]
        v_kmEst = t[3]
        v_kmExced = t[4]
        nova = Tipo (id, ident, v_diaria, v_kmEst, v_kmExced)
        lista_tipos.append(nova)
    conn.close()
    return lista_tipos

def getTipo(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("SELECT * FROM Tipos WHERE id=?;")
    cursor.execute(sql, [id])  
    t = cursor.fetchall()[0]
    id = t[0]
    ident = t[1]
    v_diaria = t[2]
    v_kmEst = t[3]
    v_kmExced = t[4]
    novo = Tipo(id, ident,v_diaria, v_kmEst, v_kmExced)
    conn.close()
    return novo

def addTipo(tipo):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO Tipos (ident, v_diaria, v_kmEst, v_kmExced)
            VALUES (?,?,?,?);"""
    cursor.execute(sql, [tipo.ident, tipo.v_diaria, tipo.v_kmEst, tipo.v_kmExced])
    conn.commit()
    conn.close()

def editTipo(tipo):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("UPDATE Tipos SET ident=?, v_diaria=?, v_kmEst=?, v_kmExced=? WHERE id=?;")
    cursor.execute(sql, [tipo.ident, tipo.v_diaria, tipo.v_kmEst, tipo.v_kmExced, tipo.id])
    conn.commit()
    conn.close()

def delTipo(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("DELETE FROM Tipos WHERE id=?;")
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()