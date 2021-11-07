from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem
import models.model_servico as Servicos

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
        self.lista_servicos = Servicos.getServicos()
        # necessário marcar a linha como a primeira para sobreescrever os dados da tabela
        self.setRowCount(0)
        for servico in self.lista_servicos:
            self._addRow(servico)
    
    def _addRow(self, servico):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        # fixa a linha e muda a coluna conforme os valores
        id_item = QTableWidgetItem(str(servico.id))
        id_ident = QTableWidgetItem(servico.ident)
        id_valor = QTableWidgetItem(str("%.2f" %servico.valor))
        # insere os itens na tabela
        self.setItem(rowCount, 0, id_item)
        self.setItem(rowCount, 1, id_ident)
        self.setItem(rowCount, 2, id_valor)

    def on_click(self):
        selected_row = self.currentRow()
        id = self.item(selected_row, 0).text()
        servico = Servicos.getServico(id)
        self.parent.insereServico(servico)
    
    # funções para adicionar no banco de dados
    def add(self, servico):
        Servicos.addServico(servico)
        # Carrega os dados do banco
        self.carregaDados()

    def update(self, servico):
        Servicos.editServico(servico)
        # Carrega os dados do banco
        self.carregaDados()

    def delete(self, servico):
        Servicos.delPlano(servico.id)
        # Carrega os dados do banco
        self.carregaDados()