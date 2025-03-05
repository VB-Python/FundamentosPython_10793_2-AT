'''Aumentar salario de todos em 5%'''



import sqlite3

try:
    
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()

    #Atualizar todos os salários em 5%
    cursor.execute("UPDATE funcionarios SET salario = salario*1.05 ")

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

except FileNotFoundError: 
    print("Erro: O ficheiro não existe.") 
except Exception as e: 
    print(f"Ocorreu um erro inesperado: {e}") 