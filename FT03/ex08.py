'''Escreve um programa para classificar um triângulo de acordo com o comprimento dos
seus lados. Considere as seguintes informações:
• Triângulo equilátero: todos os lados possuem o mesmo comprimento;
• Triângulo escaleno: todos os lados possuem comprimento diferente;
• Triângulo isósceles: caracterizado por ter dois lados com o mesmo comprimento'''


lado1 = float(input("Introduza um primeiro lado do Triângulo:"))
lado2 = float(input("Introduza um segundo lado do Triângulo:"))
lado3 = float(input("Introduza um terceiro e ultimo lado do Triângulo:"))



if lado1 == lado2 == lado3:
    print("Triângulo equilátero: todos os lados possuem o mesmo comprimento")
elif lado1 == lado2 != lado3 or lado1 != lado2 == lado3 or lado1 == lado3 != lado2:
    print("Triângulo isósceles: caracterizado por ter dois lados com o mesmo comprimento")
else:
    print("Triângulo escaleno: todos os lados possuem comprimento diferente")


lado_a = float(input("Digite o primeiro lado\n "))
lado_b = float(input("Digite o segundo lado\n "))
lado_c = float(input("Digite o terceiro lado\n "))
if lado_a == lado_b == lado_c:
    print("Triângulo equilátero")
elif lado_a != lado_b != lado_c:
    print("Triângulo escaleno")
else:
    print("Triângulo isósceles")