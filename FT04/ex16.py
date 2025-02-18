''' Escreva um programa que peça ao utilizador números 
entre 0-10. Se o utilizador inserir um número fora 
desse intervalo o programa deverá finalizar com uma 
mensagem personalizada.'''


n = int(input("Introduza um número interio entre 0 e 10: "))


#Testa se o valor introduzido é um inteiro positivo usando a função isdigit(). Enquanto não for solicita constantemente ao
while n<10 and n>0:
    n = int(input("Introduza um número natural: "))
else:
    print("O número introduzido é inválido")
    