'''Cria ou faz download de um ficheiro CSV. De seguida cria um programa 
que leia o ficheiro CSV e mostre cada linha do mesmo.  '''


import csv

try:
    
    ficheiro_csv = input("Digite o nome do ficheiro binário a copiar: ")
    with open(ficheiro_csv, newline='', encoding="utf-8") as ficheiro: 
        leitor = csv.DictReader(ficheiro)  # Converte cada linha num dicionário 
        for linha in leitor: 
            print(linha["Nome"], "->", linha["Idade"], "anos ->", linha["Cidade"])

except FileNotFoundError: 
    print("Erro: O ficheiro não existe.") 
except Exception as e: 
    print(f"Ocorreu um erro inesperado: {e}") 

