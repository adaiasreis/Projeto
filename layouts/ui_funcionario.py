from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from clas.funcionario import Funcionario

class CadFuncionario(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_funcionario.ui", self)

    def setEventos(self):
        self.b_novo.clicked.connect(self.addFuncionario)
        self.b_limpar.clicked.connect(self.limparCampos)
        self.b_excluir.clicked.connect(self.excluirItem)

    def addFuncionario(self):
        novoFuncionario = self.getFuncionario()
        if novoFuncionario != None:
            if self.funcionarioAtual == None:
                self.table.add(novoFuncionario)
            else:
                novoFuncionario.id = self.funcionarioAtual.id
                self.table.update(novoFuncionario)
            self.limparCampos()

    def getFuncionarios(self):
        nome = self.campNome.text()
        rgNum = self.campRgn.text()
        orgaoExp = self.campRgo.text()
        rgDataEmis = self.campRgd.text()
        cpf = self.campCpf.text()
        telefone = self.campTelefone.text()
        nasc = self.campNasc.text()
        email = self.campEmail.text()
        endereco = self.campEndereco.text()
        nomeMae = self.campNmae.text()
        cargo = self.campCargo.text()
        salario = self.campSalario.text()
        cargahs = self.campCarga.text()
        usuario = self.campUsario.text()
        senha = self.campSenha.text()

        if ((nome != "") and (rgNum != "") and (orgaoExp != "") and (rgDataEmis != "") and (cpf != "") and (telefone != "") and (nasc != "") and (email != "") and (endereco != "") and (nomeMae != "") and (cargo != "") and (salario != "") and (cargahs != "") and (usuario != "" ) and (senha != "")):
            return Funcionario (-1, self.campNome.text(), self.campRgn.text(), self.campRgo.text(), self.campRgd.text(), self.campCpf.text(), self.campTelefone.text(), self.campNasc.text(), self.campEmail.text(), self.campendereco.text(), self.campNmae.text(), self.campCargo.text(), self.campSalario.text(), self.campCarga.text(), self.campUsuario.text(), self.campSenha.text())
        return None

    def limparCampos(self):
        self.funcionarioAtual = None
        self.campNome.text("")
        self.campRgn.text("")
        self.campRgo.text("")
        self.campRgd.text("")
        self.campCpf.text("")
        self.campTelefone.text("")
        self.campNasc.text("")
        self.campEmail.text("")
        self.campEndereco.text("")
        self.campNmae.text("")
        self.campCargo.text("")
        self.campSalario.text("")
        self.campCarga.text("")
        self.campUsario.text("")
        self.campSenha.text("")

        self.b_novo.setText("Adicionar")
        self.b_excluir.setEnabled(False)
        self.b_historico.setEnabled(False)

    def insereFuncionario(self, funcionario):
        self.funcionarioAtual = funcionario
        self.campNome.text(funcionario.nome)
        self.campRgn.text(funcionario.rgNum)
        self.campRgo.text(funcionario.orgaoExp)
        self.campRgd.text(funcionario.dataEmis)
        self.campCpf.text(funcionario.cpf)
        self.campTelefone.text(funcionario.telefone)
        self.campNasc.text(funcionario.nasc)
        self.campEmail.text(funcionario.email)
        self.campEndereco.text(funcionario.endereco)
        self.campNmae.text(funcionario.nomeMae)
        self.campCargo.text(funcionario.cargo)
        self.campSalario.text(funcionario.salario)
        self.campCarga.text(funcionario.cargahs)
        self.campUsario.text(funcionario.usuario)
        self.campSenha.text(funcionario.senha)

        self.b_novo.setText("Atualizar")
        self.b_excluir.setEnabled(True)
        self.b_historico.setEnabled(True)

    def excluirItem(self):
        self.table.delete(self.funcionarioAtual)
        self.limparCampos()