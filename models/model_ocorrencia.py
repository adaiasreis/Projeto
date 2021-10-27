import database.database as db
from clas.ocorrencia import Ocorrencia

def getOcors():
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Ocorrencias;")
    lista_ocorrencias = []
    for o in cursor.fetchall():
        id = o[0]
        tipo = o[1]
        ident = o[2]
        valor = o[3]
        nova = Ocorrencia(id, tipo, ident, valor)
        lista_ocorrencias.append(nova)
    conn.close()
    return lista_ocorrencias

def getOcor(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("SELECT * FROM Ocorrencias WHERE id=?;")
    cursor.execute(sql, [id])  
    o = cursor.fetchall()[0]
    id = o[0]
    tipo = o[1]
    ident = o[2]
    valor = o[3]
    novo = Ocorrencia(id, tipo, ident, valor)
    conn.close()
    return novo

def addOcor(ocorrencia):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("INSERT INTO Ocorrencias (tipo, ident, valor) VALUES (?, ?, ?);")
    cursor.execute(sql, [ocorrencia.tipo, ocorrencia.ident, ocorrencia.valor])
    conn.commit()
    conn.close()

def editOcor(ocorrencia):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("UPDATE Ocorrencias SET tipo=?, ident=?, valor=? WHERE id=?;")
    cursor.execute(sql, [ocorrencia.tipo, ocorrencia.ident, ocorrencia.valor, ocorrencia.id])
    conn.commit()
    conn.close()

def delOcor(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("DELETE FROM Ocorrencias WHERE id=?;")
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()

def getOcorsPlan():
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute ("SELECT * FROM Ocorrencias WHERE tipo='Taxa Especial';")
    lista_planos = []
    for p in cursor.fetchall():
        id = p[0]
        tipo = p[1]
        ident = p[2]
        valor = p[3]
        nova = Ocorrencia(id,tipo, ident, valor)
        lista_planos.append(nova)
    conn.close()
    return lista_planos