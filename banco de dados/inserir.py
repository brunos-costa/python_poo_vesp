import sqlite3

#Passo1 - Conexão com o banco
conexao = sqlite3.connect("departamento.db")

#Passo2 - Verificar se a tabela existe ou não
tabela = """
CREATE TABLE IF NOT EXISTS funcionario(
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    salario FLOAT,
    cargo VARCHAR(100)
);
"""
#Passo3 - Acessar o objeto cursor() da biblioteca sqlite3, para manipular dados do banco
consulta = conexao.cursor()

#Passo4 - Executar o comando de criação da tabela
consulta.execute(tabela)

#INSERIR DADOS NA TABELA
#Passo5 - solicitar dados do usuário
nome = input("Informe o nome do funcionário: ")
salario = float(input("Informe o salário do funcionário: "))
cargo = input("Informe o cargo do funcionário: ")

#Passo6 - Criando comando SQL para inserir os dados na tabela
sql = "INSERT INTO funcionario VALUES(?,?,?,?)"# Colocamos ? no lugar dos daddos reais, para evitar possíveis ataques de sql injection. Isso é uma implementação da biblioteca sqlite3.

#Passo7 - Organizar os dados que irão substituir ? no coando sql
campos = (None, nome, salario, cargo)# Criando uma tupla com os dados que irão substituir ?. Ao informar o valor 'None', estamos dizendo que será atribuído o valor padrão do AUTOINCREMENT

#pPasso8 - Executar o comando sql e substiruir '?' pelos campos
consulta.execute(sql, campos)

#Passo9 - Gravar os dados no banco
conexao.commit()

print(consulta.rowcount, " linha(s) inseridas com sucesso")

#Passo10 - encerrar a connexão
conexao.close()