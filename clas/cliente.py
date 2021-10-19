#Classe Clientes
class Cliente:
    def __init__(self, id, nome, rgNum, orgaoExp, rgDataEmis, cnhNum, categ, cnhDataEmis, cpf, telefone, nasc, email, endereco, nomeMae):
        self.id = id
        self.nome = nome
        self.rgNum = rgNum
        self.orgaoExp = orgaoExp
        self.rgDataEmis = rgDataEmis
        self.cnhNum = cnhNum
        self.categ = categ
        self.cnhDataEmis = cnhDataEmis
        self.cpf = cpf
        self.telefone = telefone
        self.nasc = nasc
        self.email = email
        self.endereco = endereco
        self.nomeMae = nomeMae