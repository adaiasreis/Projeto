from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from components.table_servicos import TableWidget
from clas.ocorrencia import Ocorrencia

class CadServicos(QWidget):
    def __init__(self, janelaOcorrencia):
        super(). __init__()
        uic.loadUi("ui/ui_servico.ui", self)

        self.janelaOcorrencia = janelaOcorrencia

        self.table = TableWidget(self)
        self.verticalLayout.addWidget(self.table)
        
        self.setEventos()

        self.servicoAtual = None

    def setEventos(self):
        self.b_novo.clicked.connect(self.addOcor)
        self.b_limpar.clicked.connect(self.limparCampos)
        self.b_excluir.clicked.connect(self.excluirItem)

    def addOcor(self):
        novoServico = self.getOcor()
        if novoServico != None:
            if self.servicoAtual == None:
                self.table.add(novoServico)
            else:
                novoServico.id = self.servicoAtual.id
                self.table.update(novoServico)
            self.limparCampos()

    def getOcor(self):
        indet = self.campIdent.text()
        valor = self.campValor.text()

        if (indet != "") and (valor != ""):
            return Ocorrencia (-1, self.campIdent.text(), self.campValor.text())
        return None

    def limparCampos(self):
        self.servicoAtual = None
        self.campIdent.setText("")
        self.campValor.setText("")

        self.b_novo.setText("Adicionar")
        self.b_excluir.setEnabled(False)
        self.b_limpar.setEnabled(False)

    def insereOcor(self, servico):
        self.servicoAtual = servico
        self.campIdent.setText(servico.ident)
        self.campValor.setText(str("%.2f" %servico.valor))

        self.b_novo.setText("Atualizar")
        self.b_excluir.setEnabled(True)
        self.b_limpar.setEnabled(True)

    def excluirItem(self):
        self.table.delete(self.servicoAtual)
        self.limparCampos()