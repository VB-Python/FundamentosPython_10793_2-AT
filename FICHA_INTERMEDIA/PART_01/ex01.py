
'''Escreva um programa que pede ao utilizador um número inteiro e trata 
erros de entrada.'''

try: 
    numero = int(input("Digite um número: ")) 
    print("O dobro do número é:", numero * 2) 
except ValueError: 
    print("Erro: Digite apenas números inteiros.") 