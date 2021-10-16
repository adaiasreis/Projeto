import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

from layouts.ui_inicio import Inicio
from layouts.ui_veiculo import CadVeiculos
from layouts.ui_cliente import CadClientes
from layouts.ui_funcionario import CadFuncionarios
from layouts.ui_ocorrencia import CadOcorrencias
from layouts.ui_locacao import CadLocacoes

class MainWindow(QMainWindow):
    def __init__(self, janelaLogin, usuarioAtual):
        super().__init__()
        uic.loadUi("ui/ui_mainWindow.ui",self)
        self.janelaLogin = janelaLogin

        self.usuarioAtual = usuarioAtual

        self.listWidget.setCurrentRow(0)

        self.carregarJanelas()

        self.listWidget.currentRowChanged.connect(self.display)

        self.statusBar.showMessage("Seja bem vindo "+ self.usuarioAtual['nome'])

    def carregarJanelas(self):
        self.stackedWidget.insertWidget(0, Inicio())
        self.stackedWidget.insertWidget(1, CadVeiculos())
        self.stackedWidget.insertWidget(2, CadClientes())
        self.stackedWidget.insertWidget(3, CadFuncionarios())
        self.stackedWidget.insertWidget(4, CadOcorrencias())
        self.stackedWidget.insertWidget(5, CadLocacoes())
        #self.stackedWidget.insertWidget(6, Ajuda())
        #self.stackedWidget.insertWidget(7, Sobre())

    def display(self, index):
        # necessário carregar as janelas a cada trasição para atualizar as informações
        self.carregarJanelas()
        self.stackedWidget.setCurrentIndex(index)
        self.listWidget.setCurrentRow(index)

    def closeEvent(self, event):
        self.janelaLogin.show()