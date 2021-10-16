from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from components.table_clientes import TableWidget
from clas.cliente import Cliente

class CadClientes(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_cliente.ui", self)

        self.table = TableWidget(self)
        self.verticalLayout.addWidget(self.table)

        self.setEventos()

        self.clienteAtual = None

    def setEventos(self):
        self.b_novo.clicked.connect(self.addCliente)
        self.b_limpar.clicked.connect(self.limparCampos)
        self.b_excluir.clicked.connect(self.excluirItem)

    def addCliente(self):
        novoCliente = self.getClientes()
        if novoCliente != None:
            if self.clienteAtual == None:
                self.table.add(novoCliente)
            else:
                novoCliente.id = self.clienteAtual.id
                self.table.update(novoCliente)
            self.limparCampos()

    def getClientes(self):
        nome = self.campNome.text()
        rgNum = self.campRgn.text()
        orgaoExp = self.campRgo.text()
        rgDataEmis = self.campRgd.text()
        cnhNum = self.campChn.text()
        categ = self.campChc.text()
        cnhDataEmis = self.campChd.text()
        cpf = self.campCpf.text()
        telefone = self.campTelefone.text()
        nasc = self.campNasc.text()
        email = self.campEmail.text()
        endereco = self.campEndereco.text()
        nomeMae = self.campNmae.text()

        if ((nome != "") and (rgNum != "") and (orgaoExp != "") and (rgDataEmis != "") and (cnhNum != "") and (categ != "") and (cnhDataEmis != "") and (cpf != "") and (telefone != "") and (nasc != "") and (email != "") and (endereco != "") and (nomeMae != "")):
            return Cliente (-1, self.campNome.text(), self.campRgn.text(), self.campRgo.text(), self.campRgd.text(), self.campChn.text(), self.campChc.text(), self.campChd.text(), self.campCpf.text(), self.campTelefone.text(), self.campNasc.text(), self.campEmail.text(), self.campEndereco.text(), self.campNmae.text())
        return None

    def limparCampos(self):
        self.clienteAtual = None
        self.campNome.text("")
        self.campRgn.text("")
        self.campRgo.text("")
        self.campRgd.text("")
        self.campChn.text("")
        self.campChc.text("")
        self.campChd.text("")
        self.campCpf.text("")
        self.campTelefone.text("")
        self.campNasc.text("")
        self.campEmail.text("")
        self.campEndereco.text("")
        self.campNmae.text("")

        self.b_novo.setText("Adicionar")
        self.b_excluir.setEnabled(False)
        self.b_limpar.setEnabled(False)

    def insereCliente(self, cliente):
        self.clienteAtual = cliente
        self.campNome.text(cliente.nome)
        self.campRgn.text(cliente.rgNum)
        self.campRgo.text(cliente.orgaoExp)
        self.campRgd.text(cliente.rgDataEmis)
        self.campChn.text(cliente.cnhNum)
        self.campChc.text(cliente.categ)
        self.campChd.text(cliente.cnhDataEmis)
        self.campCpf.text(cliente.cpf)
        self.campTelefone.text(cliente.telefone)
        self.campNasc.text(cliente.nasc)
        self.campEmail.text(cliente.email)
        self.campEndereco.text(cliente.endereco)
        self.campNmae.text(cliente.nomeMae)

        self.b_novo.setText("Atualizar")
        self.b_excluir.setEnabled(True)
        self.b_limpar.setEnabled(True)

    def excluirItem(self):
        self.table.delete(self.clienteAtual)
        self.limparCampos()