from academia import Aluno

listaAlunos = []

for contador in range(2):
    nome = input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))
    peso = float(input("Informe seu peso: "))
    altura = float(input("Informe sua altura: "))

    aluno = Aluno(nome, idade, peso, altura)
    listaAlunos.append(aluno)

#exibindo o 1º objeto
listaAlunos[0].exibirDados()
print(listaAlunos[0].calcularImc())

#exibindo o 2º objeto
listaAlunos[1].exibirDados()
print(listaAlunos[1].calcularImc())