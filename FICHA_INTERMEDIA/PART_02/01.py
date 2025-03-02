'''Reproduz o seguinte Código que tem como objetivo:  
Criar um programa que leia um ficheiro de texto e exibir o seu conteúdo. 

with open("exemplo.txt", "r") as ficheiro: 
    conteudo = ficheiro.read() 
    print(conteudo) '''
    



with open("exemplo.txt", "r") as ficheiro: 
    while chunk := ficheiro.read(1024):#Lê 1024 bytes de cada vez 
        print(chunk) 
