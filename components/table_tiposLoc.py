from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem

import models.model_tipoLoc as Tipos

class TableTipo(QTableWidget):
    def __init__(self, parent):
        super().__init__(0, 4)
        self.parent = parent

        headers = ["ID","IDENTIFICAÇÃO","VALOR DA DIARIA (R$)","VALOR POR KM (R$)"]
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
        self.lista_tipos = Tipos.getTipos()
        self.setRowCount(0)
        for tipo in self.lista_tipos:
            self._addRow(tipo)

    def _addRow(self, tipo):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        id_id = QTableWidgetItem(str(tipo.id))
        id_indet = QTableWidgetItem(tipo.ident)
        id_v_diaria = QTableWidgetItem(str(tipo.v_diaria))
        id_v_kmEst = QTableWidgetItem(str(tipo.v_kmEst))
        id_v_kmExced = QTableWidgetItem(str(tipo.v_kmExced))
        self.setItem(rowCount, 0, id_id)
        self.setItem(rowCount, 1, id_indet)
        self.setItem(rowCount, 2, id_v_diaria)
        self.setItem(rowCount, 3, id_v_kmEst)
        self.setItem(rowCount, 4, id_v_kmExced)

    def on_click(self):
        selected_row = self.currentRow()
        id = self.item(selected_row, 0).text()
        tipo = Tipos.getTipo(id)
        self.parent.insereTipo(tipo)

    def add(self, tipo):
        Tipos.addTipo(tipo)
        # Carrega os dados do banco
        self.carregaDados()

    def update(self, tipo):
        Tipos.editTipo(tipo)
        # Carrega os dados do banco
        self.carregaDados()

    def delete(self, tipo):
        Tipos.delTipo(tipo.id)
        # Carrega os dados do banco
        self.carregaDados()