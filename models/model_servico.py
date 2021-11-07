import database.database as db
from clas.ocorrencia import Ocorrencia

def getServicos():
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Servicos;")
    lista_planos = []
    for s in cursor.fetchall():
        id = s[0]
        ident = s[1]
        valor = s[2]
        nova = Ocorrencia(id, ident, valor)
        lista_planos.append(nova)
    conn.close()
    return lista_planos

def getServico(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("SELECT * FROM Servicos WHERE id=?;")
    cursor.execute(sql,[id])
    s = cursor.fetchall()[0]
    id = s[0]
    ident = s[1]
    valor = s[2]
    novo = Ocorrencia(id, ident, valor)
    conn.close()
    return novo

def addServico(servico):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("INSERT INTO Servicos (ident, valor) VALUES (?,?);")
    cursor.execute(sql,[servico.ident, servico.valor])
    conn.commit()
    conn.close()

def editPlano(servico):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("UPDATE Servicos SET ident=?, valor=? WHERE id=?;")
    cursor.execute(sql,[servico.ident, servico.valor, servico.id])
    conn.commit()
    conn.close()

def editPlano(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("DELETE FROM Servicos WHERE id=?;")
    cursor.execute(sql,[id])
    conn.commit()
    conn.close()