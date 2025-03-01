''' Prevenir falhas com tre-except – garante robustez contra falhas '''

try: 
    with open("exemplo.txt", "r") as ficheiro: 
        print(ficheiro.read()) 
except FileNotFoundError: 
    print("Erro: O ficheiro não existe.") 
except Exception as e: 
    print(f"Ocorreu um erro inesperado: {e}") 