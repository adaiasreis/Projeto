from PyQt5.QtWidgets import QDateEdit, QWidget, QTabWidget, QVBoxLayout
from PyQt5.QtCore import QDateTime
from PyQt5 import uic

from components.table_reservas import TableReserva
from clas.locacao import Reserva

import models.model_cliente as Clientes
import models.model_veiculo as Veiculos

class CadReserva(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ui_reserva.ui", self)

        self.table = TableReserva(self)
        self.verticalLayout.addWidget(self.table)
    
        self.reservaAtual = None
        self.clienteAtual = None
        self.veiculoAtual = None
        self.lista_clientes = []
        self.lista_veiculos = []

        self.dataInic.setDateTime(QDateTime.currentDateTime())
        self.dataFim.setDateTime(QDateTime.currentDateTime())

        self.setEventos()

        self.carregaDadosCliente()
        self.carregaDadosVeiculo()

    def carregaDadosCliente(self):
        self.lista_clientes = Clientes.getClientes()
        lista_combo = []
        for c in self.lista_clientes:
            lista_combo.append(c.nome)
        self.comboCliente.addItems(lista_combo)

    def carregaDadosVeiculo(self):
        self.lista_veiculos = Veiculos.getVeiculos()
        lista_combo = []
        for v in self.lista_veiculos:
            lista_combo.append(v.marca)
        self.comboMarca.addItems(lista_combo)

    def setEventos(self):
        self.comboCliente.currentIndexChanged.connect(self.index_changed_cliente)
        self.comboMarca.currentIndexChanged.connect(self.index_changed_veiculo)
        self.b_reserva.clicked.connect(self.addReserva)
        self.b_limpar.clicked.connect(self.limparCampos)

    def index_changed_cliente(self, i):
        self.clienteAtual = self.lista_clientes[i]
        self.campId_cli.setText(str(self.clienteAtual.id))
        self.campPlano.setText(self.clienteAtual.plano)

    def index_changed_veiculo(self, i):
        self.veiculoAtual = self.lista_veiculos[i]
        self.campId_vei.setText(str(self.veiculoAtual.id))
        self.campModelo.setText(self.veiculoAtual.modelo)

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
        self.comboCliente.setCurrentText("")
        self.campPlano.setText("")
        self.comboTipo.setText("")
        self.campId_vei.setText("")
        self.comboVeiculo.setCUrrentText("")
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