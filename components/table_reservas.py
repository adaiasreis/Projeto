from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon
from layouts.ui_locacao import CadLocacao

import models.model_reservas as Reservas

class TableReserva(QTableWidget):
    def __init__(self, parent):
        super().__init__(0, 8)
        self.parent = parent

        headers = ["ID","CLIENTE","TIPO DA LOCAÇÃO","VEÍCULO","DATA PREVISTA","DIARIAS" ,"VALOR PREVIO R$","STATUS"]
        self.setHorizontalHeaderLabels(headers)

        self.configTable()

        self.carregaDados()

    def configTable(self):
        self.verticalHeader().setVisible(False)
        # ajusta as colunas ao tamanho da tela
        self.horizontalHeader().setStretchLastSection(False)
        self.horizontalHeader().setSectionResizeMode(0,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(2,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(3,QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(4,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(5,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(6,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(7,QHeaderView.ResizeToContents)
        # Alterna as cores das linhas
        self.setAlternatingRowColors(True)
        # desabilita a edição dos campos
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.setSelectionBehavior(QTableWidget.SelectRows)
        # evento ao selecionar uma linha
        self.clicked.connect(self.on_click)
    
    def carregaDados(self):
        self.lista_reservas = Reservas.getReservas()
        # necessário marcar a linha como a primeira para sobreescrever os dados da tabela
        self.setRowCount(0)
        for reserva in self.lista_reservas:
            self._addRow(reserva)

    def _addRow(self, reserva):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        # fixa a linha e muda a coluna conforme os valores
        id_item = QTableWidgetItem(str(reserva.id))
        id_cliente = QTableWidgetItem(reserva.cliente)
        id_tipo = QTableWidgetItem(reserva.tipo)
        id_veiculo = QTableWidgetItem(reserva.veiculo)
        id_dataLoc = QTableWidgetItem(reserva.dp_saida)
        id_diarias = QTableWidgetItem(str(reserva.diarias))
        id_valorPrev = QTableWidgetItem(str(reserva.valor_prev))
        id_status = QTableWidgetItem(reserva.status)
        # insere os itens na tabela
        self.setItem(rowCount, 0, id_item)
        self.setItem(rowCount, 1, id_cliente)
        self.setItem(rowCount, 2, id_tipo)
        self.setItem(rowCount, 3, id_veiculo)
        self.setItem(rowCount, 4, id_dataLoc)
        self.setItem(rowCount, 5, id_diarias)
        self.setItem(rowCount, 6, id_valorPrev)
        self.setItem(rowCount, 7, id_status)

    def on_click(self):
        selected_row = self.currentRow()
        id = self.item(selected_row, 0).text()
        reserva = Reservas.getReserva(id)
        self.parent.insereReserva(reserva)
    
    # funções para adicionar no banco de dados
    def add(self, reserva):
        Reservas.addReserva(reserva)
        # Carrega os dados do banco
        self.carregaDados()

    def update(self, reserva):
        Reservas.editReserva(reserva)
        # Carrega os dados do banco
        self.carregaDados()

    def delete(self, reserva):
        Reservas.delReserva(reserva.id)
        # Carrega os dados do banco
        self.carregaDados()

class IconHistoricot(QWidget):
    def __init__(self, reserva):
        super(IconHistoricot, self).__init__()
        self.reserva = reserva
        self.btn = QPushButton(self)
        self.btn.setText("")  # text
        self.btn.setIcon(QIcon("icons/icon_locacao..png"))  # icon
        self.btn.clicked.connect(self.cadLocacao())
        self.btn.setToolTip(
            "Histórico de compras do cliente.")  # Tool tip
        # remove a cor de fundo do botão e a borda
        self.btn.setStyleSheet(
            'QPushButton {background-color: #00FFFFFF; border:  none}')
        self.btn.setIconSize(QSize(20, 20))

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 10)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def abrirHistorico(self):
        self.hreserva = CadLocacao(self.reserva)
        self.hreserva.show()
