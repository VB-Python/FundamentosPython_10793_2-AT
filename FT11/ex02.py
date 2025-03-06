'''Escreve uma função em Python que, dados a medida do comprimento do lado de
 um quadrado imprima os valores do seu perímero e da sua área (area=lado x 
lado; perimetro = 4 x lado). '''


def calcular_quadrado(lado):
    area = (lado * lado)
    perimetro = (4 * lado)
    print(f"Os valores do perimetro são {perimetro}")
    print(f"Os valores da area são {area}")
a = int(input("Insira uma medida: "))
calcular_quadrado(a)


print("outra solução")

from  minhasfunc import areaeperimetoquadrado
l1 = float(input("Introduza o valor do lado: "))
    
a1, p1 = areaeperimetoquadrado(l1)
print("area = ", a1, " perimetro =",p1)

