'''Segurança e Boas Práticas 
i. 
Verificação da existência de ficheiros 
Evitar erros ao tentar abrir ficheiros inexistentes: '''

import os 

if os.path.exists("exemplo.txt"): 
    with open("exemplo.txt", "r") as ficheiro: 
        print(ficheiro.read()) 
else: 
    print("Erro: O ficheiro não foi encontrado.")