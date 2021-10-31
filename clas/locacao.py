#Classe locação
class Reserva:
    def __init__ (self, id,id_cliente, cliente, plano, tipo, id_veiculo, veiculo, dp_saida, dp_retorno, diarias, valor_prev, status):
        self.id = id
        self.id_cliente = id_cliente
        self.cliente = cliente
        self.plano = plano
        self.tipo = tipo
        self.id_veiculo = id_veiculo
        self.veiculo = veiculo
        self.dp_saida = dp_saida
        self.dp_retorno = dp_retorno
        self.diarias = diarias
        self.valor_prev = valor_prev
        self.status = status

class Locacao:
    def __init__(self, id, id_res, kmAtual, kmEstim, seguro, servicos, valorLoc, status):
        self.id = id
        self.id_res = id_res
        self.kmAtual = kmAtual
        self.kmEstim = kmEstim
        self.seguro = seguro
        self.servicos = servicos
        self.valorLoc = valorLoc
        self.status = status

class Checkout:

    pass

class Tipo:
    def __init__(self, id, ident, v_diaria, v_kmEst, v_kmExced):
        self.id = id
        self.ident = ident
        self.v_diaria = v_diaria
        self.v_kmEst = v_kmEst
        self.v_kmExced = v_kmExced