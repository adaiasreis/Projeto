from PyQt5.QtWidgets import QDateEdit, QWidget, QTabWidget, QVBoxLayout
from PyQt5.QtCore import QDateTime
from PyQt5 import uic

from components.table_locacoes import TableLocacao
from clas.locacao import Locacao

import models.model_reservas as Reservas

class CadLocacao(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ui_locacao.ui", self)

        self.table = TableLocacao(self)
        self.verticalLayout_2.addWidget(self.table)

        self.locacaoAtual = None
        self.reservaAtual = None
        self.lista_reservas = []

        self.setEventos()

        self.carregaDadosReservas()

    def carregaDadosReservas(self):
        self.lista_reservas = Reservas.getReservas()
        lista_combo = []
        for r in self.lista_reservas:
            lista_combo.append(r.id)
        self.comboId.addItems(lista_combo)

    def setEventos(self):
        self.comboId.currentIndexChanged.connect(self.index_changed_reserva)
        self.b_locar.clicked.connect(self.addLocacao)
        self.b_limpar_2.clicked.connect(self.limparCampos)

    def index_changed_reserva(self, i):
        self.reservaAtual = self.lista_reservas[i]
        self.campCli.setText(self.reservaAtual.nome)
        self.campVei.setText(self.reservaAtual.marca)

    def addLocacao(self):
        novoLocacao = self.getLocacao()
        if novoLocacao != None:
            if self.locacaoAtual == None:
                self.table.add(novoLocacao)
            self.limparCampos()

    def getLocacao(self):
        id_res = self.comboId.currentText()
        kmAtual = self.campKmInic.text()
        kmEstim = self.campKmEstim.text()
        seguro = self.comboSeguro.currentText()
        taxa = self.comboTaxas.currentText()
        servicos = self.groupServicos.currentText()
        valorLoc = self.campValorPagar.text()
        status = self.comboStatus.currentText()

        if ((id_res !="") and (kmAtual != "") and (kmEstim != "") and (seguro != "") and (taxa != "") and (servicos != "") and (valorLoc != "") and (status != "")):
            return Locacao (-1, self.comboId.currentText(), self.campKmInic.text(), self.campKmEstim.text(), self.comboSeguro.currentText(), self.comboTaxas.currentText(),
                self.groupServicos.currentText(), self.campValorPagar.text(), self.comboStatus.currentText())
        return None

    def limparCampos(self):
        self.locacaoAtual = None
        self.comboId.currentText("")
        self.campKmInic.text("")
        self.campKmEstim.text("")
        self.comboSeguro.currentText("")
        self.comboTaxas.currentText("")
        self.groupServicos.currentText("")
        self.campValorPagar.text("")

        self.b_locar.setText("Confirmar")
        self.b_limpar_2.setEnabled(False)

    def insereLocacao(self, locacao):
        self.locacaoAtual = locacao
        self.comboId.currentText(locacao.id_reserva)
        self.campKmInic.text(locacao.kmAtual)
        self.campKmEstim.text(locacao.kmEstim)
        self.comboSeguro.currentText(locacao.seguro)
        self.comboTaxas.currentText(locacao.taxa)
        self.groupServicos.currentText(locacao.servicos)
        self.campValorPagar.text(locacao.valorLoc)

        self.b_locar.setText("Atualizar")
        self.b_limpar.setEnabled(True)