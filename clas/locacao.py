#Classe locação
class Reserva:
    def __init__ (self, id, cliente, plano, tipo, veiculo, data_inic, data_fim, status):
        self.id = id
        self.cliente = cliente
        self.plano = plano
        self.tipo = tipo
        self.veiculo = veiculo
        self.data_inic = data_inic
        self.data_fim = data_fim
        self.status = status

class Locacao:
    def __init__(self, id, cliente, kmAtual, estim, seguro, taxa, servicos, valorLoc):
        self.id = id
        self.cliente = cliente
        self.kmAtual = kmAtual
        self.estim = estim
        self.seguro = seguro
        self.taxa = taxa
        self.servicos = servicos
        self.valorLoc = valorLoc

class Checkout:

    pass
