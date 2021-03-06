from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem
import models.model_veiculo as Veiculos

class TableWidget(QTableWidget):
    def __init__(self, parent):
        super().__init__(0, 7)
        self.parent = parent

        headers = ["ID","MARCA","MODELO","COR","CATEGORIA","ANO FAB","PLACA"]
        self.setHorizontalHeaderLabels(headers)

        self.configTable()

        self.carregaDados()

    def configTable(self):
        self.verticalHeader().setVisible(False)
        # ajusta as colunas ao tamanho da tela
        self.horizontalHeader().setStretchLastSection(False)
        self.horizontalHeader().setSectionResizeMode(0,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(3,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(4,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(5,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(6,QHeaderView.ResizeToContents)
        # Alterna as cores das linhas
        self.setAlternatingRowColors(True)
        # desabilita a edição dos campos
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.setSelectionBehavior(QTableWidget.SelectRows)
        # evento ao selecionar uma linha
        self.clicked.connect(self.on_click)

    def carregaDados(self):
        self.lista_veiculos = Veiculos.getVeiculos()
        # necessário marcar a linha como a primeira para sobreescrever os dados da tabela
        self.setRowCount(0)
        for veiculo in self.lista_veiculos:
            self._addRow(veiculo)

    def _addRow(self, veiculo):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        # fixa a linha e muda a coluna conforme os valores
        id_item = QTableWidgetItem(str(veiculo.id))
        id_marca = QTableWidgetItem(veiculo.marca)
        id_modelo= QTableWidgetItem(veiculo.modelo)
        id_cor = QTableWidgetItem(veiculo.cor)
        id_categ = QTableWidgetItem(veiculo.categ)
        id_anoFab = QTableWidgetItem(veiculo.anoFab)
        id_placa = QTableWidgetItem(veiculo.placa)
        # insere os itens na tabela
        self.setItem(rowCount, 0, id_item)
        self.setItem(rowCount, 1, id_marca)
        self.setItem(rowCount, 2, id_modelo)
        self.setItem(rowCount, 3, id_cor)
        self.setItem(rowCount, 4, id_categ)
        self.setItem(rowCount, 5, id_anoFab)
        self.setItem(rowCount, 6, id_placa)

    def on_click(self):
        selected_row = self.currentRow()
        id = self.item(selected_row, 0).text()
        veiculo = Veiculos.getVeiculo(id)
        self.parent.insereVeiculo(veiculo)
    
    # funções para adicionar no banco de dados
    def add(self, veiculo):
        Veiculos.addVeiculo(veiculo)
        # Carrega os dados do banco
        self.carregaDados()

    def update(self, veiculo):
        Veiculos.editVeiculo(veiculo)
        # Carrega os dados do banco
        self.carregaDados()

    def delete(self, veiculo):
        Veiculos.delVeiculo(veiculo.id)
        # Carrega os dados do banco
        self.carregaDados()