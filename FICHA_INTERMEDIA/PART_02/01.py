'''Reproduz o seguinte Código que tem como objetivo:  
Criar um programa que escreva três linhas num ficheiro novo. '''




with open("ficheiro.csv", newline='', encoding="utf-8") as ficheiro: 
    leitor = csv.DictReader(ficheiro)  # Converte cada linha num dicionário 
    for linha in leitor: 
        print(linha["Nome"], "-", linha["Idade"]) 