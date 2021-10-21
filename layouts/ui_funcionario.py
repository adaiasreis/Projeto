from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import uic

from components.table_funcionarios import TableWidget
from clas.funcionario import Funcionario
import models.model_funcionario as Funcionarios

class CadFuncionarios(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_funcionario.ui", self)

        #Ajusta a tabela
        self.table = TableWidget(self)
        self.verticalLayout.addWidget(self.table)
        #Carrega os eventos
        self.setEventos()
        #Inicia o funcionario como vazio
        self.funcionarioAtual = None

    def setEventos(self):
        self.b_novo.clicked.connect(self.addFunc)
        self.b_limpar.clicked.connect(self.limparCampos)
        self.b_excluir.clicked.connect(self.excluirItem)

    def addFunc(self):
        novoFuncionario = self.getFuncs()
        print(novoFuncionario)
        print(self.funcionarioAtual)
        if novoFuncionario != None:
            if self.funcionarioAtual == None:
                self.table.add(novoFuncionario)
            else:
                novoFuncionario.id = self.funcionarioAtual.id
                self.table.update(novoFuncionario)
            self.limparCampos()

    def getFuncs(self):
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
        usuario = self.campUsuario.text()
        senha = self.campSenha.text()

        if ((nome != "") and (rgNum != "") and (orgaoExp != "") and (rgDataEmis != "") and (cpf != "") and (telefone != "") and (nasc != "") and (email != "") and (endereco != "") and (nomeMae != "") and (cargo != "") and (salario != "") and (cargahs != "") and (usuario != "" ) and (senha != "")):
            return Funcionario (-1, self.campNome.text(), self.campRgn.text(), self.campRgo.text(), self.campRgd.text(), self.campCpf.text(), self.campTelefone.text(), self.campNasc.text(), self.campEmail.text(), self.campEndereco.text(), self.campNmae.text(), self.campCargo.text(), self.campSalario.text(), self.campCarga.text(), self.campUsuario.text(), self.campSenha.text())
        return None

    def limparCampos(self):
        self.funcionarioAtual = None
        self.campNome.setText("")
        self.campRgn.setText("")
        self.campRgo.setText("")
        self.campRgd.setText("")
        self.campCpf.setText("")
        self.campTelefone.setText("")
        self.campNasc.setText("")
        self.campEmail.setText("")
        self.campEndereco.setText("")
        self.campNmae.setText("")
        self.campCargo.setText("")
        self.campSalario.setText("")
        self.campCarga.setText("")
        self.campUsuario.setText("")
        self.campSenha.setText("")

        self.b_novo.setText("Adicionar")
        self.campUsuario.setEnabled(True)
        self.b_excluir.setEnabled(False)
        self.b_limpar.setEnabled(False)
        
    def insereFunc(self, funcionario):
        self.funcionarioAtual = funcionario
        self.campNome.setText(funcionario.nome)
        self.campRgn.setText(funcionario.rgNum)
        self.campRgo.setText(funcionario.orgaoExp)
        self.campRgd.setText(funcionario.dataEmis)
        self.campCpf.setText(funcionario.cpf)
        self.campTelefone.setText(funcionario.telefone)
        self.campNasc.setText(funcionario.nasc)
        self.campEmail.setText(funcionario.email)
        self.campEndereco.setText(funcionario.endereco)
        self.campNmae.setText(funcionario.nomeMae)
        self.campCargo.setText(funcionario.cargo)
        self.campSalario.setText(str(funcionario.salario))
        self.campCarga.setText(str(funcionario.cargahs))
        self.campUsuario.setText(funcionario.usuario)
        self.campSenha.setText(funcionario.senha)

        self.b_novo.setText("Atualizar")
        self.b_excluir.setEnabled(True)
        self.b_limpar.setEnabled(True)
        self.campUsuario.setEnabled(False)

    def excluirItem(self):
        self.lista_funcionarios = Funcionarios.getFuncs()
        #Se houver somente um funcionario cadastrado o sistema não permite a exclusão
        if len(self.lista_funcionarios) == 1:
            self.messageError()
        else:
            self.table.delete(self.funcionarioAtual)
            self.limparCampos()
    
    def messageError(self):
        em = QMessageBox()
        em.setIcon(QMessageBox.Information)
        em.setText("A exclusão não foi permitida porque a tabela de Funcionários não pode ser vazia. Para completar esta ação, por favor cadastre um novo funcionário.")
        em.setInformativeText("Para mais informações, consulte o menu Ajuda")
        em.setWindowTitle("Exclusão Não Permitida")
        em.exec()