from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from layouts.ui_servico import CadServicos
from layouts.ui_seguro import CadSeguros
from layouts.ui_plano import CadPlanos
from layouts.ui_tipoLoc import CadTipos

class Ocorrencias(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_ocorrencia.ui", self)

        self.setEventos()

    def setEventos(self):
        self.b_servicos.clicked.connect(self.cadServicos)
        self.b_seguros.clicked.connect(self.cadSeguros)
        self.b_planos.clicked.connect(self.cadPlanos)
        self.b_tipos.clicked.connect(self.tiposLoc)

    def cadServicos(self, winServicos):
        self.abrirServicos = CadServicos(self)
        self.abrirServicos.show()

    def cadSeguros(self, winSeguros):
        self.abrirSeguros = CadSeguros(self)
        self.abrirSeguros.show()

    def cadPlanos(self, winPlanos):
        self.abrirPlanos = CadPlanos(self)
        self.abrirPlanos.show()

    def tiposLoc(self, winTipos):
        self.abrirTipos = CadTipos(self)
        self.abrirTipos.show()