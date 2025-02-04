'''Faz um programa que receba a distância em km e a quantidade em litros de
combustível consumido por um carro num percurso. Calcula o consumo km/l e escreve
uma mensagem de acordo com o resultado obtido. (deverá ser criado o ficheiro
ex07.py).'''

km = input("Introduza o numero de kilometros:")
km = float(km)

litros = input("Introduza os litros gastos:")
litros = float(litros)


print(f"A média de combutivel por km foi de: {((litros*100)/km)} km/l")

km = input("introduza os km percurridos: ")
litros = input("introduza os litros gastos: ")
kml = (float(km)) / (float(litros))
lkm = (float(litros)) / (float(km))
print("o seu consumo foi ", kml, "Km/l")
print("o seu consumo foi ", lkm, "l/km")