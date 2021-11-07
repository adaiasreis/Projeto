import database.database as db
from clas.locacao import Locacao

def getLocacoes():
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Locacoes;")
    lista_locacaoes = []
    for l in cursor.fetchall():
        id = l[0]
        id_res = l[1]
        kmAtual = l[2]
        kmEstim = l[3]
        status = l[4]
        nova = Locacao(id, id_res, kmAtual,kmEstim, status)
        lista_locacaoes.append(nova)
    conn.close()
    return lista_locacaoes

def getLocacao(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("SELECT * FROM Locacoes WHERE id=?;")
    cursor.execute(sql, [id])  
    l = cursor.fetchall()[0]
    id = l[0]
    id_res = l[1]
    kmAtual = l[2]
    kmEstim = l[3]
    status = l[4]
    novo = Locacao(id, id_res,kmAtual,kmEstim,status)
    conn.close()
    return novo

def addLocacao(locacao):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO Locacoes (id_res, kmAtual, kmEstim, status)
            VALUES (?, ?, ?, ?, ?, ?, ?);"""
    cursor.execute(sql, [locacao.id_res, locacao.kmAtual, locacao.kmEstim, locacao.status])
    conn.commit()
    conn.close()

def editLocacao(locacao):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("UPDATE Locacoes SET id_res=?, kmAtual=?, kmEstim=?, status=? WHERE id=?;")
    cursor.execute(sql, [locacao.id_res, locacao.kmAtual, locacao.kmEstim, locacao.status, locacao.id])
    conn.commit()
    conn.close()

def delLocacao(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("DELETE FROM Locacoes WHERE id=?;")
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()