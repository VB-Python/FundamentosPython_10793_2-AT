'''Exercicio 1.
Criei, e executei o ficheiro "banco_dados.py".
Verifiquei o criar de um ficheiro chamado "empresa.db".'''

import banco_dados
import sqlite3

banco_dados

try:
    conexao = sqlite3.connect("empresa.db")


    cursor = conexao.cursor()

    print("Base de dados criada e conectada com sucesso!")

    conexao.close()

except FileNotFoundError: 
    print("Erro: O ficheiro não existe.") 
except Exception as e: 
    print(f"Ocorreu um erro inesperado: {e}") 

