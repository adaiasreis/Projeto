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

        self.setEventos()

        self.veiculoAtual = None

    def setEventos(self):
        self.b_novo.clicked.connect(self.addOcorrencias)
        self.b_limpar.clicked.connect(self.limparCampos)
        self.b_excluir.clicked.connect(self.excluirItem)

    def addOcorrencias(self):
        novoOcorrencia = self.getOcorrencias()
        if novoOcorrencia != None:
            if self.ocorrenciaAtual == None:
                self.table.add(novoOcorrencia)
            else:
                novoOcorrencia.id = self.ocorrenciaAtual.id
                self.table.update(novoOcorrencia)
            self.limparCampos()

    def getOcorrencias(self):
        tipo = self.camboTipo.currentText()
        indet = self.campIden.text()
        valor = self.campVal.text()

        if ((tipo != "") and (indet != "") and (valor != "")):
            return Ocorrencia (-1, self.comboTipo.currentText(), self.campIden.text(), self.campVal.text())
        return None

    def limparCampos(self):
        self.OcorrenciaAtual = None
        self.comboTipo.text("Selecione...")
        self.campIdent("")
        self.campValor.text("")

        self.b_novo.setText("Adicionar")
        self.b_excluir.setEnabled(False)
        self.b_limpar.setEnabled(False)

    def insereOcorrencia(self, ocorrencia):
        self.ocorrenciaAtual = ocorrencia
        self.comboTipo.text(ocorrencia.tipo)
        self.campIdent.text(ocorrencia.campIdent)
        self.campValor.text(ocorrencia.campValor)

        self.b_novo.setText("Atualizar")
        self.b_excluir.setEnabled(True)
        self.b_limpar.setEnabled(True)

    def excluirItem(self):
        self.table.delete(self.Ocorrenciatual)
        self.limparCampos()