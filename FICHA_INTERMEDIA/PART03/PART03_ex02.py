'''Dados inseridos em PART03_PONTO_2.py'''

'''Acrescenta mais 2 funcionários à basa de dados, alterando o código acima, PART03_PONTO_2.py'''



import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

#Inserir funcionários na tabela
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Mario', 'Presidente', 6500)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Soares', 'Ministro', 7500)")



#Verificar nomes criados
cursor.execute("SELECT * FROM funcionarios")
nomes = cursor.fetchall() #retorna todos os registos

#Exibe os funcionarios
    for nome in nomes:
        #if funcionario == "Mario" and funcionario == "Soares"
           # print("Funcionários acrescentados com Sucesso")
        #else
           # print("Acrescentar 2 funcionários sem sucesso")
        print(nome)

#Guardar mudanças
conn.commit()
#Fechar conexão
conn.close()

