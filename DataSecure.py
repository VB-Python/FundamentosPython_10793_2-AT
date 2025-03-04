

import hashlib 
import os 
 
def calcular_hash(ficheiro): 
    """Calcula o hash MD5 de um ficheiro binário para verificar integridade.""" 
    hash_md5 = hashlib.md5() 
    with open(ficheiro, "rb") as f: 
        for chunk in iter(lambda: f.read(4096), b""):  # Lê o ficheiro em blocos de 4KB 
            hash_md5.update(chunk) 
    return hash_md5.hexdigest() 
 
def copiar_ficheiro_binario(origem, destino): 
    """Copia um ficheiro binário e verifica a integridade dos dados.""" 
    try: 
        # Verificar se o ficheiro de origem existe
        if not os.path.exists(origem): 
            print("Erro: O ficheiro de origem não existe.") 
            return
 
        # Copiar o ficheiro binário 
        with open(origem, "rb") as f_origem, open(destino, "wb") as f_destino: 
            for chunk in iter(lambda: f_origem.read(4096), b""):  # Copia em blocos de 4KB 
                f_destino.write(chunk) 
 
        # Verificar integridade dos ficheiros 
        if calcular_hash(origem) == calcular_hash(destino): 
            print(f"Sucesso! O ficheiro '{destino}' foi copiado corretamente.") 
        else: 
            print("Erro: A cópia do ficheiro não é idêntica ao original.") 
            
    except Exception as e: 
        print(f"Erro inesperado: {e}")


