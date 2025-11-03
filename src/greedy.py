"""
greedy.py
----------
Implementação de uma heurística gulosa para caminho mínimo.
Em cada passo, escolhe o vizinho mais próximo ainda não visitado.

Autor: Pedro Henrique
Data: 03-11-2025
"""

def greedy_path(G, s, t, counter):
    """
    Executa a heurística gulosa entre s e t.
    Retorna o caminho percorrido.
    """
    visited = set([s])
    u = s
    path = [s]

    while u != t:
        min_w, next_v = float('inf'), None
        for v, w in G.neighbors(u):
            counter.inc()
            if v not in visited and w < min_w:
                min_w, next_v = w, v
        if next_v is None:
            break  # não há mais vizinhos disponíveis
        visited.add(next_v)
        path.append(next_v)
        u = next_v

    return path
