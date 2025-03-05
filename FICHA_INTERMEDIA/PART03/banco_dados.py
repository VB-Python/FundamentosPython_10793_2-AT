'''1.- Criar um ficheiro python'''

import sqlite3

try:
    
    #Criar conexão com o banco de dados (ou criar se não existir)
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()

    #Criar tabela de funcionários

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL, cargo TEXT NOT NULL,
        salario REAL NOT NULL
    )
    ''')


    #Guardar as mudanças e fechar a conexão
    conn.commit()
    conn.close()

except FileNotFoundError: 
    print("Erro: O ficheiro não existe.") 
except Exception as e: 
    print(f"Ocorreu um erro inesperado: {e}") 