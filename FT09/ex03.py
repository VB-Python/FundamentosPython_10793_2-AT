'''Efetua um programa em python:
a. Instancie o seguinte dicionário:
Computadores_1={
 "Marca":"Asus",
 "Ecra":"14Pol",
 "RAM": [4, 8, 12]
 }
b. Acrescente um novo elemento à lista com chave igual a “Disco” e
valor [“128G”, “256G”]
c. Permita ao utilizador introduzir um valor específico de RAM e
verificar se esta está presente na lista.
d. Acrecente 16 como novo valor de RAM.
e. Copie o dicionário para um novo usando Deep Copy().
f. No novo dicionário modifique a marca para “Lenovo” e os valores da
RAM para [4,8]. Imprima a nova lista
g. Crie uma nova lista com deep copy e modifique a marca para “HP” e
Disco para [“256G”]- Imprima a respetiva lista
h. Cria uma lista cujos elementos são os três dicionários.
i. Imprima as marcas com 128G de Disco
j. Imprima as marcas com 8 e 12 de RAM'''


print("a - Instancie o seguinte dicionário")
print("b - Acrescente um novo elemento à lista com chave igual a “Disco” e valor [“128G”, “256G”]")
print("c - Permita ao utilizador introduzir um valor específico de RAM e verificar se esta está presente na lista")
print("d - Acrecente 16 como novo valor de RAM")
print("e - Copie o dicionário para um novo usando Deep Copy()")
print("f - No novo dicionário modifique a marca para “Lenovo” e os valores da RAM para [4,8]. Imprima a nova lista")
print("g - Crie uma nova lista com deep copy e modifique a marca para “HP” e Disco para [“256G”]- Imprima a respetiva lista")
print("h - Cria uma lista cujos elementos são os três dicionários")
print("i - Imprima as marcas com 128G de Disco")
print("j - Imprima as marcas com 8 e 12 de RAM")


Computadores_1={"Marca":"Asus","Ecra":"14Pol","RAM": [4, 8, 12]}
while True:
    user = input("Escolha uma opção:")
    match user:
        case "a":
            Computadores_1={ "Marca":"Asus","Ecra":"14Pol","RAM": [4, 8, 12]}
            print(Computadores_1["RAM"][1])
        case "b":
            Computadores_1["Disco"]=["128G", "256G"]
            Computadores_1.update({"Disco":["128G", "256G"]})
            print(Computadores_1)
        case "c":
            if m_ram in Computadores_1["RAM"]:
                print("existe um computador com essa capacidade")
            else:
                print("Não existe um computador com essa capacidade")
        case "d":
            Computadores_1["RAM"].append(16)
            print(Computadores_1)
        case "e":
            computadores_2=Computadores_1.copy()
        case "f":
            computadores_2["Marca"]="Lenovo"
            computadores_2["RAM"]=[4,8]
            print(computadores_2)
        case "g":
            computadores_3=Computadores_1.copy()
            computadores_3["Marca"]="HP"
            computadores_3["Disco"]=["256G"]
            print(computadores_3)
        case "h":
            lista_pc=[Computadores_1, computadores_2, computadores_3]
        case "i":
            for x in lista_pc:
                if "128G" in x["Disco"]:
                    marcas = marcas + " "+ x["Marca"]
             
            print(marcas) 
        case "j":
            for x in lista_pc:
                if 8 and 12 in x["RAM"]:
                    print("Marcas com 8 e 12G de RAM: ", x["Marca"])
        case _:
            print("Escolha uma opção entre a e d")

