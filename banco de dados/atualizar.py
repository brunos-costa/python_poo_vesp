import sqlite3

#Estabelecendo a conexão
conexao = sqlite3.connect("departamento.db")

consulta = conexao.cursor()

tabela = """
CREATE TABLE IF NOT EXISTS funcionario(
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    salario FLOAT,
    cargo VARCHAR(100)
);
"""
consulta.execute(tabela)


nome = input("Informe o novo nome do funcionário: ")
codigo = int(input("Informe o código do fucnoinário: "))

sql = "UPDATE funcionario SET nome = ? WHERE codigo = ?"

campos = (nome, codigo)

consulta.execute(sql, campos)

conexao.commit()

print(consulta.rowcount, " linha(s) atualizada(s) com sucesso")

conexao.close()
