'''Escreve um programa que receba o nome de um produto e o seu preço, e retorne o
preço total considerando os descontos seguintes:
1. Se o produto for um smartphone, será aplicado um desconto de 10%.
2. Se o produto for um tablet, será aplicado um desconto de 15%.
3. Se o produto for um laptop, será aplicado um desconto de 20%.
4. Para qualquer outro produto, não haverá desconto.
Utilize a estrutura match...case para determinar o desconto a ser aplicado'''

print("1. Se o produto for um smartphone;\n 2. Se o produto for um tablet;\n 3. Se o produto for um laptop;\n 4. Para qualquer outro produto.")



produto = float(input("Introduza o produto: "))
preco   = float(input("Introduza o preço do produto:"))

match produto:
    case 1:
        print("Preço final, com 10% de desconto:" ,preco - (preco * 10 / 100), "€")
    case 2:
        print("Preço final, com 15% de desconto:" ,preco - (preco * 15 / 100), "€")
    case 3:
        print("Preço final, com 20% de desconto:" ,preco - (preco * 20 / 100), "€")
    case 4:
        print("Preço final, sem desconto:" ,preco, "€")
    case _:
        print("Código inválido")




#Seleccionar o produto e aplicar o desconto
codigo_produto=int(input("introduza o código do produto(Smartphone=1, Tablet=2, laptop=3, Outro=4)"))
preco=float(input("introduza o preço do produto:"))
match codigo_produto:
    case (1):
        preco_final=preco*0.90
        print(f"O preço final é: {preco_final}")
    case (2):
        preco_final=preco*0.85
        print(f"O preço final é: {preco_final}")
    case (3):
        preco_final=preco*0.80
        print(f"O preço final é: {preco_final}")
    case (4):
        preco_final=preco
        print(f"O preço final é: {preco_final}")
    case _:
         print("código inválido")