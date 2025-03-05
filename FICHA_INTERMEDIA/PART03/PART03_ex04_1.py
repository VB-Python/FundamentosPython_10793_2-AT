'''Atualizar dados'''



import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

#Atualizar o salário de Pedro Santos
cursor.execute("UPDATE funcionarios SET salario = 3000.00 WHERE nome = 'Pedro Santos'")

#Consulta todos os funcionarios
cursor.execute("SELECT * FROM funcionarios")
#retorna todos os registos
funcionarios = cursor.fetchall()

#Exibir os resultados
for funcionario in funcionarios:
    #exibe todos os funcionarios
    print(funcionario)


conn.commit()
conn.close()
