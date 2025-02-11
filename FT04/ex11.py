''' Escreve um programa que calcule a soma e o produto dos N primeiros números naturais.
'''

n = int(input("Introduza um numero:"))
N = n+1
soma = 0
multiplicacao = 1
for i in range(1,N):
    soma += i
    multiplicacao = multiplicacao * i

print(f"soma: {soma}")
print(f"multiplicacao: {multiplicacao}")