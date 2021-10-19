from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from components.table_veiculos import TableWidget
from clas.veiculo import Veiculo

class CadVeiculos(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_veiculo.ui", self)

        self.table = TableWidget(self)
        self.verticalLayout.addWidget(self.table)

        self.setEventos()

        self.veiculoAtual = None

    def setEventos(self):
        self.b_novo.clicked.connect(self.addVeiculo)
        self.b_limpar.clicked.connect(self.limparCampos)
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
        cor = self.campCor.text()
        categ = self.campCateg.text()
        anoF = self.campAnoF.text()
        placa = self.campPlaca.text()
        chassi = self.campChassi.text()
        renavam = self.campRenavam.text()
        capPassag = self.campCapPassag.text()
        portas = self.campPortas.text()
        potencia = self.campPotencia.text()
        cilindradas = self.campCilindradas.text()
        
        if ((marca != "") and (modelo != "") and (cor != "") and (categ != "") and (anoF != "") and (placa != "") and (chassi != "") and (renavam != "") and (capPassag != "") and (portas != "") and (potencia != "") and (cilindradas != "")):
            return Veiculo(-1, self.campMarca.text(), self.campModelo.text(), self.campCor.text(), self.campCateg.text(), self.campAnoF.text(), self.campPlaca.text(), self.campChassi.text(), self.campRenavam.text(), self.campCapPassag.text(), self.campPortas.text(), self.campPotencia.text(), self.campCilindradas.text())
        return None

    def limparCampos(self):
        self.veiculoAtual = None
        self.campMarca.setText("")
        self.campModelo.setText("")
        self.campCor.setText("")
        self.campCateg.setText("")
        self.campAnoF.setText("")
        self.campPlaca.setText("")
        self.campChassi.setText("")
        self.campRenavam.setText("")
        self.campCapPassag.setText("")
        self.campPortas.setText("")
        self.campPotencia.setText("")
        self.campCilindradas.setText("")

        self.b_novo.setText("Adicionar")
        self.b_excluir.setEnabled(False)
        self.b_limpar.setEnabled(False)

    def insereVeiculo(self, veiculo):
        self.veiculoAtual = veiculo
        self.campMarca.setText(veiculo.marca) 
        self.campModelo.setText(veiculo.modelo)
        self.campCor.setText(veiculo.cor)
        self.campCateg.setText(veiculo.categ)
        self.campAnoF.setText(veiculo.anoFab)
        self.campPlaca.setText(veiculo.placa)
        self.campChassi.setText(veiculo.chassi)
        self.campRenavam.setText(veiculo.renavam)
        self.campCapPassag.setText(str(veiculo.capPassag))
        self.campPortas.setText(str(veiculo.portas))
        self.campPotencia.setText(str(veiculo.potencia))
        self.campCilindradas.setText(str(veiculo.cilindradas))

        self.b_novo.setText("Atualizar")
        self.b_excluir.setEnabled(True)
        self.b_limpar.setEnabled(True)

    def excluirItem(self):
        self.table.delete(self.veiculoAtual)
        self.limparCampos()