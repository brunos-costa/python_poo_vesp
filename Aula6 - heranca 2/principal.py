from pessoa import Pessoa, Aluno, Professor

pessoa1 = Pessoa("Garibalde", 54)
aluno1 = Aluno("JUciclea", 16, 987)
prof1 = Professor("Ana Lúcia", 35, "Português")

pessoa1.info()

aluno1.info()
aluno1.estudar()

prof1.info()
prof1.ensinar()