'''Eliminar dados
executar código e verificar se o funcionário foi eliminado'''


import sqlite3

try:
    
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()

    #Eliminar um funcionário
    cursor.execute("DELETE FROM funcionarios WHERE nome = 'Mariana Costa'")

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