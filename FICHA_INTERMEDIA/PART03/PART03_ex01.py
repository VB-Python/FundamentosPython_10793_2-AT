'''Exercicio 1.
Criei, e executei o ficheiro "banco_dados.py".
Verifiquei o criar de um ficheiro chamado "empresa.db".'''

import banco_dados
import sqlite3

#banco_dados

conexao = sqlite3.connect("empresa.db")


cursor = conexao.cursor()

print("Base de dados criada e conectada com sucesso!")

conexao.close()
