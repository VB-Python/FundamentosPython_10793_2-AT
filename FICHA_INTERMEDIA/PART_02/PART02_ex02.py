'''Reproduz o seguinte Código que tem como objetivo:  
Modificar o exercício anterior para exibir o conteúdo linha por linha. 
 
with open("exemplo.txt", "r") as ficheiro: 
    for linha in ficheiro: 
        print(linha.strip()) '''

try:#prevenção de falhas em PART02_ex02, prevenção existencia de ficheiro.py em PART02_ex02

    with open("exemplo.txt", "r", encoding="utf-8") as ficheiro:
        ficheiro = ficheiro.readlines()
        for linha in ficheiro: 
            print(linha.strip())
except FileNotFoundError: 
    print("Erro: O ficheiro não existe.") 
except Exception as e: 
    print(f"Ocorreu um erro inesperado: {e}") 
