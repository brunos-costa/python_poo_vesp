class Conta:
    def __init__(self, numero, titular, saldo, limite=200):# EStamos passando um valor padrão para o limte, tornando-o opcional, dessa forma o objeto ao ser criado pode ter um limite informado ou não
        #Quando colocamos 2 underlines antes do atributo, indicamos que esse atributo está com a visibilidade "privado", o ocntrário significa que está público
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def relatorio(self):
        print(f"Olá {self.__titular} seu saldo atual é {self.__saldo} e o seu limite atual é {self.__limite}")

    def getLimite(self):
        return self.__limite
    
    def setLimite(self, valor):
        if valor < 0:
            print("Informe um valor válido")
        else:
            self.__limite = valor
    
    def depositar(self, valor):
        if valor <= 0:
            print("Informe um valor positivo")
        else:
            self.__saldo = self.__saldo + valor
    
    def sacar(self, valor):
        if valor <= 0 or valor > self.__saldo:
            print("Saldo insuficiente ou valor negativo solicitado")
        else:
            self.__saldo -= valor
