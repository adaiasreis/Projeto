import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ui_mainWindow.ui",self)

        #self.fazerLogin()
        self.carregarJanelas()

    def carregarJanelas(self):
        self.stackedWidget.insertWidget(0, CadVeiculos())
        self.stackedWidget.insertWidget(1, CadClientes())
        self.stackedWidget.insertWidget(2, CadFuncionarios(self))
        self.stackedWidget.insertWidget(3, Servicos())
        self.stackedWidget.insertWidget(4, Locacoes())

    def display(self):

        pass