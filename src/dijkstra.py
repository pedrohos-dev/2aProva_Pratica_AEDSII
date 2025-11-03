"""
dijkstra.py
------------
Implementação do algoritmo de Dijkstra com contagem de comparações.

Autor: Pedro Henrique
Data: 03-11-2025
"""

import heapq

def dijkstra(G, s, counter):
    """
    Executa o algoritmo de Dijkstra a partir do vértice s.
    G: grafo (objeto da classe Graph)
    counter: instância de Counter para contar comparações
    """
    n = G.n
    dist = [float('inf')] * n
    dist[s] = 0
    pq = [(0, s)]  # fila de prioridade (min-heap)

    while pq:
        d, u = heapq.heappop(pq)
        for v, w in G.neighbors(u):
            counter.inc()  # comparação dist[u] + w < dist[v]
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist
