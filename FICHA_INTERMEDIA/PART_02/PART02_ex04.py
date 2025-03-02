'''Reproduz o seguinte Código que tem como objetivo:  
 
Modificar o programa anterior para acrescentar mais uma linha ao ficheiro. 
 
with open("novo_ficheiro.txt", "a") as ficheiro: 
    ficheiro.write("Linha adicional") '''


try: 
    with open("novo_ficheiro.txt", "a", encoding="utf-8") as ficheiro: 
        ficheiro.write("\nLinha adicional")
except FileNotFoundError: 
    print("Erro: O ficheiro não existe.") 
except Exception as e: 
    print(f"Ocorreu um erro inesperado: {e}") 