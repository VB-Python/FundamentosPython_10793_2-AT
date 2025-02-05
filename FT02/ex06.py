'''Escreve um programa que solicite a temperatura em Fahrenheit (F), ao utilizador, e a
converta para grau Celsius (C), devolvendo o resultado da conversão.
Use a fórmula: C = 5 * ((F-32) / 9).
'''

print("Conversão de Fahrenheit (F) em graus Celsius (C)")


fahrenheit = float(input("Introduza um valor de temperatura em Fahrenheit (F):"))

celsius = 5 * ((fahrenheit - 32) / 9)


print(fahrenheit, "graus Fahrenheit correspondem a " , celsius, "graus Celsius")

