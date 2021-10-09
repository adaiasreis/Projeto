from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from clas.locacao import Locacao

class CadLocacao(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_locacao.ui", self)

    def setEventos(self):
        self.b_novo.clicked.connect(self.addLocacao)
        self.b_limpar.clicked.connect(self.limparCampos)

    def addLocacao(self):
        novoLocacao = self.getLocacoes()
        if novoLocacao != None:
            if self.locacaoAtual == None:
                self.table.add(novoLocacao)
            self.limparCampos()

    def getLocacoes(self):
        dataLoc = self.dataInic.text()
        veiculo = self.comboVeiculo.currentText()
        cliente = self.comboCliente.currentText()
        kmAtual = self.campKmInic.text()
        hora = self.horaIn.text()
        kmEstim = self.compKmEstim.text()
        seguro = self.comboSeguro.currentText()
        taxa = self.comboTaxa.currentText()
        valorLoc = self.campValorPagar.text()
        status = self.g_status.text()
        dataEnt = self.dataFinal.text()
        kmEnt = self.campKmEnt.text()
        infoEnt = self.campInform.text()

        if ((dataLoc != "") and (veiculo != "") and (cliente != "") and (kmAtual != "") and (hora != "") (kmEstim != "") and (seguro != "") and (taxa != "") and (valorLoc != "") and (status != "") and (dataEnt != "") and (kmEnt != "") and (infoEnt != "")):
            return Locacao (-1, self.compDataInic.text(), self.comboVeiculo.currentText(), self.comboCliente.currentText(), self.campKmInic.text(), self.horaIn.text(), self.campKmEstim.text(), self.comboSeguro.currentText(), self.comboTaxa.currentText(), self.campValorPagar.text(), self.g_status.text(), self.dataFinal.text(), self.campKmEnt.text(), self.campInform.text())
        return None

    def limparCampos(self):
        self.funcionarioAtual = None
        self.dataInic.text("")
        self.comboVeiculo.currentText("")
        self.comboCliente.currentText("")
        self.campKmInic.text("")
        self.horaIn.text("")
        self.compKmEstim.text("")
        self.comboSeguro.currentText("")
        self.comboTaxa.currentText("")
        self.campValorPagar.text("")
        self.g_status.text("")
        self.dataFinal.text("")
        self.campKmEnt.text("")
        self.campInform.text("")

        self.b_novo.setText("Adicionar")
        self.b_excluir.setEnabled(False)
        self.b_historico.setEnabled(False)

    def insereLocacao(self, locacao):
        self.funcionarioAtual = locacao
        self.dataInic.text(locacao.dataLoc)
        self.comboVeiculo.currentText(locacao.veiculo)
        self.comboCliente.currentText(locacao.cliente)
        self.campKmInic.text(locacao.kmAtual)
        self.horaIn.text(locacao.hora)
        self.compKmEstim.text(locacao.kmEstim)
        self.comboSeguro.currentText(locacao.seguro)
        self.comboTaxa.currentText(locacao.taxa)
        self.campValorPagar.text(locacao.valorLoc)
        self.g_status.text(locacao.status)
        self.dataFinal.text(locacao.dataEnt)
        self.campKmEnt.text(locacao.kmEnt)
        self.campInform.text(locacao.infoEnt)

        self.b_novo.setText("Atualizar")
        self.b_excluir.setEnabled(True)
        self.b_historico.setEnabled(True)