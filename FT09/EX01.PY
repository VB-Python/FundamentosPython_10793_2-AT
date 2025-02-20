'''Considera o seguinte dicionário, a que cada prato é associado o respetivo
valor em euros:
menu={
"entremeada": 7,
"Sardinha": 6,
"Filetes": 5.5,
"Prego": 7,
"Hamburguer": 5.5
}
Efetua um programa em python que, após instaciar a variável:
a. Devolva o preço do “prego”.
b. Faça o print de todas as chaves do dicionário
c. Acrescente na lista “omolete” com o preço de 5.
d. Faça o print de todo o dicionário, para visualizar as alterações.'''


menu={
"entremeada": 7,
"Sardinha": 6,
"Filetes": 5.5,
"Prego": 7,
"Hamburguer": 5.5
}

while True:
    print("\na - Devolva o preço do prego")
    print("b - Faça o print de todas as chaves do dicionário")
    print("c - Acrescente na lista “omolete” com o preço de 5")
    print("d - Faça o print de todo o dicionário, para visualizar as alterações")
    print("s - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "a":
            print (f" O preço para um Prego é de {(menu["Prego"])} €")
        case "b":
            for x in menu:
                print(x)
        case "c":
            menu.update({"omolete": 5})
        case "d":
            for x, y in menu.items():
                print(x, y)
        case _:
            print("Opção inválida, tente novamente.")
