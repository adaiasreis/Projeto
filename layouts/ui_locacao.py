from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, uic

from components.table_locacoes import TableLocacao
from clas.locacao import Locacao

import models.model_reservas as Reservas

class CadLocacao(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ui_locacao.ui", self)

        self.table = TableLocacao(self)
        self.verticalLayout_2.addWidget(self.table)

        #self.setEventosCheckBox()

        self.carregaDadosReservas()

        self.setEventos()

        self.locacaoAtual = None
        self.reservaAtual = None
        self.lista_reservas = []
        self.lista_veiculos = []

    def setEventos(self):
        self.comboId.currentIndexChanged.connect(self.index_changed_reserva)
        self.b_locar.clicked.connect(self.addLocacao)
        self.b_limpar.clicked.connect(self.limparCampos)

    def carregaDadosReservas(self):
        self.lista_reservas = Reservas.getReservas()
        lista_combo = []
        for r in self.lista_reservas:
            lista_combo.append(str(r.id))
        self.comboId.addItems(lista_combo)

    def setEventosCheckBox(self):
        self.ch_mec.stateChanged.connect(self.checkBoxSeg())
        self.ch_perdaT.stateChanged.connect(self.checkBoxSeg())
        self.ch_furto.stateChanged.connect(self.checkBoxSeg())
        self.cb_guincho.stateChanged.connect(self.checkBoxSer())
        self.cb_gps.stateChanged.connect(self.checkBoxSer())
        self.cb_cadeirinha.stateChanged.connect(self.checkBoxSer())

    def index_changed_reserva(self, i):
        self.reservaAtual = self.lista_reservas[i]
        self.campValorPagar.setText(str(self.reservaAtual.valor_prev))

    def addLocacao(self):
        novoLocacao = self.getLocacao()
        if novoLocacao != None:
            if self.locacaoAtual == None:
                self.table.add(novoLocacao)
            else:
                novoLocacao = self.locacaoAtual.id
                self.table.update(novoLocacao)
            self.limparCampos()

    def getLocacao(self):
        id_res = self.comboId.currentText()
        kmAtual = self.campKmInic.text()
        kmEstim = self.campKmEstim.text()
        seguro = self.campCheckSeg.text()
        servicos = self.campCheckSer.text()
        valorLoc = self.campValorPagar.text()
        status = self.comboStatus.currentText()

        if ((id_res !="") and (kmAtual != "") and (kmEstim != "") and (seguro != "") and (servicos != "") and (valorLoc != "") and (status != "")):
            return Locacao (-1, self.comboId.currentText(), self.campKmInic.text(), self.campKmEstim.text(), self.campCheckSeg.text(), self.campCheckSer.text(), self.campValorPagar.text(), self.comboStatus.currentText())
        return None

    def limparCampos(self):
        self.locacaoAtual = None
        self.comboId.setCurrentText("")
        self.campKmInic.setText("")
        self.campKmEstim.setText("")
        self.campCheckSeg.setText("")
        self.campCheckSer.setText("")
        self.campValorPagar.setText("")
        self.comboStatus.setCurrentText("")

        self.b_locar.setText("Confirmar")
        self.b_limpar.setEnabled(False)

    def insereLocacao(self, locacao):
        self.locacaoAtual = locacao
        self.comboId.setCurrentText(str(locacao.id_res))
        self.campKmInic.setText(str(locacao.kmAtual))
        self.campKmEstim.setText(str(locacao.kmEstim))
        self.campCheckSeg.setText(str(locacao.seguro))
        self.campCheckSer.setText(str(locacao.servicos))
        self.campValorPagar.setText(str(locacao.valorLoc))
        self.comboStatus.setCurrentText(locacao.status)

        self.b_locar.setText("Atualizar")
        self.b_limpar.setEnabled(True)

    def checkBoxSeg(self):
        items = 0
        if self.ch_mec.isChecked():
            items =+ 1
        if self.ch_perdaT.isChecked():
            items =+ 1
        if self.ch_furto.isChecked():
            items =+ 1
        self.campCheckSeg.setText(str(items))

    def checkBoxSer(self, state):
        items = 0
        if state == QtCore.Qt.Checked:
            items =+ 1
        self.campCheckSer.setText(items)