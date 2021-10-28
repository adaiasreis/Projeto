from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QDate
from PyQt5 import uic
from datetime import datetime

from components.table_reservas import TableReserva
from clas.locacao import Reserva
from layouts.ui_tipoLoc import CadTipos

import models.model_cliente as Clientes
import models.model_veiculo as Veiculos
import models.model_tipoLoc as Tipos
import models.model_reservas as Reservas

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
        self.lista_tipos = []
        self.lista_reservas = []

        self.editData_inic.setDate(QDate.currentDate())
        self.editData_fim.setDate(QDate.currentDate())

        self.setEventos()

        self.carregaDadosCliente()
        self.carregaDadosVeiculo()
        self.carregaDadosTipos()
        self.carregaListaReservas()

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
            for r in self.lista_reservas:
                while v.id == r.veiculo_id:
                    print(r.veiculo.id)
                    lista_combo.append(r.marca)
                self.comboVeiculos.addItems(lista_combo)

    def carregaDadosTipos(self):
        self.lista_tipos = Tipos.getTipos()
        lista_combo = []
        for t in self.lista_tipos:
            lista_combo.append(t.ident)
        self.comboTipos.addItems(lista_combo)

    def carregaListaReservas(self):
        self.lista_reservas = Reservas.getReservas()
        print(self.lista_reservas)
        return self.lista_reservas

    def setEventos(self):
        self.comboCliente.currentIndexChanged.connect(self.index_changed_cliente)
        self.comboVeiculos.currentIndexChanged.connect(self.index_changed_veiculo)
        self.b_reserva.clicked.connect(self.addReserva)
        self.b_limpar.clicked.connect(self.limparCampos)
        self.b_tipos.clicked.connect(self.tiposLoc)

    def index_changed_cliente(self, i):
        self.clienteAtual = self.lista_clientes[i]
        self.campId_cli.setText(str(self.clienteAtual.id))
        self.campPlano.setText(self.clienteAtual.plano)

    def index_changed_veiculo(self, i):
        self.veiculoAtual = self.lista_veiculos[i]
        self.campId_vei.setText(str(self.veiculoAtual.id))
        self.campModelo.setText(self.veiculoAtual.modelo)

    def tiposLoc(self, winTipos):
        self.abrirTipos = CadTipos(self)
        self.abrirTipos.show()

    def addReserva(self):
        novoReserva = self.getReservas()
        if novoReserva != None:
            if self.reservaAtual == None:
                self.table.add(novoReserva)
            else:
                novoReserva.id = self.reservaAtual.id
                self.table.update(novoReserva)
            self.limparCampos()

    def getReservas(self):
        id_cliente = self.campId_cli.text()
        cliente = self.comboCliente.currentText()
        plano = self.campPlano.text()
        tipo = self.comboTipos.currentText()
        id_veiculo = self.campId_vei.text()
        veiculo = self.comboVeiculos.currentText()
        data_inic = self.editData_inic.date().toString('dd/MM/yyyy')
        data_fim = self.editData_fim.date().toString('dd/MM/yyyy')
        valor_prev = self.campValorP.text()
        status = self.comboStatus.currentText()

        if ((id_cliente != "") and (cliente != "") and (plano != "") and (tipo != "") and (id_veiculo != "") and (veiculo != "") and (data_inic != "") and (data_fim != "") and(valor_prev != "") and (status != "")):
            return Reserva (-1, self.campId_cli.text(), self.comboCliente.currentText(), self.campPlano.text(), self.comboTipos.currentText(), self.campId_vei.text(), self.comboVeiculos.currentText(), self.editData_inic.dateTime().toString('dd/MM/yyyy'),
                    self.editData_fim.dateTime().toString('dd/MM/yyyy'), self.campValorP.text(), self.comboStatus.currentText())
        return None

    def limparCampos(self):
        self.reservaAtual = None
        self.campId_cli.setText("")
        self.comboCliente.setCurrentText("")
        self.campPlano.setText("")
        self.comboTipos.setText("")
        self.campId_vei.setText("")
        self.comboVeiculos.setCurrentText("")
        self.editData_inic.setDateTime("")
        self.editData_fim.setDateTime("")
        self.campValorP.setText("")
        self.comboStatus.setCurrentText("")

        self.b_reserva.setText("Reservar")
        self.b_limpar.setEnabled(False)

    def insereReserva(self, reserva):
        self.reservaAtual = reserva
        self.campId_cli.setText(str(reserva.id_cliente))
        self.comboCliente.setCurrentText(reserva.cliente)
        self.campPlano.setText(reserva.plano)
        self.comboTipos.setCurrentText(reserva.tipo)
        self.campId_vei.setText(str(reserva.id_veiculo))
        self.comboVeiculos.setCurrentText(reserva.veiculo)
        self.editData_inic.setCurrentText(reserva.data_inic)
        self.editData_fim.setCurrentText(reserva.data_fim)
        self.campValorP.setText(reserva.valor_prev)
        self.comboStatus.setCurrentText(reserva.status)

        self.b_reserva.setText("Atualizar")
        self.b_limpar.setEnabled(True)


