'''Escreve uma função em Python que, dados a medida do comprimento dos três
 lados de um triângulo diga se o mesmo é equilátero, isósceles ou escaleno.'''
 
import minhasfunc

a = float(input("Introduza medida de comprimento do lado 1!"))
b = float(input("Introduza medida de comprimento do lado 2!"))
c = float(input("Introduza medida de comprimento do lado 3!"))
       
        
res = minhasfunc.triangulo(a,b,c)
print(res)

