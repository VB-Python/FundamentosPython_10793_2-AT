

def areaeperimetoquadrado(lado):
    area = lado*lado
    perimetro = 4*lado
    return area, perimetro


def numeros(dados):
    import statistics
    user = list(map(int, dados.split()))
    soma = sum(user)
    conta_numeros = len(user)
    media = statistics.mean(user)
    return soma, conta_numeros, media


def dadoslista(valores):
    soma = sum(valores)
    compr = len(valores)
    media = sum(valores)/len(valores)
    return soma, compr, media

