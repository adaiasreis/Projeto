from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem
import models.model_plano as Planos

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
        self.lista_planos = Planos.getPlanos()
        # necessário marcar a linha como a primeira para sobreescrever os dados da tabela
        self.setRowCount(0)
        for plano in self.lista_planos:
            self._addRow(plano)
    
    def _addRow(self, plano):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        # fixa a linha e muda a coluna conforme os valores
        id_item = QTableWidgetItem(str(plano.id))
        id_ident = QTableWidgetItem(plano.ident)
        id_valor = QTableWidgetItem(str("%.2f" %plano.valor))
        # insere os itens na tabela
        self.setItem(rowCount, 0, id_item)
        self.setItem(rowCount, 1, id_ident)
        self.setItem(rowCount, 2, id_valor)

    def on_click(self):
        selected_row = self.currentRow()
        id = self.item(selected_row, 0).text()
        ocor = Planos.getPlano(id)
        self.parent.inserePlano(ocor)
    
    # funções para adicionar no banco de dados
    def add(self, plano):
        Planos.addPlano(plano)
        # Carrega os dados do banco
        self.carregaDados()

    def update(self, plano):
        Planos.editPlano(plano)
        # Carrega os dados do banco
        self.carregaDados()

    def delete(self, plano):
        Planos.delPlano(plano.id)
        # Carrega os dados do banco
        self.carregaDados()