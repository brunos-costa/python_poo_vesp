class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
    
    def descrever(self):
        print(f"O produto {self._nome} custa R${self._preco}")
    
    def calcularDesconto(self, valor):
        print(f"O desconto não será fornecido por aqui")

# Classe filha 1 - Eletronico
class Eletronico(Produto):
    def __init__(self, nome, preco, voltagem ):
        super().__init__(nome, preco)
        self._voltagem = voltagem
    
    def descrever(self): 
        print(f"O Eletrônico {self._nome} custa R${self._preco} e possui a voltagem {self._voltagem}")
    
    def calcularDesconto(self, valor):
        desconto = valor/100
        print(f"O produto eletrônico {self._nome} terá um deconto de {desconto}%")

    