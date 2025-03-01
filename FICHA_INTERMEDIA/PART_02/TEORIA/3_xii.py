'''readline() - Lê linha a linha 
O método readline( ) lê o ficheiro linha a linha, evitando o carregamento total na 
memória. '''

import exemplo.txt

with open("exemplo.txt", "r") as ficheiro: 
    linha = ficheiro.readline() 
    while linha: 
        print(linha, end="") 
        linha = ficheiro.readline() 