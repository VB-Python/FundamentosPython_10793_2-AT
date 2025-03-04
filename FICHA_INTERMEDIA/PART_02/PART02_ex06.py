'''Cria ou faz download de um ficheiro CSV. De seguida cria um programa 
que leia o ficheiro CSV e mostre cada linha do mesmo.  '''

import csv

ficheiro_csv = input("Digite o nome do ficheiro.csv: ")
with open(ficheiro_csv, newline='', encoding="utf-8") as ficheiro: 
    leitor = csv.reader(ficheiro) 
    for linha in leitor: 
        print(linha)
    print("\noutra forma: ")

#with open(ficheiro_csv, newline='', encoding="utf-8") as ficheiro: 
   # leitor = csv.DictReader(ficheiro)  # Converte cada linha num dicionário 
    #for linha in leitor: 
      #  print(linha["Nome"], "-", linha["Idade"]) 



