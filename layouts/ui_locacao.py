from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, uic

#from components.table_locacoes import TableLocacao
from clas.locacao import Locacao as Loc

import models.model_reserva as Reservas
import models.model_plano as Planos

class CadLocacao(QWidget):
    def __init__(self, reservaAtual, winReserva):
        super().__init__()
        uic.loadUi("ui/ui_locacao.ui", self)

        self.reservaAtual = reservaAtual
        self.winReserva = winReserva
        
        """self.table = TableLocacao(self)
        self.verticalLayout_2.addWidget(self.table)"""

        self.locacaoAtual = None
        self.lista_reservas = []

        self.setEventos()

        self.setEventosCheckBox()

        self.campId_reserva.setText(str(self.reservaAtual.id))

    def setEventos(self):
        self.b_locar.clicked.connect(self.addLocacao)
        self.b_limpar.clicked.connect(self.limparCampos)
        self.b_ok.clicked.connect(self.carregaDadosPlanos)

    def carregaDadosReservas(self):
        self.lista_reservas = Reservas.getReservas()
        lista_combo = []
        for r in self.lista_reservas:
            lista_combo.append(str(r.id))
        self.campId.addItems(lista_combo)

    def carregaDadosPlanos(self, tipoLoc):
        tipoLoc = self.winReserva.comboTipos.currentText()
        self.lista_planos = Planos.getPlanosCateg(tipoLoc)
        for p in self.lista_planos:
            valorkm = p.valorKmEst
            self.calculaKm(valorkm)

    def setEventosCheckBox(self):
        self.ch_mec.stateChanged.connect(self.checkBoxSeg)
        self.ch_perdaT.stateChanged.connect(self.checkBoxSeg)
        self.ch_furto.stateChanged.connect(self.checkBoxSeg)
        self.cb_guincho.stateChanged.connect(self.checkBoxSer)
        self.cb_gps.stateChanged.connect(self.checkBoxSer)
        self.cb_cadeirinha.stateChanged.connect(self.checkBoxSer)

    def addLocacao(self):
        novoLocacao = self.getLocacao()
        if novoLocacao != None:
            if self.locacaoAtual == None:
                self.table.add(novoLocacao)
            else:
                novoLocacao.id = self.locacaoAtual.id
                self.table.update(novoLocacao)
            self.limparCampos()

    def getLocacao(self):
        id_res = self.campId_reserva.text()
        kmAtual = self.campKmInic.text()
        kmEstim = self.campKmEstim.text()
        #self.campKmEstim.returnPressed.connect(self.calculaKm)
        status = self.comboStatus.currentText()

        if ((id_res !="") and (kmAtual != "") and (kmEstim != "") and (status != "")):
            return Loc (-1, self.campId_reserva.text(), self.campKmInic.text(), self.campKmEstim.text(), self.comboStatus.currentText())
        return None

    def limparCampos(self):
        self.locacaoAtual = None
        self.campId_reserva.setText("")
        self.campKmInic.setText("")
        self.campKmEstim.setText("")
        self.comboStatus.setCurrentText("")

        self.b_locar.setText("Confirmar")
        self.b_limpar.setEnabled(False)
        self.campId_reserva.setEnabled(True)

    def insereLocacao(self, locacao):
        self.locacaoAtual = locacao
        self.campId_reserva.setText(str(locacao.id_res))
        self.campKmInic.setText(str(locacao.kmAtual))
        self.campKmEstim.setText(str(locacao.kmEstim))
        self.comboStatus.setCurrentText(locacao.status)

        self.b_locar.setText("Atualizar")
        self.b_limpar.setEnabled(True)
        self.campId_reserva.setEnabled(False)

    def calculaKm(self, valor):
        pagarKm = 0.0
        kmEstim = self.campKmEstim.text()
        if valor == "":
            valor == 0.0
        else:
            valor == float(valor)

        if kmEstim == "":
            kmEstim == 0.0
        else: 
            kmEstim == float(kmEstim)

            pagarKm = float(valor) * float(kmEstim)

        self.campValor.setText(str("%.2f" %pagarKm))
        self.calculaPagar(pagarKm)

    def calculaPagar(self, pagarKm):
        valorPag = 0.0
        valorIn = self.winReserva.campValorP.text()
        if valorIn == "":
            valorIn == 0.0
        else:
            valorIn == float(valorIn)
        if valorPag == "":
            valorPag == 0.0
        else:
            valorPag == (float(valorPag))

            valorPag = pagarKm + float(valorIn)
            self.campPagar.setText(str("%.2f" %valorPag))

    def checkBoxSeg(self):
        if self.ch_mec.isChecked():
            print("Marcou Mecânico")

        if self.ch_perdaT.isChecked():
            print("Marcou perda Total")

        if self.ch_furto.isChecked():
            print("Marcou Furto")

    def checkBoxSer(self, state):
        if self.cb_guincho.isChecked:
            print("Marcou guincho")

        if self.cb_gps.isChecked:
            print("Marcou gps")
         
        if self.cb_cadeirinha.isChecked:
            print("Marcou cadeirinha")