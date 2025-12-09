def torre_de_hanoi(n, origem, destino, auxiliar):
    """
    Resolve o problema da Torre de Hanói usando recursão.

    Args:
        n (int): O número de discos a serem movidos.
        origem (str): O nome da coluna de origem (ex: 'A').
        destino (str): O nome da coluna de destino (ex: 'C').
        auxiliar (str): O nome da coluna auxiliar (ex: 'B').
    """
    if n == 1:
        # Caso base: mover 1 disco diretamente
        print(f"Mova o disco 1 da coluna {origem} para a coluna {destino}")
        return

    # 1. Mover n-1 discos da Origem para a Auxiliar, usando a Destino como auxiliar
    torre_de_hanoi(n - 1, origem, auxiliar, destino)
    
    # 2. Mover o maior disco (o disco n) da Origem para a Destino
    print(f"Mova o disco {n} da coluna {origem} para a coluna {destino}")
    
    # 3. Mover os n-1 discos da Auxiliar para a Destino, usando a Origem como auxiliar
    torre_de_hanoi(n - 1, auxiliar, destino, origem)

# --- Configuração do Problema ---
n_discos = 3
coluna_origem = 'A'
coluna_destino = 'C'
coluna_auxiliar = 'B'

print(f"Resolvendo a Torre de Hanói com {n_discos} discos:")
print("-" * 35)

# Execução da função
torre_de_hanoi(n_discos, coluna_origem, coluna_destino, coluna_auxiliar)
print("-" * 35)
print(f"Solução concluída em {2**n_discos - 1} movimentos.")