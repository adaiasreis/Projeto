from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
import sys

class FazerLogin(QWidget):
    def __init__(self, parent):
        super().__init__()
        uic.loadUi("ui/ui_login.ui",self)

        self.parent = parent

    def fazerLogin(self):

        while(True):

            self.l_info.setText("")
            usuario = ""
            senha = ""
            
            usuario = self.campUsuario.text()
            senha = self.campSenha.text()

            self.login = Usuarios.getLogin(usuario, senha)
            print(self.login)
            
            if  len(self.login) > 0:
                self.scre = self.parent.MainWindow(self)
                self.scre.show()
                self.hide()
                self.limpaCampos()
                        
            else:
                self.l_info.setText("Dados de login incorretos. Tente novamente.")
                self.limpaCampos()
            break
    
    def limpaCampos(self):
        self.newUser = None
        self.campUser.setText("")
        self.campPassw.setText("")