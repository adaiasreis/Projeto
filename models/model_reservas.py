import database.database as db
from clas.locacao import Reserva

def getReservas():
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Reservas;")
    lista_reservas = []
    for r in cursor.fetchall():
        id = r[0]
        id_cliente = r[1]
        cliente = r[2]
        plano = r[3]
        tipo = r[4]
        id_veiculo = r[5]
        veiculo = r[6]
        dp_saida = r[7]
        dp_retorno = r[8]
        valor_prev = r[9]
        status = r[10]
        nova = Reserva(id, id_cliente, cliente, plano, tipo, id_veiculo,veiculo, dp_saida, dp_retorno, valor_prev, status)
        lista_reservas.append(nova)
    conn.close()
    return lista_reservas

def getReserva(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("SELECT * FROM Reservas WHERE id=?;")
    cursor.execute(sql, [id])
    r = cursor.fetchall()[0]
    id = r[0]
    id_cliente = r[1]
    cliente = r[2]
    plano = r[3]
    tipo = r[4]
    id_veiculo = r[5]
    veiculo = r[6]
    dp_saida = r[7]
    dp_retorno = r[8]
    valor_prev = r[9]
    status = r[10]
    novo = Reserva(id, id_cliente, cliente, plano, tipo, id_veiculo, veiculo, dp_saida, dp_retorno, valor_prev, status)
    conn.close()
    return novo

def addReserva(reserva):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO Reservas (id_cliente, cliente, plano, tipo, id_veiculo, veiculo, dp_saida, dp_retorno, valor_prev, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    cursor.execute(sql, [reserva.id_cliente, reserva.cliente, reserva.plano, reserva.tipo, reserva.id_veiculo, reserva.veiculo, 
            reserva.dp_saida, reserva.dp_retorno, reserva.valor_prev, reserva.status])
    conn.commit()
    conn.close

def editReserva(reserva):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("UPDATE Reservas SET id_cliente=?, cliente=?, plano=?, tipo=?, id_veiculo=?, veiculo=?, dp_saida=? dp_retorno=?, valor_prev=?, status=? WHERE id=?;")
    cursor.execute(sql, [reserva.id_cliente, reserva.plano, reserva.tipo, reserva.id_veiculo, reserva.dp_saida, reserva.dp_retorno, reserva.valor_prev, reserva.status, reserva.id])
    conn.commit()
    conn.close()

def delReserva(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("DELETE FROM Reservas WHERE id=?;")
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()