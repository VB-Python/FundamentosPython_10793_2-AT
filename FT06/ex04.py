'''Considera a seguinte lista:
nums=[10, 2.5, 7, 11, 7.9, "Python", True,6, 5.8 , "Listas"]
Efetua um programa em python que:
a. Imprima a quantidade de inteiros, floats, strings e boleanos na lista;
b. Efetua a média de todos os valores inteiros na lista.
c. Crie e retorne uma nova lista só com os valores inteiros'''


nums=[10, 2.5, 7, 11, 7.9, "Python", True,6, 5.8 , "Listas"]

x=0
for x in nums:
    isinstance(x,int) and not isinstance(x,bool)
    x += 1
print(x)


