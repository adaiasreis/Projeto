from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem
import models.model_funcionario as Funcionarios

class TableWidget(QTableWidget):
    def __init__(self, parent):
        super().__init__(0, 6)
        self.parent = parent

        headers = ["ID","NOME","CPF","TELEFONE","EMAIL","CARGO"]
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
        self.horizontalHeader().setSectionResizeMode(3,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(4,QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(5,QHeaderView.ResizeToContents)
        # Alterna as cores das linhas
        self.setAlternatingRowColors(True)
        # desabilita a edição dos campos
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.setSelectionBehavior(QTableWidget.SelectRows)
        # evento ao selecionar uma linha
        self.clicked.connect(self.on_click)

    def carregaDados(self):
        self.lista_funcionarios = Funcionarios.getFuncs()
        # necessário marcar a linha como a primeira para sobreescrever os dados da tabela
        self.setRowCount(0)
        for func in self.lista_funcionarios:
            self._addRow(func)

    def _addRow(self, func):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        # fixa a linha e muda a coluna conforme os valores
        id_item = QTableWidgetItem(str(func.id))
        id_nome = QTableWidgetItem(func.nome)
        id_cpf= QTableWidgetItem(func.cpf)
        id_telefone = QTableWidgetItem(func.telefone)
        id_email = QTableWidgetItem(func.email)
        id_cargo = QTableWidgetItem(func.cargo)
        # insere os itens na tabela
        self.setItem(rowCount, 0, id_item)
        self.setItem(rowCount, 1, id_nome)
        self.setItem(rowCount, 2, id_cpf)
        self.setItem(rowCount, 3, id_telefone)
        self.setItem(rowCount, 4, id_email)
        self.setItem(rowCount, 5, id_cargo)

    def on_click(self):
        selected_row = self.currentRow()
        id = self.item(selected_row, 0).text()
        func = Funcionarios.getFunc(id)
        self.parent.insereFunc(func)
    
    # funções para adicionar no banco de dados
    def add(self, func):
        Funcionarios.addFunc(func)
        # Carrega os dados do banco
        self.carregaDados()

    def update(self, func):
        Funcionarios.editFunc(func)
        # Carrega os dados do banco
        self.carregaDados()

    def delete(self, func):
        Funcionarios.delFunc(func.id)
        # Carrega os dados do banco
        self.carregaDados()
