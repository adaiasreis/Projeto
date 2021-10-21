from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout
from PyQt5.QtCore import QDateTime
from PyQt5 import uic

from components.table_locacoes import TableWidget
from clas.locacao import Locacao

class CadLocacoes(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_locacao.ui", self)

        self.table = TableWidget(self)
        self.verticalLayout.addWidget(self.table)

        self.locacaoAtual = None

        self.dataInic.setDateTime(QDateTime.currentDateTime())
        self.dataFinal.setDateTime(QDateTime.currentDateTime())

        self.setEventos()

    def setEventos(self):
        self.b_reserva.clicked.connect(self.addLocacao)
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
        self.locacaoAtual = None
        self.dataInic.setText("")
        self.comboVeiculo.currentText("")
        self.comboCliente.currentText("")
        self.campKmInic.setText("")
        self.horaIn.setText("")
        self.compKmEstim.setText("")
        self.comboSeguro.currentText("")
        self.comboTaxa.currentText("")
        self.campValorPagar.setText("")
        self.g_status.setText("")
        self.dataFinal.setText("")
        self.campKmEnt.setText("")
        self.campInform.setText("")

        self.b_novo.setText("Adicionar")
        self.b_excluir.setEnabled(False)
        self.b_limpar.setEnabled(False)

    def insereLocacao(self, locacao):
        self.locacaoAtual = locacao
        self.dataInic.setText(locacao.dataLoc)
        self.comboVeiculo.currentText(locacao.veiculo)
        self.comboCliente.currentText(locacao.cliente)
        self.campKmInic.setText(locacao.kmAtual)
        self.horaIn.setText(locacao.hora)
        self.compKmEstim.setText(locacao.kmEstim)
        self.comboSeguro.currentText(locacao.seguro)
        self.comboTaxa.currentText(locacao.taxa)
        self.campValorPagar.setText(locacao.valorLoc)
        self.g_status.setText(locacao.status)
        self.dataFinal.setText(locacao.dataEnt)
        self.campKmEnt.setText(locacao.kmEnt)
        self.campInform.setText(locacao.infoEnt)

        self.b_novo.setText("Atualizar")
        self.b_excluir.setEnabled(True)
        self.b_limpar.setEnabled(True)

class MyTabWidget(QWidget):
    def __init__(self, parent = None):
        super(MyTabWidget, self).__init__(parent)

        self.setTabIndex(0)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
            
        self.addTab(self.tab1,"Tab 1")
        self.addTab(self.tab2,"Tab 2")
        self.addTab(self.tab3,"Tab 3")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
		
    def tab1UI(self):

        self.setTabText(0,"Reserva")
            
    def tab2UI(self):
        self.setTabText(1,"Locação")
            
    def tab3UI(self):
      self.setTabText(2,"Tabela de Preços")

"""class MyTabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
  
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
  
        # Add tabs
        self.tabs.addTab(self.tab1, "Geeks")
        self.tabs.addTab(self.tab2, "For")
        self.tabs.addTab(self.tab3, "Geeks")
  
        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.l = QLabel()
        self.l.setText("This is the first tab")
        self.tab1.layout.addWidget(self.l)
        self.tab1.setLayout(self.tab1.layout)
  
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)"""