class Banco:
    valorDeposito = 0
    soma = 0

    def __init__(self, nome, tipoConta, numConta, numAgencia, saldo, chequeEspecial, statusConta=True):
        self.nome = nome
        self.tipoConta = tipoConta
        self.numConta = numConta
        self.numAgencia = numAgencia
        self.saldo = float(saldo)
        self.statusConta = statusConta
        self.chequeEspecial = chequeEspecial

    def verificarSaldo(self):
        print(self.saldo)

    def deposito(self, valor):
        self.valor = float(valor)
        if self.valor >= 0 and self.statusConta == True:
            self.saldo += self.valor
            print(f'o valor depositado foi {self.valor}')

    def saque(self, valor):
        self.valor = valor
        if self.valor >= 0 and self.statusConta == True:
            self.saldo -= self.valor
            print(f'o valor sacado foi {self.valor}')

    def desativarConta(self):
        if self.saldo == 0 and self.statusConta == True:
            self.statusConta == False
            print(f'conta desativada {self.statusConta}')
        else:
            print(f'sua conta já está desativada.')

    def ativarLimite(self, valor):
        self.valor = valor
        print(f'você ativou seu limite, o limite é de {self.valor}')

    def informacaoConta(self):
        info = (f'Essa conta pertence a {self.nome}. \n '
              f'Conta: {self.numConta} \n Agência: {self.numAgencia} \n Tipo de conta: {self.tipoConta} \n Saldo: {self.saldo}')
        return info

    def comprovanteBancario(self):
        with open("comprovanteBancario.txt", "a") as arquivo:
            arquivo.write(self.informacaoConta() + '\n')
            print("As informações da conta foram registradas no comprovante.")

    def abrirComprovante(self):
        with open("comprovanteBancario.txt", "r", encoding="latin-1") as arquivo:
            comprovante = arquivo.read()
            print(comprovante)

conta1 = Banco("maria jose", "corrente", "41254", "001", 0, 0)
conta1.deposito(300)
conta1.saque(150)
conta1.verificarSaldo()
conta1.abrirComprovante()
