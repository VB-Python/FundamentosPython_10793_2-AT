'''Reproduz o seguinte Código que tem como objetivo:  
Criar um programa que escreva três linhas num ficheiro novo. 
 
with open("novo_ficheiro.txt", "w") as ficheiro: 
    ficheiro.write("Linha 1") 
    ficheiro.write("Linha 2") 
    ficheiro.write("Linha 3") '''

try:
    with open("novo_ficheiro.txt", "w", encoding="utf-8") as ficheiro: 
        ficheiro.write("Linha 1")
        ficheiro.write("\nLinha 2") 
        ficheiro.write("\nLinha 3")
except FileNotFoundError: 
    print("Erro: O ficheiro não existe.") 
except Exception as e: 
    print(f"Ocorreu um erro inesperado: {e}") 