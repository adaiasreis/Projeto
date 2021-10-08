from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from clas.veiculo import Veiculo

class CadVeiculo(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_veiculo.ui", self)

    
    def setEventos(self):
        self.b_novo.clicked.connect(self.addVeiculo)
        self.b_limpar.clicked.connect(self.limpaCampos)
        self.b_excluir.clicked.connect(self.excluirItem)
    
    def addVeiculo(self):
        novoVeiculo = self.getVeiculos()
        if novoVeiculo != None:
            if self.veiculoAtual == None:
                self.table.add(novoVeiculo)
            else:
                novoVeiculo.id = self.veiculoAtual.id
                self.table.update(novoVeiculo)
            
            self.limparCampos()

    def getVeiculos(self):
        marca = self.campMarca.text()
        modelo = self.campModelo.text()
        tipo = self.campTipo.text()
        categ = self.campCateg.text()
        anoFab = self.campAnoFab.text()
        placa = self.campPlaca.text()
        chassi = self.campChassi.text()
        renavam = self.campRenavam.text()
        capPassag = self.campCapPassag.text()
        potencia = self.campPotencia.text()
        cilindradas = self.campCilindradas.text()
        
        if ((marca != "") and (modelo != "") and (tipo != "") and (categ != "") and (anoFab != "") and (placa != "") and (chassi != "") and (renavam != "") and (capPassag != "") and (potencia != "") and (cilindradas != "")):
            return Veiculo(-1, self.campMarca.text(), self.campModelo.text(), self.campTipo.tex(), self.campCateg.text(), self.campanoFab.text(), self.campPlaca.text(), self.campChassi.text(), self.campRenavam.text(), self.campCapPassag.text(), self.campPotencia.text(), self.campCilindradas.text())
        return None

    def limpaCampos(self):
        self.veiculoAtual = None
        self.campMarca.setText() = ""
        self.campModelo.setText() = ""
        self.campTipo.setText() = ""
        self.campCateg.setText() = ""
        self.campAnoFab.setText() = ""
        self.campPlaca.setText() = ""
        self.campChassi.setText() = ""
        self.campRenavam.setText() = ""
        self.campCapPassag.setText() = ""
        self.campPotencia.setText() = ""
        self.campCilindradas.setText() = ""

        self.b_novo.setText("Adicionar")
        self.b_excluir.setEnabled(False)
        self.b_historico.setEnabled(False)

    def insereVeiculo(self, veiculo):
        self.veiculoAtual = veiculo
        self.campMarca.setText(veiculo.marca) 
        self.campModelo.setText(veiculo.modelo)
        self.campTipo.setText(veiculo.tipo)
        self.campCateg.setText(veiculo.categ)
        self.campAnoFab.setText(veiculo.anoFab)
        self.campPlaca.setText(veiculo.placa)
        self.campChassi.setText(veiculo.chassi)
        self.campRenavam.setText(veiculo.renavam)
        self.campCapPassag.setText(veiculo.capPassag)
        self.campPotencia.setText(veiculo.potencia)
        self.campCilindradas.setText(veiculo.cilindradas)

        self.b_novo.setText("Atualizar")
        self.b_excluir.setEnabled(True)
        self.b_historico.setEnabled(True)

    def excluirItem(self):
        self.table.delete(self.veiculoAtual)
        self.limpaCampos()