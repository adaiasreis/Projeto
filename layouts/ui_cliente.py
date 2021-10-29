from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from components.table_clientes import TableWidget
from clas.cliente import Cliente
import models.model_ocorrencia as Ocorrencias 

class CadClientes(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_cliente.ui", self)

        self.table = TableWidget(self)
        self.verticalLayout.addWidget(self.table)

        self.setEventos()

        self.carregaDadosPlanos()

        self.clienteAtual = None

    def setEventos(self):
        self.b_novo.clicked.connect(self.addCliente)
        self.b_limpar.clicked.connect(self.limparCampos)
        self.b_excluir.clicked.connect(self.excluirItem)

    def carregaDadosPlanos(self):
        self.lista_planos = Ocorrencias.getOcorsPlan()
        lista_combo = []
        for o in self.lista_planos:
            lista_combo.append(o.ident)
        self.comboPlanos.addItems(lista_combo)

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
        plano = self.comboPlanos.currentText()

        if ((nome != "") and (rgNum != "") and (orgaoExp != "") and (rgDataEmis != "") and (cnhNum != "") and (categ != "") and (cnhDataEmis != "") and (cpf != "") and (telefone != "") and (nasc != "") and (email != "") and (endereco != "") and (nomeMae != "") and (plano != "Não Atribuido")):
            return Cliente (-1, self.campNome.text(), self.campRgn.text(), self.campRgo.text(), self.campRgd.text(), self.campChn.text(), self.campChc.text(), self.campChd.text(), self.campCpf.text(), self.campTelefone.text(), self.campNasc.text(), self.campEmail.text(), self.campEndereco.text(), self.campNmae.text(), self.comboPlanos.currentText())
        return None

    def limparCampos(self):
        self.clienteAtual = None
        self.campNome.setText("")
        self.campRgn.setText("")
        self.campRgo.setText("")
        self.campRgd.setText("")
        self.campChn.setText("")
        self.campChc.setText("")
        self.campChd.setText("")
        self.campCpf.setText("")
        self.campTelefone.setText("")
        self.campNasc.setText("")
        self.campEmail.setText("")
        self.campEndereco.setText("")
        self.campNmae.setText("")
        self.comboPlanos.setCurrentIndex(0)

        self.b_novo.setText("Adicionar")
        self.b_excluir.setEnabled(False)
        self.b_limpar.setEnabled(False)

    def insereCliente(self, cliente):
        self.clienteAtual = cliente
        self.campNome.setText(cliente.nome)
        self.campRgn.setText(cliente.rgNum)
        self.campRgo.setText(cliente.orgaoExp)
        self.campRgd.setText(cliente.rgDataEmis)
        self.campChn.setText(cliente.cnhNum)
        self.campChc.setText(cliente.categ)
        self.campChd.setText(cliente.cnhDataEmis)
        self.campCpf.setText(cliente.cpf)
        self.campTelefone.setText(cliente.telefone)
        self.campNasc.setText(cliente.nasc)
        self.campEmail.setText(cliente.email)
        self.campEndereco.setText(cliente.endereco)
        self.campNmae.setText(cliente.nomeMae)
        self.comboPlanos.setCurrentText(cliente.plano)

        self.b_novo.setText("Atualizar")
        self.b_excluir.setEnabled(True)
        self.b_limpar.setEnabled(True)

    def excluirItem(self):
        self.table.delete(self.clienteAtual)
        self.limparCampos()