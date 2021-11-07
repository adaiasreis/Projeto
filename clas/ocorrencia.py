class Ocorrencia:
    def __init__ (self, id, ident, valor):
        self.id = id
        self.ident = ident
        self.valor = valor

class Plano:
    def __init__ (self, id, indet, valor, tipoLoc, valorDia, valorKmEst, valorKmExced, b_valorDia, b_valorEst, b_valorExced):
        self.id = id
        self.ident = indet
        self.valor = valor
        self.tipoLoc = tipoLoc
        self.valorDia = valorDia
        self.valorKmEst = valorKmEst
        self.valorKmExced = valorKmExced
        self.b_valorDia = b_valorDia
        self.b_valorEst = b_valorEst
        self.b_valorExced = b_valorExced