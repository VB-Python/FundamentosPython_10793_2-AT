'''Reproduz o seguinte Código que tem como objetivo:  
Criar um programa que leia um ficheiro de texto e exibir o seu conteúdo. 

with open("exemplo.txt", "r") as ficheiro: 
    conteudo = ficheiro.read() 
    print(conteudo) '''


       
try:    #Prevenir falhas com tre-except – garante robustez contra falhas
    
    with open("exemplo.txt", "r", encoding="utf-8") as ficheiro: 
        while chunk := ficheiro.read(1024):#Lê 1024 bytes de cada vez 
            print(chunk) 
except FileNotFoundError: 
    print("Erro: O ficheiro não existe.") 
except Exception as e: 
    print(f"Ocorreu um erro inesperado: {e}")





#outras formas que complementaram a anterior:


import os   #Verificação da existência de ficheiros-Evitar erros ao tentar abrir ficheiros inexistentes
try:
    if os.path.exists("exemplo.txt"):
        with open("exemplo.txt", "r", encoding="utf-8") as ficheiro:
            conteudo = ficheiro.read() 
            print(conteudo)
    else:
        print("Erro: O ficheiro não foi encontrado.")
except FileNotFoundError: 
    print("Erro: O ficheiro não existe.") 
except Exception as e: 
    print(f"Ocorreu um erro inesperado: {e}") 
    
#outra forma:
    
try:    #Prevenir falhas com tre-except – garante robustez contra falhas
    
    with open("exemplo.txt", "r", encoding="utf-8") as ficheiro:
        conteudo = ficheiro.read() 
        print(conteudo)
except FileNotFoundError: 
    print("Erro: O ficheiro não existe.") 
except Exception as e: 
    print(f"Ocorreu um erro inesperado: {e}")



'''Eficiência na Manipulação de Ficheiros- Leitura e Escrita com chunking 
O método `chunking` permite ler ficheiros grandes sem sobrecarregar a RAM (ler e 
escrever em partes – chuncks).'''

with open("exemplo.txt", "r", encoding="utf-8") as ficheiro: 
    while chunk := ficheiro.read(1024):#Lê 1024 bytes de cada vez 
        print(chunk) 



import mmap 

with open("exemplo.txt", "r+b") as ficheiro:
    conteudo = mmap.mmap(ficheiro.fileno(), 0) 
    #conteudo = ficheiro.read() 
    #print(conteudo)
    print(conteudo.readline()) 
    conteudo.close()
    
    
    
    
    
       
try:    #Prevenir falhas com tre-except – garante robustez contra falhas
    
    with open("exemplo.txt", "r", encoding="utf-8") as ficheiro: 
        while chunk := ficheiro.read(1024):#Lê 1024 bytes de cada vez 
            print(chunk) 
except FileNotFoundError: 
    print("Erro: O ficheiro não existe.") 
except Exception as e: 
    print(f"Ocorreu um erro inesperado: {e}")
