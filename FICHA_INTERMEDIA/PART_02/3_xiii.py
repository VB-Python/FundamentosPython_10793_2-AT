

with open("exemplo.txt", "r") as ficheiro: 
    linhas = ficheiro.readlines() 
    for linha in linhas: 
        print(linha.strip()) 