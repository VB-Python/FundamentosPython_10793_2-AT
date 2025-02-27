'''Elabora uma script em python que peça ao utilizador um número e some todos 
os números de 1 até esse mesmo número. Deves utilizar o tratamento de 
erros.'''

import sys
j = 0
try: 
    numero = int(input("Digite um número: "))
    for j in range(2, numero + 1):
    #print soma
        j += j
    print("A soma de todos os numeros de 1 a ", numero, " é: ", j)
    
except Exception as e: 
    print("Erro inesperado:", e) 
    sys.exit(1)
except ValueError: 
    print("Erro: O valor deve ser um número inteiro.") 