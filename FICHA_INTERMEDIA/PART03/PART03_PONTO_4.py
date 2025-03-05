'''Atualizar dados'''



import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

#Atualizar o salário de Pedro Santos
cursor.execute("UPDATE funcionarios SET salario = 3000.00 WHERE nome = 'Pedro Santos'")

conn.commit()
conn.close()
