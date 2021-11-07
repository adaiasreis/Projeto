from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem
import models.model_seguro as Seguros

class TableWidget(QTableWidget):
    def __init__(self, parent):
        super().__init__(0, 3)
        self.parent = parent

        headers = ["ID","IDENTIFICAÇÃO","VALOR"]
        self.setHorizontalHeaderLabels(headers)

        self.configTable()

        self.carregaDados()

    def configTable(self):
        self.verticalHeader().setVisible(False)
        # ajusta as colunas ao tamanho da tela
        self.horizontalHeader().setStretchLastSection(False)
        self.horizontalHeader().setSectionResizeMode(0,QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        # Alterna as cores das linhas
        self.setAlternatingRowColors(True)
        # desabilita a edição dos campos
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.setSelectionBehavior(QTableWidget.SelectRows)
        # evento ao selecionar uma linha
        self.clicked.connect(self.on_click)

    def carregaDados(self):
        self.lista_seguros = Seguros.getSeguros()
        # necessário marcar a linha como a primeira para sobreescrever os dados da tabela
        self.setRowCount(0)
        for seguro in self.lista_seguros:
            self._addRow(seguro)
    
    def _addRow(self, seguro):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        # fixa a linha e muda a coluna conforme os valores
        id_item = QTableWidgetItem(str(seguro.id))
        id_ident = QTableWidgetItem(seguro.ident)
        id_valor = QTableWidgetItem(str("%.2f" %seguro.valor))
        # insere os itens na tabela
        self.setItem(rowCount, 0, id_item)
        self.setItem(rowCount, 1, id_ident)
        self.setItem(rowCount, 2, id_valor)

    def on_click(self):
        selected_row = self.currentRow()
        id = self.item(selected_row, 0).text()
        seguro = Seguros.getSeguro(id)
        self.parent.insereSeguro(seguro)
    
    # funções para adicionar no banco de dados
    def add(self, seguro):
        Seguros.addSeguro(seguro)
        # Carrega os dados do banco
        self.carregaDados()

    def update(self, seguro):
        Seguros.editSeguro(seguro)
        # Carrega os dados do banco
        self.carregaDados()

    def delete(self, seguro):
        Seguros.delSeguro(seguro.id)
        # Carrega os dados do banco
        self.carregaDados()