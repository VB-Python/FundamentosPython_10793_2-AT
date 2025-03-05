'''Eliminar os funcionarios com salario inferior a 3000.00'''


import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

#Elimina todos os salários inferiores a 3000.00
cursor.execute("DELETE FROM funcionarios WHERE salario < 3000.00")

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