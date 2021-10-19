from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem
import models.model_ocorrencia as Ocorrencias

class TableWidget(QTableWidget):
    def __init__(self, parent):
        super().__init__(0, 4)
        self.parent = parent

        headers = ["ID","TIPO","IDENTIFICAÇÃO","VALOR"]
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
        # Alterna as cores das linhas
        self.setAlternatingRowColors(True)
        # desabilita a edição dos campos
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.setSelectionBehavior(QTableWidget.SelectRows)
        # evento ao selecionar uma linha
        self.clicked.connect(self.on_click)

    def carregaDados(self):
        self.lista_ocors = Ocorrencias.getOcors()
        # necessário marcar a linha como a primeira para sobreescrever os dados da tabela
        self.setRowCount(0)
        for ocor in self.lista_ocors:
            self._addRow(ocor)
    
    def _addRow(self, ocor):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        # fixa a linha e muda a coluna conforme os valores
        id_item = QTableWidgetItem(str(ocor.id))
        id_tipo = QTableWidgetItem(ocor.tipo)
        id_ident = QTableWidgetItem(ocor.ident)
        id_valor = QTableWidgetItem(str(ocor.valor))
        # insere os itens na tabela
        self.setItem(rowCount, 0, id_item)
        self.setItem(rowCount, 1, id_tipo)
        self.setItem(rowCount, 2, id_ident)
        self.setItem(rowCount, 3, id_valor)

    def on_click(self):
        selected_row = self.currentRow()
        id = self.item(selected_row, 0).text()
        ocor = Ocorrencias.getOcor(id)
        self.parent.insereOcor(ocor)
    
    # funções para adicionar no banco de dados
    def add(self, ocor):
        Ocorrencias.addOcor(ocor)
        # Carrega os dados do banco
        self.carregaDados()

    def update(self, ocor):
        Ocorrencias.editOcor(ocor)
        # Carrega os dados do banco
        self.carregaDados()

    def delete(self, ocor):
        Ocorrencias.delOcor(ocor.id)
        # Carrega os dados do banco
        self.carregaDados()