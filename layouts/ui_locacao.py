from PyQt5.QtWidgets import QDateEdit, QWidget, QTabWidget, QVBoxLayout
from PyQt5.QtCore import QDateTime
from PyQt5 import uic

from components.table_locacoes import *
from clas.locacao import *

import models.model_cliente as Clientes
import models.model_veiculo as Veiculos

class MyTabWidget(QWidget):
    def __init__(self, parent = None):
        super(MyTabWidget, self).__init__(parent)
        uic.loadUi("ui/ui_locacao.ui", self)

        self.tab1 = QWidget(CadReserva())
        self.tab2 = QWidget(CadLocacao())
        self.tab3 = QWidget()

        self.dataInic.setDateTime(QDateTime.currentDateTime())
        self.dataFim.setDateTime(QDateTime.currentDateTime())

        """#self.setTabIndex(0)
            
        self.addTab(self.tab1,"Tab 1")
        self.addTab(self.tab2,"Tab 2")
        self.addTab(self.tab3,"Tab 3")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
		
    def tab1UI(self):
        self.setTabText(0,"Reserva")
        self.reservaAtual = None

    def tab2UI(self):
        self.setTabText(1,"Locação")
            
    def tab3UI(self):
      self.setTabText(2,"Tabela de Preços")"""

class CadReserva(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ui_locacao.ui", self)

        self.table = TableReserva(self)
        self.verticalLayout.addWidget(self.table)
        
        self.reservaAtual = None
        self.clienteAtual = None
        self.veiculoAtual = None
        self.lista_clientes = []
        self.lista_veiculos = []

        self.setEventos()

        self.carregaDadosCliente()
        self.carregaDadosVeiculo()

    def carregaDadosCliente(self):
        self.lista_clientes = Clientes.getClientes()
        print(self.lista_clientes)
        lista_combo = []
        for c in self.lista_clientes:
            lista_combo.append(c.nome)
        self.comboClienteR.addItems(lista_combo)

    def carregaDadosVeiculo(self):
        self.lista_veiculos = Veiculos.getVeiculos()
        lista_combo = []
        for v in self.lista_veiculos:
            lista_combo.append(v.marca)
        self.comboMarcaR.addItems(lista_combo)

    def setEventos(self):
        self.comboClienteR.currentIndexChanged.connect(self.index_changed_cliente)
        self.comboMarcaR.currentIndexChanged.connect(self.index_changed_veiculo)
        self.b_reserva.clicked.connect(self.addReserva)
        self.b_limpar.clicked.connect(self.limparCampos)

    def index_changed_cliente(self, i):
        self.clienteAtual = self.lista_clientes[i]
        self.campId_cli.setText(str(self.lista_clientes[i].id))
        #self.camoPlano.setText(self.lista_cliente[i].plano)

    def index_changed_veiculo(self, i):
        self.veiculoAtual = self.lista_veiculos[i]
        self.campId_vei.setText(str(self.lista_veiculos[i].id))
        self.comboMarcaR.setCurrentText(self.lista_veiculos[i].marca)
        self.campModeloR.setText(self.lista_veiculos[i].modelo)

    def addReserva(self):
        novoReserva = self.getReservas()
        if novoReserva != None:
            if self.reservaAtual == None:
                self.table.add(novoReserva)
            self.limparCampos()

    def getReservas(self):
        id_cliente = self.campId_cli.text()
        cliente = self.comboCliente.currentText()
        plano = self.campPlano.text()
        tipo = self.comboTipo.currentText()
        id_veiculo = self.campId_vei.text()
        veiculo = self.comboVeiculo.currentText()
        data_inic = self.dataInic.dateTime().toString('dd/MM/yyyy')
        data_fim = self.dataFim.dateTime().toString('dd/MM/yyyy')
        status = self.comboStatus.text()

        if ((id_cliente != "") and (cliente != "") and (plano != "") and (tipo != "") and (id_veiculo != "") and (veiculo != "") and (data_inic != "") and (data_fim != "") and (status != "")):
            return Reserva (-1, self.campId_cli.text(), self.comboCliente.currentText(), self.campPlano.text(), self.comboTipo.currentText(), self.campId_vei.text(), self.comboVeiculo.currentText(),
                self.dataInic.dateTime().toString('dd/MM/yyyy'), self.dataFim.dateTime().toString('dd/MM/yyyy'), self.comboStatus.currentText())
        return None

    def limparCampos(self):
        self.reservaAtual = None
        self.campId_cli.setText("")
        self.comboCliente.currentText("")
        self.campPlano.setText("")
        self.comboTipo.setText("")
        self.campId_vei.setText("")
        self.comboVeiculo.setText("")
        self.data_inic.setDateTime("")
        self.dataFim.setDateTime("")
        self.comboStatus.currentText("")

        self.b_reserva.setText("Reservar")
        self.b_limpar.setEnabled(False)

    def insereReserva(self, reserva):
        self.reservaAtual = reserva
        self.campId_cli.setText(reserva.id_cliente)
        self.comboCliente.currentText(reserva.cliente)
        self.campPlano.setText(reserva.plano)
        self.comboTipo.setText(reserva.tipo)
        self.campId_vei.setText(reserva.id_veiculo)
        self.campVeiculo.setText(reserva.veiculo)
        self.data_inic.setDataTime(reserva.data_inic)
        self.campVeiculo.setText(reserva.data_fim)
        self.comboStatus.currentText(reserva.status)

        self.b_reserva.setText("Atualizar")
        self.b_limpar.setEnabled(True)

class CadLocacao(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ui_locacao.ui", self)

        self.table = TableLocacao(self)
        self.verticalLayout.addWidget(self.table)

        self.locacaoAtual = None

        self.setEventos()

    def setEventos(self):
        self.b_locar.clicked.connect(self.addLocacao)
        self.b_limpar_2.clicked.connect(self.limparCampos)

    def addLocacao(self):
        novoLocacao = self.getLocacao()
        if novoLocacao != None:
            if self.locacaoAtual == None:
                self.table.add(novoLocacao)
            self.limparCampos()

    def getLocacao(self):
        id_res = self.comboId_reserva.currentText()
        kmAtual = self.campKmInic.text()
        kmEstim = self.campKmEstim.text()
        seguro = self.comboSeguro.currentText()
        taxa = self.comboTaxas.currentText()
        servicos = self.groupServicos.currentText()
        valorLoc = self.campValorPagar.text()
        status = self.comboStatus.currentText()

        if ((id_res !="") and (kmAtual != "") and (kmEstim != "") and (seguro != "") and (taxa != "") and (servicos != "") and (valorLoc != "") and (status != "")):
            return Locacao (-1, self.comboId_reserva.currentText(), self.campKmInic.text(), self.campKmEstim.text(), self.comboSeguro.currentText(), self.comboTaxas.currentText(),
                self.groupServicos.currentText(), self.campValorPagar.text(), self.comboStatus.currentText())
        return None

    def limparCampos(self):
        self.locacaoAtual = None
        self.comboId_reserva.currentText("")
        self.campKmInic.text("")
        self.campKmEstim.text("")
        self.comboSeguro.currentText("")
        self.comboTaxas.currentText("")
        self.groupServicos.currentText("")
        self.campValorPagar.text("")

        self.b_locar.setText("Locar")
        self.b_limpar_2.setEnabled(False)

    def insereLocacao(self, locacao):
        self.locacaoAtual = locacao
        self.comboId_reserva.currentText(locacao.id_reserva)
        self.campKmInic.text(locacao.kmAtual)
        self.campKmEstim.text(locacao.kmEstim)
        self.comboSeguro.currentText(locacao.seguro)
        self.comboTaxas.currentText(locacao.taxa)
        self.groupServicos.currentText(locacao.servicos)
        self.campValorPagar.text(locacao.valorLoc)

        self.b_locar.setText("Atualizar")
        self.b_limpar.setEnabled(True)










            
    

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
        self.setLayout(self.layout)
        
        
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
        self.b_limpar.setEnabled(True)"""