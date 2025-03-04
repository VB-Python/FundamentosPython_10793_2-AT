'''Criar uma Base de Dados SQLite3 em Python '''

import sqlite3

conexao = sqlite3.connect("nome_da_base_de_dados")

cursor = conexao.cursor()

print("Base de Dados criada e conectada com sucesso!")

conexao.close()

