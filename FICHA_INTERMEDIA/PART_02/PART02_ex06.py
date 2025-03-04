'''Cria ou faz download de um ficheiro CSV. De seguida cria um programa 
que leia o ficheiro CSV e mostre cada linha do mesmo.  '''

import csv

with open("ficheiro.csv", newline='', encoding="utf-8") as ficheiro: 
    leitor = csv.reader(ficheiro) 
    for linha in leitor: 
        print(linha)# ficheiro CSV