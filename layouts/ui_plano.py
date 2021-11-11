from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from components.table_planos import TableWidget
from clas.ocorrencia import Plano

import models.model_tipoLoc as Tipos

class CadPlanos(QWidget):
    def __init__(self, janelaOcorrencia):
        super(). __init__()
        uic.loadUi("ui/ui_plano.ui", self)

        self.janelaOcorrencia = janelaOcorrencia

        self.table = TableWidget(self)
        self.verticalLayout.addWidget(self.table)

        self.planoAtual = None
        
        self.setEventos()

        self.carregaDadosTipos()

    def setEventos(self):
        self.combo_tipoLoc.currentIndexChanged.connect(self.index_changed_tipoLoc)
        self.b_novo.clicked.connect(self.addPlano)
        self.b_limpar.clicked.connect(self.limparCampos)
        self.b_excluir.clicked.connect(self.excluirItem)

    def carregaDadosTipos(self):
        self.lista_tipos = Tipos.getTipos()
        lista_combo = []
        for t in self.lista_tipos:
            lista_combo.append(t.ident)
        self.combo_tipoLoc.addItems(lista_combo)

    def index_changed_tipoLoc(self, i):
        self.tipoLoc = self.lista_tipos[i]
        self.camp_valDia.setText(str("%.2f" %self.tipoLoc.v_diaria))
        self.camp_valEst.setText(str("%.2f" %self.tipoLoc.v_kmEst))
        self.camp_valExced.setText(str("%.2f" %self.tipoLoc.v_kmExced))

    def addPlano(self):
        novoPlano = self.getPlanos()
        if novoPlano != None:
            if self.planoAtual == None:
                self.table.add(novoPlano)
            else:
                novoPlano.id = self.planoAtual.id
                self.table.update(novoPlano)
            self.limparCampos()

    def getPlanos(self):
        indet = self.campIdent.text()
        valor = self.campValor.text()
        tipoLoc = self.combo_tipoLoc.currentText()
        valorDia = self.camp_valDia.text()
        valorKmEst = self.camp_valEst.text()
        valorKmExced = self.camp_valExced.text()
        b_valorDia = self.camp_bValDia.text()
        b_valorEst = self.camp_bValEst.text()
        b_valorExced = self.camp_bValExced.text()

        if (indet != "") and (valor != "") and (tipoLoc != "") and (valorDia != "", (valorKmEst != "") and (valorKmExced != "") and (b_valorDia != "") and (b_valorEst != "") and (b_valorExced != "")):
            return Plano (-1, self.campIdent.text(), self.campValor.text(), self.combo_tipoLoc.currentText(), self.camp_valDia.text(), self.camp_valEst.text(), self.camp_valExced.text(), self.camp_bValDia.text(), self.camp_bValEst.text(), self.camp_bValExced.text())
        return None

    def limparCampos(self):
        self.planoAtual = None
        self.campIdent.setText("")
        self.campValor.setText("")
        self.combo_tipoLoc.setCurrentIndex(0)
        self.camp_valDia.setText("")
        self.camp_valEst.setText("")
        self.camp_valExced.setText("")
        self.camp_bValDia.setText("")
        self.camp_bValEst.setText("")
        self.camp_bValExced.setText("")

        self.b_novo.setText("Adicionar")
        self.b_excluir.setEnabled(False)
        self.b_limpar.setEnabled(False)

    def inserePlano(self, plano):
        self.planoAtual = plano
        self.campIdent.setText(plano.ident)
        self.campValor.setText(str("%.2f" %plano.valor))
        self.combo_tipoLoc.setCurrentText(plano.tipoLoc)
        self.camp_valDia.setText(str("%.2f" %plano.valorDia))
        self.camp_valEst.setText(str("%.2f" %plano.valorKmEst))
        self.camp_valExced.setText(str("%.2f" %plano.valorKmExced))
        self.camp_bValDia.setText(str(plano.b_valorDia))
        self.camp_bValEst.setText(str(plano.b_valorEst))
        self.camp_bValExced.setText(str(plano.b_valorExced))

        self.b_novo.setText("Atualizar")
        self.b_excluir.setEnabled(True)
        self.b_limpar.setEnabled(True)

    def excluirItem(self):
        self.table.delete(self.planoAtual)
        self.limparCampos()