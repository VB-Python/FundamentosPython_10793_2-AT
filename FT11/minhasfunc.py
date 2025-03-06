
##########################################################
def triangulo (lado1,lado2,lado3):
    if lado1==lado2 and lado2==lado3:
        return "Equilátero"
    elif lado!=lado2 and lado2!=lado3 and lado1!=lado3:
        return "Escaleno"
    else:
        return "Isósceles"
##########################################################
def areaeperimetoquadrado(lado):
    area = lado*lado
    perimetro = 4*lado
    return area, perimetro
##########################################################
def info_num(*num):
    soma=sum(num)
    total=len(num)
    media=soma/totalreturn soma, media, total
##########################################################
def numeros(dados):
    import statistics
    user = list(map(int, dados.split()))
    soma = sum(user)
    conta_numeros = len(user)
    media = statistics.mean(user)
    return soma, conta_numeros, media
##########################################################
def dadoslista(valores):
    soma = sum(valores)
    compr = len(valores)
    media = sum(valores)/len(valores)
    return soma, compr, media
##########################################################
def info_str(palavra="AEc"):
    count_vogais=0
    for x in palavra:
        if x in ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]:
            count_vogais+=1
    
    return count_vogais
##########################################################
def ex5(elemento):
    elementos = []
    for p in elemento:
        if p not in elementos:
            elementos.append(p)
    return elementos
##########################################################


