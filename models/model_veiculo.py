import database.database as db
from clas.veiculo import Veiculo

def getVeiculos():
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Veiculos;")
    lista_veiculos = []
    for v in cursor.fetchall():
        id = v[0]
        marca = v[1]
        modelo = v[2]
        cor = v[3]
        categ = v[4]
        anoFab = v[5]
        placa = v[6]
        chassi = v[7]
        renavam = v[8]
        capPassag = v[9]
        portas = v[10]
        potencia = v[11]
        cilindradas = v[12]
        nova = Veiculo(id, marca, modelo, cor, categ, anoFab, placa, chassi, renavam, capPassag, portas, potencia, cilindradas)
        lista_veiculos.append(nova)
    conn.close()
    return lista_veiculos

def getVeiculosCateg(categ):
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Veiculos WHERE categ=?;" ,[categ])
    lista_veiculos = []
    for v in cursor.fetchall():
        id = v[0]
        marca = v[1]
        modelo = v[2]
        cor = v[3]
        categ = v[4]
        anoFab = v[5]
        placa = v[6]
        chassi = v[7]
        renavam = v[8]
        capPassag = v[9]
        portas = v[10]
        potencia = v[11]
        cilindradas = v[12]
        nova = Veiculo(id, marca, modelo, cor, categ, anoFab, placa, chassi, renavam, capPassag, portas, potencia, cilindradas)
        lista_veiculos.append(nova)
    conn.close()
    return lista_veiculos

def getVeiculo(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("SELECT * FROM Veiculos WHERE id=?;")
    cursor.execute(sql, [id])  
    v = cursor.fetchall()[0]
    id = v[0]
    marca = v[1]
    modelo = v[2]
    cor = v[3]
    categ = v[4]
    anoFab = v[5]
    placa = v[6]
    chassi = v[7]
    renavam = v[8]
    capPassag = v[9]
    portas = v[10]
    potencia = v[11]
    cilindradas = v[12]
    novo = Veiculo(id, marca, modelo, cor, categ, anoFab, placa, chassi, renavam, capPassag, portas, potencia, cilindradas)
    conn.close()
    return novo

def addVeiculo(veiculo):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO Veiculos (marca, modelo, cor, categ, anoFab, placa, chassi, renavam, capPassag, portas, potencia, cilindradas)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """
    cursor.execute(sql, [veiculo.marca, veiculo.modelo, veiculo.cor, veiculo.categ, veiculo.anoFab, veiculo.placa, veiculo.chassi, 
        veiculo.renavam, veiculo.capPassag, veiculo.portas, veiculo.potencia, veiculo.cilindradas])
    conn.commit()
    conn.close()

def editVeiculo(veiculo):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("UPDATE Veiculos SET marca=?, modelo=?, cor=?, categ=?, anoFab=?, placa=?, chassi=?, renavam=?, capPassag=?, portas=?, potencia=?, cilindradas=? WHERE id=?;")
    cursor.execute(sql, [veiculo.marca, veiculo.modelo, veiculo.cor, veiculo.categ, veiculo.anoFab, veiculo.placa, veiculo.chassi, 
        veiculo.renavam, veiculo.capPassag, veiculo.portas, veiculo.potencia, veiculo.cilindradas, veiculo.id])
    conn.commit()
    conn.close()

def delVeiculo(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("DELETE FROM Veiculos WHERE id=?;")
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()