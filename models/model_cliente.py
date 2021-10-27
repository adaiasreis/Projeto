import database.database as db
from clas.cliente import Cliente

def getClientes():
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Clientes;")
    lista_clientes = []
    for c in cursor.fetchall():
        id = c[0]
        nome = c[1]
        rgNum = c[2]
        orgaoExp = c[3]
        rgDataEmis = c[4]
        cnhNum = c[5]
        categ = c[6]
        cnhDataEmis = c[7]
        cpf = c[8]
        telefone = c[9]
        nasc = c[10]
        email = c[11]
        endereco = c[12]
        nomeMae = c[13]
        plano = c[14]
        nova = Cliente(id, nome, rgNum, orgaoExp, rgDataEmis, cnhNum, categ, cnhDataEmis, cpf, telefone, nasc, email, endereco, nomeMae, plano)
        lista_clientes.append(nova)
    conn.close()
    return lista_clientes

def getCliente(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("SELECT * FROM Clientes WHERE id=?;")
    cursor.execute(sql, [id])  
    c = cursor.fetchall()[0]
    id = c[0]
    nome = c[1]
    rgNum = c[2]
    orgaoExp = c[3]
    rgDataEmis = c[4]
    cnhNum = c[5]
    categ = c[6]
    cnhDataEmis = c[7]
    cpf = c[8]
    telefone = c[9]
    nasc = c[10]
    email = c[11]
    endereco = c[12]
    nomeMae = c[13]
    plano = c[14]
    novo = Cliente(id, nome, rgNum, orgaoExp, rgDataEmis, cnhNum, categ, cnhDataEmis, cpf, telefone, nasc, email, endereco, nomeMae, plano)
    conn.close()
    return novo

def addCliente(cliente):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO Clientes (nome, rgNum, orgaoExp, rgDataEmis, cnhNum, categ, cnhDataEmis, cpf, telefone, nasc, email, endereco, nomeMae, plano)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    cursor.execute(sql, [cliente.nome, cliente.rgNum, cliente.orgaoExp, cliente.rgDataEmis, cliente.cnhNum, cliente.categ, cliente.cnhDataEmis,
            cliente.cpf, cliente.telefone, cliente.nasc, cliente.email, cliente.endereco, cliente.nomeMae, cliente.plano])
    conn.commit()
    conn.close()

def editCliente(cliente):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("UPDATE Clientes SET nome=?, rgNum=?, orgaoExp=?, rgDataEmis=?, cnhNum=?, categ=?, cnhDataEmis=?, cpf=?, telefone=?, nasc=?, email=?, endereco=?, nomeMae=?, plano=? WHERE id=?;")
    cursor.execute(sql, [cliente.nome, cliente.rgNum, cliente.orgaoExp, cliente.rgDataEmis, cliente.cnhNum, cliente.categ, cliente.cnhDataEmis, cliente.cpf, cliente.telefone,
            cliente.nasc, cliente.email, cliente.endereco, cliente.nomeMae, cliente.plano, cliente.id])
    conn.commit()
    conn.close()

def delCliente(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("DELETE FROM Clientes WHERE id=?;")
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()