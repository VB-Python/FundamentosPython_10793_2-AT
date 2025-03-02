'''Reproduz o seguinte Código que tem como objetivo:  
Modificar o exercício anterior para exibir o conteúdo linha por linha. 
 
with open("exemplo.txt", "r") as ficheiro: 
    for linha in ficheiro: 
        print(linha.strip()) '''



with open("exemplo.txt", "r", encoding="utf-8") as ficheiro: 
    for linha in ficheiro: 
        ficheiro = ficheiro.readlines()
        print(ficheiro)
        #print(linha.strip())