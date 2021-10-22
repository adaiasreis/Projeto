from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from tkinter import *

from layouts.ui_mainWindow import MainWindow
import models.model_funcionario as Funcionarios

class FazerLogin(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ui_telaLogin.ui",self)

        self.into = Tk()

        self.setEventos()

    def setEventos(self):
        self.b_entrar.clicked.connect(self.fazerLogin)
        self.b_sair.clicked.connect(self.Sair)

    def clicker(self):
        self.into.bind('<Return>', self.fazerLogin())


    def fazerLogin(self):

        while(True):

            self.l_info.setText("")
            usuario = ""
            senha = ""
            
            usuario = self.campUsuario.text()
            senha = self.campSenha.text()

            self.login = Funcionarios.getLogin(usuario, senha)
            
            if  len(self.login) > 0:
                self.scre = MainWindow(self, self.login[0])
                self.scre.show()
                self.hide()
                self.limpaCampos()
                        
            else:
                self.l_info.setText("Dados de login incorretos. Tente novamente.")
                self.limpaCampos()
            break
    
    def limpaCampos(self):
        self.newUser = None
        self.campUsuario.setText("")
        self.campSenha.setText("")

    def Sair(self):
        self.close()