from datetime import datetime as dt
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import QTimer
from PyQt5 import uic

from layouts.ui_inicio import Inicio
from layouts.ui_veiculo import CadVeiculos
from layouts.ui_cliente import CadClientes
from layouts.ui_funcionario import CadFuncionarios
from layouts.ui_ocorrencia import Ocorrencias
from layouts.ui_reserva import CadReserva
from layouts.ui_ajuda import Ajuda
from layouts.ui_sobre import Sobre

class MainWindow(QMainWindow):
    def __init__(self, janelaLogin, usuarioAtual):
        super().__init__()
        uic.loadUi("ui/ui_mainWindow.ui",self)
        self.janelaLogin = janelaLogin

        self.usuarioAtual = usuarioAtual

        timer = QTimer(self) 
        timer.timeout.connect(self.showTime) 
        timer.start(1000)

        self.carregarJanelas()

        self.listWidget.setCurrentRow(0)

        self.listWidget.currentRowChanged.connect(self.display)

    def showTime(self):
        now = dt.now()
        data = now.strftime("%d/%m/%Y %H:%M:%S")
        
        self.statusBar.showMessage("Seja bem vindo "+ self.usuarioAtual['nome'] + "  [" + data + "]")

    def carregarJanelas(self):
        self.stackedWidget.insertWidget(0, Inicio())
        self.stackedWidget.insertWidget(1, CadVeiculos())
        self.stackedWidget.insertWidget(2, CadClientes())
        self.stackedWidget.insertWidget(3, CadFuncionarios())
        self.stackedWidget.insertWidget(4, Ocorrencias())
        self.stackedWidget.insertWidget(5, CadReserva())
        self.stackedWidget.insertWidget(6, Ajuda())
        self.stackedWidget.insertWidget(7, Sobre())

    def display(self, index):
        # necessário carregar as janelas a cada trasição para atualizar as informações
        self.carregarJanelas()
        self.stackedWidget.setCurrentIndex(index)
        self.listWidget.setCurrentRow(index)

    def closeEvent(self, event):
        self.janelaLogin.show()
        