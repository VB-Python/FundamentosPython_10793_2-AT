'''Dados inseridos em PART03_PONTO_2.py'''

'''Acrescenta mais 2 funcionários à basa de dados, alterando o código acima, PART03_ex02_1.py'''



import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

#Inserir funcionários na tabela
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Mario', 'Presidente', 2500)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Soares', 'Ministro', 2100)")

#Guardar mudanças
conn.commit()



#Consulta todos os funcionarios
cursor.execute("SELECT * FROM funcionarios")
#retorna todos os registos
funcionarios = cursor.fetchall()

#Exibir os resultados
for funcionario in funcionarios:
    #exibe todos os funcionarios
    print(funcionario)


#Fechar conexão
conn.close()

print("Dados atualizados com sucesso!")


''' Não consegui validar os nomes introduzidos com a função if

import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

#Verificar nomes criados
cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor.fetchall()

#Exibir os resultados
for funcionario in funcionarios:
 
  if "Mario" in funcionario["nome"]:
     print(funcionario)
   
conn.close()
'''