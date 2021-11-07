from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from components.table_seguros import TableWidget
from clas.ocorrencia import Ocorrencia

class CadSeguros(QWidget):
    def __init__(self, janelaOcorrencia):
        super(). __init__()
        uic.loadUi("ui/ui_seguro.ui", self)

        self.janelaOcorrencia = janelaOcorrencia

        self.table = TableWidget(self)
        self.verticalLayout.addWidget(self.table)
        
        self.setEventos()

        self.seguroAtual = None

    def setEventos(self):
        self.b_novo.clicked.connect(self.addSeguro)
        self.b_limpar.clicked.connect(self.limparCampos)
        self.b_excluir.clicked.connect(self.excluirItem)

    def addSeguro(self):
        novoSeguro = self.getSeguros()
        if novoSeguro != None:
            if self.seguroAtual == None:
                self.table.add(novoSeguro)
            else:
                novoSeguro.id = self.seguroAtual.id
                self.table.update(novoSeguro)
            self.limparCampos()

    def getSeguros(self):
        indet = self.campIdent.text()
        valor = self.campValor.text()

        if (indet != "") and (valor != ""):
            return Ocorrencia (-1, self.campIdent.text(), self.campValor.text())
        return None

    def limparCampos(self):
        self.seguroAtual = None
        self.campIdent.setText("")
        self.campValor.setText("")

        self.b_novo.setText("Adicionar")
        self.b_excluir.setEnabled(False)
        self.b_limpar.setEnabled(False)

    def insereOcor(self, seguro):
        self.seguroAtual = seguro
        self.campIdent.setText(seguro.ident)
        self.campValor.setText(str("%.2f" %seguro.valor))

        self.b_novo.setText("Atualizar")
        self.b_excluir.setEnabled(True)
        self.b_limpar.setEnabled(True)

    def excluirItem(self):
        self.table.delete(self.seguroAtual)
        self.limparCampos()