''' Escreve um programa que calcule e escreva o resultado do fatorial de um 
número inteiro positivo N
sabendo que: n!=1*2*3*…*n.'''


n = int(input("Introduza um numero:"))
N = n+1

multiplicacao = 1
for i in range(1,N):
    
    multiplicacao *= i

print(f"Factorial de {n} é {multiplicacao}")