class Pessoa:
    #atributos
    nome = "Fulano"
    peso = 71
    escolaridade = "Ensino Médio"

    #métodos
    def falar(self, texto):
        print(f"Tenho algo para te dizer: {texto}")


#CRIANDO OS OBJETOS
pessoa1 = Pessoa()

print(pessoa1.nome)
pessoa1.falar("Boa tarde, hoje é segunda-feira")