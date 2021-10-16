import database.database as db
from clas.funcionario import Funcionario

def getFuncs():
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Funcionarios")
    lista_funcionarios = []
    for f in cursor.fetchall():
        id = f[0]
        nome = f[1]
        rgNum = f[2]
        orgaoExp = f[3]
        dataEmis = f[4]
        cpf = f[5]
        telefone = f[6]
        nasc = f[7]
        email = f[8]
        endereco = f[9]
        nomeMae = f[10]
        cargo = f[11]
        salario = f[12]
        cargahs = f[13]
        usuario = f[14]
        senha = f[15]
        nova = Funcionario(id, nome, rgNum, orgaoExp, dataEmis, cpf, telefone, nasc, email, endereco, nomeMae, cargo, salario, cargahs, usuario, senha)
        lista_funcionarios.append(nova)
    conn.close()
    return lista_funcionarios

def getFunc(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("SELECT * FROM Funcionarios WHERE id=?;")
    cursor.execute(sql, [id])  
    f = cursor.fetchall()[0]
    id = f[0]
    nome = f[1]
    rgNum = f[2]
    orgaoExp = f[3]
    dataEmis = f[4]
    cpf = f[5]
    telefone = f[6]
    nasc = f[7]
    email = f[8]
    endereco = f[9]
    nomeMae = f[10]
    cargo = f[11]
    salario = f[12]
    cargahs = f[13]
    usuario = f[14]
    senha = f[15]
    novo = Funcionario(id, nome, rgNum, orgaoExp, dataEmis, cpf, telefone, nasc, email, endereco, nomeMae, cargo, salario, cargahs, usuario, senha)
    conn.close()
    return novo

def addFunc(funcionario):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO Funcionarios (nome, rgNum, orgaoExp, dataEmis, cpf, telefone, nasc, email, endereco, nomeMae, cargo, salario, cargahs, usuario, senha)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    cursor.execute(sql, [funcionario.nome, funcionario.rgNum, funcionario.orgaoExp, funcionario.dataEmis, funcionario.cpf, funcionario.telefone, funcionario.nasc,
        funcionario.email, funcionario.endereco, funcionario.nomeMae, funcionario.cargo, funcionario.salario, funcionario.cargahs, funcionario.usuario, funcionario.senha])
    conn.commit()
    conn.close()

def editFunc(funcionario):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("UPDATE Funcionarios SET nome=?, rgNum=?, orgaoExp=?, dataEmis=?, cpf=?, telefone=?, nasc=?, email=?, endereco=?, nomeMae=?, cargo=?, salario=?, cargahs=?, usuario=?, senha=?;")
    cursor.execute(sql, [funcionario.nome, funcionario.rgNum, funcionario.orgaoExp, funcionario.dataEmis, funcionario.cpf, funcionario.telefone, funcionario.nasc,
        funcionario.email, funcionario.endereco, funcionario.nomeMae, funcionario.cargo, funcionario.salario, funcionario.cargahs, funcionario.usuario, funcionario.senha])
    conn.commit()
    conn.close()

def delFunc(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("DELETE FROM Funcionarios WHERE id=?;")
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()

def getLogin(usuario, senha):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("SELECT nome, usuario, senha FROM Funcionarios WHERE usuario=? AND senha=?;")
    cursor.execute(sql, [usuario, senha])
    new_list = []
    for u in cursor.fetchall():
        nome = u[0]
        usuario = u[1]
        senha = u[2]
        new = {'nome': nome, 'usuario': usuario,'senha': senha}
        new_list.append(new)
    conn.close()
    return new_list