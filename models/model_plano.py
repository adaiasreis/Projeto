import database.database as db
from clas.ocorrencia import Plano

def getPlanos():
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Planos;")
    lista_planos = []
    for p in cursor.fetchall():
        id = p[0]
        ident = p[1]
        valor = p[2]
        tipoLoc = p[3]
        valorDia = p[4]
        valorKmEst = p[5]
        valorKmExced = p[6]
        b_valorDia = p[7]
        b_valorEst = p[8]
        b_valorExced = p[9]
        nova = Plano(id, ident, valor, tipoLoc, valorDia, valorKmEst, valorKmExced, b_valorDia, b_valorEst, b_valorExced)
        lista_planos.append(nova)
    conn.close()
    return lista_planos

def getPlano(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("SELECT * FROM Planos WHERE id=?;")
    cursor.execute(sql,[id])
    p = cursor.fetchall()[0]
    id = p[0]
    ident = p[1]
    valor = p[2]
    tipoLoc = p[3]
    valorDia = p[4]
    valorKmEst = p[5]
    valorKmExced = p[6]
    b_valorDia = p[7]
    b_valorEst = p[8]
    b_valorExced = p[9]
    novo = Plano(id, ident, valor, tipoLoc, valorDia, valorKmEst, valorKmExced, b_valorDia, b_valorEst, b_valorExced)
    conn.close()
    return novo

def addPlano(plano):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("""INSERT INTO Planos (ident, valor, tipoLoc, valorDia, valorKmEst, valorKmExced, b_valorDia, b_valorEst, b_valorExced)
            VALUES (?,?,?,?,?,?,?,?,?);""")
    cursor.execute(sql,[plano.ident, plano.valor, plano.tipoLoc, plano.valorDia, plano.valorKmEst, plano.valorKmExced, plano.b_valorDia, plano.b_valorEst, plano.b_valorExced])
    conn.commit()
    conn.close()

def editPlano(plano):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("UPDATE Planos SET ident=?, valor=?, tipoLoc=?, valorDia=?, valorKmEst=?, valorKmExced=?, b_valorDia=?, b_valorEst=?, b_valorExced=? WHERE id=?;")
    cursor.execute(sql,[plano.ident, plano.valor, plano.tipoLoc, plano.valorDia, plano.valorKmEst, plano.valorKmExced, plano.b_valorDia, plano.b_valorEst, plano.b_valorExced, plano.id])
    conn.commit()
    conn.close()

def delPlano(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("DELETE FROM Planos WHERE id=?;")
    cursor.execute(sql,[id])
    conn.commit()
    conn.close()