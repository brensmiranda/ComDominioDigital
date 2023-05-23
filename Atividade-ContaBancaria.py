
class Banco:
    soma = 0
    subtracao = 0
    desativar = "sim"

    def __init__(self, nome, tipoConta, numConta, numAgencia, saldo, statusConta=True):
        self.nome = nome
        self.tipoConta = tipoConta
        self.numConta = numConta
        self.numAgencia = numAgencia
        self.saldo = saldo
        self.statusConta = statusConta

    def deposito(self):
        valorDeposito = float(input("Quanto você quer depositar? "))

        if valorDeposito >= 0:
            self.saldo += valorDeposito
            self.soma += valorDeposito

    def transferencia(self):
        valorTransferencia = float(input("Quanto você quer transferir? "))

        if valorTransferencia >= 0 and self.saldo >= valorTransferencia:
            self.saldo -= valorTransferencia
            self.subtracao += valorTransferencia
        else:
            print("Saldo insuficiente para transferência.")

    def desativarConta(self):
        desativarConta = input("Você deseja desativar a conta? Digite sim ou não: ").lower()
        if self.saldo == 0:
            print("A conta pode ser desativada.")
        elif self.statusConta and desativarConta == self.desativar:
            self.statusConta = False
            print("Conta desativada.")
        else:
            print("Conta continua ativada.")

    def __str__(self):
        return f"Nome: {self.nome}\nTipo de Conta: {self.tipoConta}\nNúmero da Conta: {self.numConta}\nNúmero da Agência: {self.numAgencia}\nSaldo: {self.saldo}"


conta1 = Banco("brenda", "corrente", "3422125-3", "00", 10.00)
print("Saldo:", conta1.saldo)
conta1.deposito()
conta1.transferencia()
conta1.desativarConta()

print(conta1)






