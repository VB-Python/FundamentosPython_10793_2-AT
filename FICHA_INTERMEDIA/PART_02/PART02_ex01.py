'''Reproduz o seguinte Código que tem como objetivo:  
Criar um programa que leia um ficheiro de texto e exibir o seu conteúdo. 

with open("exemplo.txt", "r") as ficheiro: 
    conteudo = ficheiro.read() 
    print(conteudo) '''
    


try:
    
    if os.path.exists("exemplo.txt"):
        with open("exemplo.txt", "r") as ficheiro:
            conteudo = ficheiro.read() 
            print(conteudo)
    else:
        print("Erro: O ficheiro não foi encontrado.")