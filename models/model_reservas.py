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
        plano = r[2]
        id_tipo = r[3]
        id_veiculo = r[4]
        dp_saida = r[5]
        dp_retorno = r[6]
        status = r[7]
        nova = Reserva(id, id_cliente, plano, id_tipo, id_veiculo, dp_saida, dp_retorno, status)
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
    plano = r[2]
    id_tipo = r[3]
    id_veiculo = r[4]
    dp_saida = r[5]
    dp_retorno = r[6]
    status = r[7]
    novo = Reserva(id, id_cliente, plano, id_tipo, id_veiculo, dp_saida, dp_retorno, status)
    conn.close()
    return novo

def addReserva(reserva):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO Reservas (id_cliente, plano, id_tipo, id_veiculo, dp_saida, dp_retorno, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)"""
    cursor.execute(sql, [reserva.id_cliente, reserva.plano, reserva.id_tipo, reserva.i_veiculo, 
        reserva.dp_saida, reserva.dp_retorno, reserva.status])
    conn.commit()
    conn.close

def editReserva(reserva):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("UPDATE Reservas SET id_cliente=?, plano=?, id_tipo=?, id_veiculo=?, dp_saida=? dp_retorno=?, status=? WHERE id=?;")
    cursor.execute(sql, [reserva.id_cliente, reserva.plano, reserva.id_tipo, reserva.i_veiculo, 
        reserva.dp_saida, reserva.dp_retorno, reserva.status, reserva.id])
    conn.commit()
    conn.close()

def delReserva(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = ("DELETE FROM Reservas WHERE id=?;")
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()