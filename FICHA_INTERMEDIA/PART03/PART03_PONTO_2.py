'''Inserir dados de funcionários'''

import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

#Inserir funcionários na tabela
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Ana Silva', 'Gestora', 3500)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Pedro Santos', 'Programador', 4500)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Mariana Costa', 'Designer', 5500)")

#Guardar mudanças e fechar conexão
conn.commit()
conn.close()

