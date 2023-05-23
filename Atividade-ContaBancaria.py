
class Banco:
    soma = 0
    subtracao = 0
    ativar = "sim"

    def __init__(self, nome, tipoConta, numConta, numAgencia, saldo):
        self.nome = nome
        self.tipoConta = tipoConta
        self.numConta = numConta
        self.numAgencia = numAgencia
        self.saldo = saldo


    def deposito(self):
        valorDeposito = float(input("Quanto você quer depositar?"))

        if valorDeposito >= 0:
            self.saldo += valorDeposito
            self.soma += valorDeposito
    def transferencia(self):
        transferencia = float(input("Quanto quer transferir?"))

        if transferencia >=0:
            self.saldo -= transferencia
            self.subtracao -= transferencia
    def ativarConta(self):
        ativarConta = input("Você deseja ativar a conta? Digite sim ou não.").lower()
        if ativarConta==self.ativar:
            print('Conta ativa.' )
        else:
            print('Conta desativada.')




    def __str__(self):
        return f"Nome: {self.nome}\nTipo de Conta: {self.tipoConta}\nNúmero da Conta: {self.numConta}\nNúmero da Agência: {self.numAgencia}\nSaldo: {self.saldo}"

conta1 = Banco("brenda", "corrente", "3422125-3", "00", 10.00)
print("saldo:", conta1.saldo)
conta1.deposito()
conta1.transferencia()
conta1.ativarConta()

print(conta1)






