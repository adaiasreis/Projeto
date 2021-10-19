import database.database as db
from clas.locacao import Locacao

def getLocacoes():
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Locacoes;")
    lista_locacaoes = []
    for l in cursor.fetchall():
        id = l[0]
        dataLoc = l[1]
        veiculo = l[2]
        cliente = l[3]
        kmAtual = l[4]
        hora = l[5]
        kmEstim = l[6]
        seguro = l[7]
        taxa = l[8]
        valorLoc = l[9]
        status = l[10]
        dataEnt = l[11]
        kmEnt = l[12]
        infoEnt = l[13]
        nova = Locacao(id, dataLoc, veiculo, cliente, kmAtual, hora, kmEstim, seguro, taxa, valorLoc, status, dataEnt, kmEnt, infoEnt)
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
    dataLoc = l[1]
    veiculo = l[2]
    cliente = l[3]
    kmAtual = l[4]
    hora = l[5]
    kmEstim = l[6]
    seguro = l[7]
    taxa = l[8]
    valorLoc = l[9]
    status = l[10]
    dataEnt = l[11]
    kmEnt = l[12]
    infoEnt = l[13]
    novo = Locacao(id, dataLoc, veiculo, cliente, kmAtual, hora, kmEstim, seguro, taxa, valorLoc, status, dataEnt, kmEnt, infoEnt)
    conn.close()
    return novo

def addLocacao(locacao):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO Locacoes (dataLoc, veiculo, cliente, kmAtual, hora, kmEstim, seguro, taxa, valorLoc, status, dataEnt, kmEnt, infoEnt)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    cursor.execute(sql, [locacao.dataLoc, locacao.veiculo, locacao.cliente, locacao.kmAtual, locacao.hora, locacao.kmEstim, locacao.seguro, locacao.taxa,
        locacao.valorLoc, locacao.status, locacao.dataEnt, locacao.kmEnt, locacao.infoEnt])
    conn.commit()
    conn.close()

def editLocacao(locacao):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("UPDATE Locacoes SET dataLoc=?, veiculo=?, cliente=?, kmAtual=?, hora=?, kmEstim=?, seguro=?, taxa=?, valorLoc=?, status=?, dataEnt=?, kmEnt=?, infoEnt=? WHERE id=?")
    cursor.execute(sql, [locacao.dataLoc, locacao.veiculo, locacao.cliente, locacao.kmAtual, locacao.hora, locacao.kmEstim, locacao.seguro, locacao.taxa, locacao.valorLoc,
        locacao.status, locacao.dataEnt, locacao.kmEnt, locacao.infoEnt, locacao.id])
    conn.commit()
    conn.close()

def delLocacao(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("DELETE FROM Locacoes WHERE id=?;")
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()