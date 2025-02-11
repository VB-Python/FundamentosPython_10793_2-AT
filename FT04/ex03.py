'''Fazer um programa para ler quatro números inteiros e positivos, calcular e devolver a sua
média.'''

contador = 1
soma = 0

while contador < 4:
    numero = int(input(f"Introduza 4 numerospara efectuar a media"))
    soma = soma + numero
    contador = contador + 1

media = soma / contador

print(f"A media é {media}")