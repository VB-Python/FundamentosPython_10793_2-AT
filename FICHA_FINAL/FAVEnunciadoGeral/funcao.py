
##########################################################
def conta_vogais(palavra):
    vogais = 'aeiou'
    count = 0
    for letra in palavra.lower():
        if letra in vogais:
            count += 1
    return count
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