from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import uic

from clas.locacao import Tipo
from components.table_tiposLoc import TableTipo

class CadTipos(QWidget):
    def __init__(self, winReserva):
        super().__init__()
        uic.loadUi("ui/ui_tipoLoc.ui", self)

        self.winReserva = winReserva

        self.table = TableTipo(self)
        self.verticalLayout.addWidget(self.table)

        self.tipoAtual = None

        self.setEventos()

    def setEventos(self):
        self.b_novo.clicked.connect(self.addTipo)
        self.b_limpar.clicked.connect(self.limparCampos)

    def addTipo(self):
        novoTipo = self.getTipo()
        if novoTipo != None:
            if self.tipoAtual == None:
                self.table.add(novoTipo)
            else:
                novoTipo.id = self.tipoAtual.id
                if novoTipo == self.tipoAtual:
                    self.messageInfo()
                else:
                    self.table.update(novoTipo)
            self.limparCampos()

    def getTipo(self):
        ident = self.campIdent.text()
        v_diaria = self.camp_valDia.text()
        v_kmEst = self.camp_valKm.text()
        v_kmExced = self.campValK_exc.text()

        if ((ident != "") and (v_diaria != "") and (v_kmEst != "") and (v_kmExced != "")):
            return Tipo (-1, self.campIdent.text(), self.camp_valDia.text(), self.camp_valKm.text(), self.campValK_exc.text())
        return None

    def limparCampos(self):
        self.tipoAtual = None
        self.campIdent.setText("")
        self.camp_valDia.setText("")
        self.camp_valKm.setText("")
        self.campValK_exc.setText("")

        self.b_novo.setText("Adicionar")
        self.b_limpar.setEnabled(False)

    def insereTipo(self, tipo):
        self.tipoAtual = tipo
        self.campIdent.setText(tipo.ident)
        self.camp_valDia.setText(str(tipo.v_diaria))
        self.camp_valKm.setText(str(tipo.v_kmEst))
        self.campValK_exc.setText(str(tipo.v_kmExced))

        self.b_novo.setText("Atualizar")
        self.b_limpar.setEnabled(True)

    def messageInfo(self):
        em = QMessageBox()
        em.setIcon(QMessageBox.Information)
        em.setText("A atualização não foi concluída porque não houve alteração em nenhum campo.")
        em.setInformativeText("Caso seja necessário atualizar, por favor altera pelo menos um campo.")
        em.setWindowTitle("Atualização Não Concluída")
        em.exec()