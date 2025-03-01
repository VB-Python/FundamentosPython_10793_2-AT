'''readlines() - Retorna todas as linhas como uma lista 
O método readlines( ) retorna uma lista onde cada linha é um elemento. '''

with open("exemplo.txt", "r") as ficheiro: 
    linhas = ficheiro.readlines() 
    for linha in linhas: 
        print(linha.strip()) 