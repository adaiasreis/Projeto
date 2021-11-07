import database.database as db
from clas.ocorrencia import Ocorrencia

def getSeguros():
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Seguros;")
    lista_planos = []
    for p in cursor.fetchall():
        id = p[0]
        ident = p[1]
        valor = p[2]
        nova = Ocorrencia(id, ident, valor)
        lista_planos.append(nova)
    conn.close()
    return lista_planos

def getSeguro(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("SELECT * FROM Seguros WHERE id=?;")
    cursor.execute(sql,[id])
    p = cursor.fetchall()[0]
    id = p[0]
    ident = p[1]
    valor = p[2]
    novo = Ocorrencia(id, ident, valor)
    conn.close()
    return novo

def addSeguro(seguro):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("INSERT INTO Seguros (ident, valor) VALUES (?,?);")
    cursor.execute(sql,[seguro.ident, seguro.valor])
    conn.commit()
    conn.close()

def editSeguro(seguro):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("UPDATE Seguros SET ident=?, valor=? WHERE id=?;")
    cursor.execute(sql,[seguro.ident, seguro.valor, seguro.id])
    conn.commit()
    conn.close()

def delSeguro(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("DELETE FROM Seguros WHERE id=?;")
    cursor.execute(sql,[id])
    conn.commit()
    conn.close()