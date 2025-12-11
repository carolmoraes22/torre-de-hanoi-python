def torre_de_hanoi(n, origem, destino, auxiliar): 
    if n == 1:
print(f"Mova o disco 1 da coluna {origem} para a coluna {destino}")
    return

torre_de_hanoi(n - 1, origem, auxiliar, destino)
print(f"Mova o disco {n} da coluna {origem} para a coluna {destino}")
torre_de_hanoi(n - 1, auxiliar, destino, origem)

n_discos = 3
coluna_origem = 'A'
coluna_destino = 'C'
coluna_auxiliar = 'B'

print(f"Resolvendo a Torre de Hanói com {n_discos} discos:")
print("-" * 35)

torre_de_hanoi(n_discos, coluna_origem, coluna_destino, coluna_auxiliar)
print("-" * 35)

print(f"Solução concluída em {2**n_discos - 1} movimentos.")
