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


codigo = int(input("Informe o código do funcionário: "))

sql = "DELETE FROM funcionario WHERE codigo = ?"

campos = (codigo,)# é preciso colocar uma vírgula depois do item para configurar que temos uma tupla, caso contrário não será aceito como uma tupla válida.

consulta.execute(sql, campos)

conexao.commit()

print(consulta.rowcount, " linha(s) deletada(s) com sucesso")

conexao.close()
