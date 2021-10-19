from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem
import models.model_cliente as Clientes

class TableWidget(QTableWidget):
    def __init__(self, parent):
        super().__init__(0, 10)
        self.parent = parent

        headers = ["ID","NOME","RG","CNH","CATEGORIA","CPF","TELEFONE","DATA NASC","EMAIL","NOME MÃE"]
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
        self.horizontalHeader().setSectionResizeMode(4,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(5,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(6,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(7,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(8,QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(9,QHeaderView.Stretch)
        # Alterna as cores das linhas
        self.setAlternatingRowColors(True)
        # desabilita a edição dos campos
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.setSelectionBehavior(QTableWidget.SelectRows)
        # evento ao selecionar uma linha
        self.clicked.connect(self.on_click)
    
    def carregaDados(self):
        self.lista_clientes = Clientes.getClientes()
        # necessário marcar a linha como a primeira para sobreescrever os dados da tabela
        self.setRowCount(0)
        for cliente in self.lista_clientes:
            self._addRow(cliente)

    def _addRow(self, cliente):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        # fixa a linha e muda a coluna conforme os valores
        id_item = QTableWidgetItem(str(cliente.id))
        id_nome = QTableWidgetItem(cliente.nome)
        id_rg= QTableWidgetItem(cliente.rgNum)
        id_cnh = QTableWidgetItem(cliente.cnhNum)
        id_categ = QTableWidgetItem(cliente.categ)
        id_cpf = QTableWidgetItem(cliente.cpf)
        id_telefone = QTableWidgetItem(cliente.telefone)
        id_nasc = QTableWidgetItem(cliente.nasc)
        id_email = QTableWidgetItem(cliente.email)
        id_nomeMae = QTableWidgetItem(cliente.nomeMae)
        # insere os itens na tabela
        self.setItem(rowCount, 0, id_item)
        self.setItem(rowCount, 1, id_nome)
        self.setItem(rowCount, 2, id_rg)
        self.setItem(rowCount, 3, id_cnh)
        self.setItem(rowCount, 4, id_categ)
        self.setItem(rowCount, 5, id_cpf)
        self.setItem(rowCount, 6, id_telefone)
        self.setItem(rowCount, 7, id_nasc)
        self.setItem(rowCount, 8, id_email)
        self.setItem(rowCount, 9, id_nomeMae)

    def on_click(self):
        selected_row = self.currentRow()
        id = self.item(selected_row, 0).text()
        cliente = Clientes.getCliente(id)
        self.parent.insereCliente(cliente)
    
    # funções para adicionar no banco de dados
    def add(self, cliente):
        Clientes.addCliente(cliente)
        # Carrega os dados do banco
        self.carregaDados()

    def update(self, cliente):
        Clientes.editCliente(cliente)
        # Carrega os dados do banco
        self.carregaDados()

    def delete(self, cliente):
        Clientes.delCliente(cliente.id)
        # Carrega os dados do banco
        self.carregaDados()