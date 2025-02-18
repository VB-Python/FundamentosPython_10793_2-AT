'''Considera a lista
idades=[25, 15, 19, 22, 37, 78, 46, 2, 67]
Cria um programa, em python, que:
a. Indique quantas pessoas são menores de idade
b. Ordene a lista por ordem decrescente
c. Pede ao utilizador uma idade e verifica se essa idade está na lista.
#- Se estiver faz print("A idade está na lista")
#- Caso contrário faz o print("não existe ninguém com essa idade na lista")'''

idades=[25,15,19,22,37,78,46,2,67]
idades.sort()
print(f"lista ordenada de idades: {idades}")
menores_de_idade = len([idade for idade in idades if idade < 18])
print(f"Quantidade de pessoas menores de idade: {menores_de_idade}")
idades.sort(reverse=True)
print(f"Lista de idades por ordem decrescente: {idades}")
idade_a_verificar = int(input("Digita a tua idade: "))
if idade_a_verificar in idades:
    print("\nA idade está na lista")
else:
    print("\nNa lista, não existe ninguém com a tua idade")
