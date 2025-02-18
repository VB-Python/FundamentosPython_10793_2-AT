'''. Escreve um programa que solicite ao utilizador um número 
e escreva em simultâneo a sequência crescente e decrescente 
entre 1 e esse número.
Apresentação no ecrã:
1 5
2 4
3 3
4 2
5 1
'''


n = int(input("Introduza um número inteiro positivo: "))

for i in range(1,n+1):
   print("%d\t\t%d"%(i,n+1-i))
   