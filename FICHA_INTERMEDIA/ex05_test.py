'''Elabora uma script em python que peça ao utilizador um número e some todos 
os números de 1 até esse mesmo número. Deves utilizar o tratamento de 
erros.'''
soma = 0
#import sys

try: 
    numero = int(input("Digite um número superior a 1: "))
    for j in range(1, numero+1):
    #print soma
        print ("j: ", j)
        soma = soma + j
        print ("soma: ", soma)
    print("A soma de todos os numeros de 1 a ", numero, " é: ", soma)
    
except ValueError: 
    print("Erro: O valor deve ser um número inteiro.") 
except ValueError: 
    print("Erro: Digite um número inteiro válido.") 
except 0: 
    print("Erro: Número não é superior ou igual a 1.")
    