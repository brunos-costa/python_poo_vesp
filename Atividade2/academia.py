class Aluno:
    def __init__(self, nome, idade,peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def exibirDados(self):
        print(f"Olá {self.nome}, sua idade é {self.idade} seu peso é {self.peso} e sua altura é {self.altura}")
    
    def calculraImc(self):
        imc = self.peso / self.altura**2
        return imc