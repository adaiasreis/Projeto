from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem

import models.model_locacao as Locacoes

class TableLocacao(QTableWidget):
    def __init__(self, parent):
        super().__init__(0, 5)
        self.parent = parent

        headers = ["CLIENTE","VEÍCULO","USO ESTIMADO (KM)", "DATA PREV RETORNO","STATUS"]
        self.setHorizontalHeaderLabels(headers)

        self.configTable()

        self.carregaDados()

    def configTable(self):
        self.verticalHeader().setVisible(False)
        # ajusta as colunas ao tamanho da tela
        self.horizontalHeader().setStretchLastSection(False)
        self.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(2,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(3,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(4,QHeaderView.ResizeToContents)
        # Alterna as cores das linhas
        self.setAlternatingRowColors(True)
        # desabilita a edição dos campos
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.setSelectionBehavior(QTableWidget.SelectRows)
        # evento ao selecionar uma linha
        self.clicked.connect(self.on_click)
    
    def carregaDados(self):
        self.lista_locacoes = Locacoes.getLocacoes()
        # necessário marcar a linha como a primeira para sobreescrever os dados da tabela
        self.setRowCount(0)
        for locacao in self.lista_locacoes:
            self._addRow(locacao)

    def _addRow(self, locacao):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        # fixa a linha e muda a coluna conforme os valores
        id_cliente = QTableWidgetItem(locacao.cliente)
        id_tipo = QTableWidgetItem(locacao.tipo)
        id_veiculo = QTableWidgetItem(locacao.veiculo)
        id_dataLoc = QTableWidgetItem(locacao.dataLoc)
        id_status = QTableWidgetItem(locacao.status)
        # insere os itens na tabela
        self.setItem(rowCount, 0, id_cliente)
        self.setItem(rowCount, 1, id_tipo)
        self.setItem(rowCount, 2, id_veiculo)
        self.setItem(rowCount, 3, id_dataLoc)
        self.setItem(rowCount, 4, id_status)

    def on_click(self):
        selected_row = self.currentRow()
        id = self.item(selected_row, 0).text()
        locacao = Locacoes.getLocacao(id)
        self.parent.insereLocacao(locacao)
    
    # funções para adicionar no banco de dados
    def add(self, locacao):
        Locacoes.addLocacao(locacao)
        # Carrega os dados do banco
        self.carregaDados()

    def update(self, locacao):
        Locacoes.editLocacao(locacao)
        # Carrega os dados do banco
        self.carregaDados()

    def delete(self, locacao):
        Locacoes.delLocacao(locacao.id)
        # Carrega os dados do banco
        self.carregaDados()