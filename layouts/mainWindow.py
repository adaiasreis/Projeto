import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ui_mainWindow.ui",self)

        #self.fazerLogin()

    def carregarJanelas(self):
        self.stackedWidget.insertWidget(0, CadProdutos())
        self.stackedWidget.insertWidget(1, CadClientes())
        self.stackedWidget.insertWidget(2, Vendas(self))
        self.stackedWidget.insertWidget(3, NovaVenda())

    def display(self):

        pass