'''Considera a seguinte lista:
nums=[10, 2.5, 7, 11, 7.9, "Python", True,6, 5.8 , "Listas"]
Efetua um programa em python que:
a. Imprima a quantidade de inteiros, floats, strings e boleanos na lista;
b. Efetua a média de todos os valores inteiros na lista.
c. Crie e retorne uma nova lista só com os valores inteiros'''


# Lista inicial
nums = [10, 2.5, 7, 11, 7.9, "Python", True, 6, 5.8, "Listas"]
# a. Conta a quantidade de cada tipo de dado
inteiros = len([x for x in nums if type(x)== int])
floats = sum(1 for x in nums if type(x)== float)
strings = sum(1 for x in nums if type(x)== str)
booleanos = sum(1 for x in nums if type(x)== bool)
print(f"Inteiros: {inteiros}, Floats: {floats}, Strings: {strings}, Booleanos: {booleanos}")
# b. Calcula a média dos inteiros
valores_inteiros = [x for x in nums if type(x)== int]
media = sum(valores_inteiros) / len(valores_inteiros)
print(media)
# c. Cria uma nova lista só com os inteiros
lista_inteiros = [x for x in nums if type(x)== int]
print(lista_inteiros)


