from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QDate
from PyQt5 import uic
from datetime import datetime

from components.table_reservas import TableReserva
from layouts.ui_locacao import CadLocacao
from clas.locacao import Reserva

import models.model_cliente as Clientes
import models.model_veiculo as Veiculos
import models.model_tipoLoc as Tipos

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
        self.tipo = ""

        self.editData_inic.setDate(QDate.currentDate())
        self.editData_fim.setDate(QDate.currentDate())

        self.setEventos()

        self.carregaDadosCliente()
        self.carregaDadosTipos()

    def carregaDadosCliente(self):
        self.lista_clientes = Clientes.getClientes()
        lista_combo = []
        for c in self.lista_clientes:
            lista_combo.append(c.nome)
        self.comboCliente.addItems(lista_combo)

    def carregaDadosVeiculo(self, categ):
        self.lista_veiculos = Veiculos.getVeiculosCateg(categ)
        lista_combo = []
        self.comboVeiculos.clear()
        for v in self.lista_veiculos:
            lista_combo.append(v.marca)
        self.comboVeiculos.addItems(lista_combo)

    def carregaDadosTipos(self):
        self.lista_tipos = Tipos.getTipos()
        lista_combo = []
        for t in self.lista_tipos:
            lista_combo.append(t.ident)
        self.comboTipos.addItems(lista_combo)

    def setEventos(self):
        self.comboCliente.currentIndexChanged.connect(self.index_changed_cliente)
        self.comboVeiculos.currentIndexChanged.connect(self.index_changed_veiculo)
        self.comboTipos.currentIndexChanged.connect(self.index_changed_tipos)
        #self.comboStatus.currentIndexChanged.connect(self.index_changed_status)
        self.b_reserva.clicked.connect(self.addReserva)
        self.b_limpar.clicked.connect(self.limparCampos)
        self.b_locar.clicked.connect(self.abrirLocacao)
        self.b_ok.clicked.connect(self.calculaDiferencaDias)

    def index_changed_cliente(self, i):
        self.clienteAtual = self.lista_clientes[i]
        self.campId_cli.setText(str(self.clienteAtual.id))
        self.campPlano.setText(self.clienteAtual.plano)

    def index_changed_veiculo(self, i):
        self.veiculoAtual = self.lista_veiculos[i]
        self.campId_vei.setText(str(self.veiculoAtual.id))
        self.campModelo.setText(self.veiculoAtual.modelo)

    def index_changed_tipos(self, i):
        global tipo
        if (i == 0):
            self.carregaDadosVeiculo("Hatch")
        elif(i == 1):
            self.carregaDadosVeiculo("Sedan")
        else:
            self.carregaDadosVeiculo("SUV")
        tipo = self.lista_tipos[i]
        self.campValorP.setText("%.2f" %tipo.v_diaria)

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
        diarias = self.campDiarias.text()
        valor_prev = self.campValorP.text()
        status = self.comboStatus.currentText()

        if ((id_cliente != "") and (cliente != "") and (plano != "") and (tipo != "") and (id_veiculo != "") and (veiculo != "") and (data_inic != "") and (data_fim != "") and(diarias != "") and(valor_prev != "") and (status != "")):
            return Reserva (-1, self.campId_cli.text(), self.comboCliente.currentText(), self.campPlano.text(), self.comboTipos.currentText(), self.campId_vei.text(), self.comboVeiculos.currentText(), self.editData_inic.dateTime().toString('dd/MM/yyyy'),
                    self.editData_fim.dateTime().toString('dd/MM/yyyy'), self.campDiarias.text(), self.campValorP.text(), self.comboStatus.currentText())
        return None

    def limparCampos(self):
        self.reservaAtual = None
        self.campId_cli.setText("")
        self.comboCliente.setCurrentIndex(0)
        self.campPlano.setText("")
        self.comboTipos.setCurrentIndex(0)
        self.campId_vei.setText("")
        self.comboVeiculos.setCurrentText("")
        self.editData_inic.setDate(QDate.currentDate())
        self.editData_fim.setDate(QDate.currentDate())
        self.campDiarias.setText("")
        self.campValorP.setText("")
        self.comboStatus.setCurrentIndex(0)

        self.b_reserva.setText("Reservar")
        self.b_limpar.setEnabled(False)
        self.b_excluir.setEnabled(False)
        self.b_locar.setEnabled(False)

    def insereReserva(self, reserva):
        self.reservaAtual = reserva
        self.campId_cli.setText(str(reserva.id_cliente))
        self.comboCliente.setCurrentText(reserva.cliente)
        self.campPlano.setText(reserva.plano)
        self.comboTipos.setCurrentText(reserva.tipo)
        self.campId_vei.setText(str(reserva.id_veiculo))
        self.comboVeiculos.setCurrentText(reserva.veiculo)
        data_saida = QDate.fromString(reserva.dp_saida, 'dd/MM/yyyy')
        self.editData_inic.setDate(data_saida)
        data_retorno = QDate.fromString(reserva.dp_retorno, 'dd/MM/yyyy')
        self.campDiarias.setText(str(reserva.diarias))
        self.editData_fim.setDate(data_retorno)
        self.campValorP.setText(str("%.2f" % reserva.valor_prev))
        self.comboStatus.setCurrentText(reserva.status)

        self.b_reserva.setText("Atualizar")
        self.b_limpar.setEnabled(True)
        self.b_excluir.setEnabled(True)
        self.b_locar.setEnabled(True)

    def calculaDiferencaDias(self):
        data1 = self.editData_inic.date().toString('dd/MM/yyyy')
        data2 = self.editData_fim.date().toString('dd/MM/yyyy')
        data_i = datetime.strptime(data1, '%d/%m/%Y')
        data_f = datetime.strptime(data2, '%d/%m/%Y')
        qtd_dias = abs((data_f - data_i).days)
        self.campDiarias.setText(str(qtd_dias))
        self.calculaValorDiarias(qtd_dias)

    def calculaValorDiarias(self, q):
        global tipo
        val_ds = 0.0
        val_d = tipo.v_diaria
        if val_d == "":
            val_d == 0.0
        else:
            val_d == float(val_d)

            val_ds = float(val_d) * float(q)
        self.campValorP.setText(str("%.2f" % val_ds))

    def abrirLocacao(self):
        self.hreserva = CadLocacao(self.reservaAtual, self)
        self.hreserva.show()
