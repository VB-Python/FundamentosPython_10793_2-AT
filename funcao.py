
##########################################################

def info_str(palavra="AEc"):
    count_vogais=0
    for x in palavra:
        if x in ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]:
            count_vogais+=1
    
    return count_vogais

##########################################################

def conta_vogais(palavra):
    vogais = 'aeiou'
    count = 0
    for letra in palavra.lower():
        if letra in vogais:
            count += 1
    return count

##########################################################