'''Vamos recuperar os dados armazenados na tabela
1.- Explica o que faz cada linha de código acima
2.- Executa o código e verifica os resultados'''


import sqlite3

try:
    
    #cria ou conecta à basede dados "empresa.db"
    conn = sqlite3.connect('empresa.db')
    #Cria um objecto cursor para interagir com a base de dados
    cursor = conn.cursor()

    #Consulta todos os funcionarios
    cursor.execute("SELECT * FROM funcionarios")
    #retorna todos os registos
    funcionarios = cursor.fetchall()

    #Exibir os resultados
    for funcionario in funcionarios:
        #exibe todos os funcionarios
        print(funcionario)

    #fecha a conexão
    conn.close()

except FileNotFoundError: 
    print("Erro: O ficheiro não existe.") 
except Exception as e: 
    print(f"Ocorreu um erro inesperado: {e}") 