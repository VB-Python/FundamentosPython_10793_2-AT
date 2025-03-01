
'''Escreva um programa que pede ao utilizador um número inteiro e trata 
erros de entrada.'''

#try: 
#    numero = int(input("Digite um número inteiro: ")) 
    numero = int(input("Digite um número superior a 1: "))
    print ("Número inserido:", numero,) 
#except ValueError: 
    print("Erro: O valor deve ser um número inteiro.") 
    