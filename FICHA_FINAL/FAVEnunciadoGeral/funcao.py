
##########################################################

def info_str(palavra="AEc"):
    count_vogais=0
    for x in palavra:
        if x in ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]:
            count_vogais+=1
    
    return count_vogais

##########################################################
