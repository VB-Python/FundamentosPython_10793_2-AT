'''4. Utilizando a biblioteca NumPy : 
a. Cria um array de números 1 com shape (8, 2) 
b. Cria um array de zeros com shape (5, 7) 
c. Subtraia o novo array de outro com dados aleatórios e armazene o numa variável 
chamada subarray 
d. Calcula a média dos valores do array subarray '''



#4. Utilizando a biblioteca NumPy : 

import numpy as np           # Import o NumPy
import numpy

try:

    while True:
        print("\nUtilizando a biblioteca NumPy : ")
        print("a - Cria um array de números 1 com shape (8, 2)")
        print("b - Cria um array de zeros com shape (5, 7)")
        print("c - Subtraia o novo array de outro com dados aleatórios,")
        print("    e armazene-o numa variável chamada subarray")
        print("d - Calcula a média dos valores do array subarray")
        print("s - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "a":
                # Cria um array de números 1 com shape (8, 2)
                obj = numpy.ones((8,2))
                print(obj)
                print(obj.shape)
                
            case "b":
                obj = numpy.zeros((5,7))
                print(obj)
                print(obj.shape)
                
            case "c":
                menu.update({"omolete": 5})
            case "d":
                for x, y in menu.items():
                    print(x, y)
            case _:
                print("Opção inválida, tente novamente.")

