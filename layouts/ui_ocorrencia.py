from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from components.table_ocorrencias import TableWidget
from clas.ocorrencia import Ocorrencia

class CadOcorrencias(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_servicos.ui", self)

        self.table = TableWidget(self)
        self.verticalLayout.addWidget(self.table)

        self.index_changed_tipos()
        
        self.setEventos()

        self.ocorrenciaAtual = None

    def setEventos(self):
        self.b_novo.clicked.connect(self.addOcor)
        self.b_limpar.clicked.connect(self.limparCampos)
        self.b_excluir.clicked.connect(self.excluirItem)

    def index_changed_tipos(self):
        self.comboTipo.addItems(["Selecione...", "Seguro", "Serviço", "Taxa Especial"])

    def addOcor(self):
        novoOcorrencia = self.getOcor()
        if novoOcorrencia != None:
            if self.ocorrenciaAtual == None:
                self.table.add(novoOcorrencia)
            else:
                novoOcorrencia.id = self.ocorrenciaAtual.id
                self.table.update(novoOcorrencia)
            self.limparCampos()

    def getOcor(self):
        tipo = self.comboTipo.currentText()
        indet = self.campIdent.text()
        valor = self.campValor.text()

        if ((tipo != "Selecione...") and (indet != "") and (valor != "")):
            return Ocorrencia (-1, self.comboTipo.currentText(), self.campIdent.text(), self.campValor.text())
        return None

    def limparCampos(self):
        self.ocorrenciaAtual = None
        self.comboTipo.setCurrentIndex(0)
        self.campIdent.setText("")
        self.campValor.setText("")

        self.b_novo.setText("Adicionar")
        self.b_excluir.setEnabled(False)
        self.b_limpar.setEnabled(False)

    def insereOcor(self, ocorrencia):
        self.ocorrenciaAtual = ocorrencia
        self.comboTipo.setCurrentText(ocorrencia.tipo)
        self.campIdent.setText(ocorrencia.ident)
        self.campValor.setText(str(ocorrencia.valor))

        self.b_novo.setText("Atualizar")
        self.b_excluir.setEnabled(True)
        self.b_limpar.setEnabled(True)

    def excluirItem(self):
        self.table.delete(self.ocorrenciaAtual)
        self.limparCampos()