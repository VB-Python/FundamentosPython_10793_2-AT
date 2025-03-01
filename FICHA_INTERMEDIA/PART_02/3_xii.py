import exemplo.txt

with open("exemplo.txt", "r") as ficheiro: 
    linha = ficheiro.readline() 
    while linha: 
        print(linha, end="") 
        linha = ficheiro.readline() 