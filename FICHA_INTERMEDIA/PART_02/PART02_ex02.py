'''Reproduz o seguinte Código que tem como objetivo:  
Modificar o exercício anterior para exibir o conteúdo linha por linha. 
 
with open("exemplo.txt", "r") as ficheiro: 
    for linha in ficheiro: 
        print(linha.strip()) '''

import os

if os.path.exists("exemplo.txt"):
    with open("exemplo.txt", "r") as ficheiro:
        ficheiro = ficheiro.readlines()
        for linha in ficheiro: 
            print(linha.strip())
else:
    print("Erro: O ficheiro não foi encontrado.")
