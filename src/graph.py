"""
graph.py
---------
Define a classe Graph para representar grafos de forma simples e eficiente.

Este módulo é responsável por:
- Criar grafos completos ou parciais;
- Gerar pesos aleatórios entre vértices;
- Permitir iteração sobre vizinhos e pesos.

Autor: Pedro Henrique
Data: 03-11-2025
"""

import random

class Graph:
    def __init__(self, n, complete=False, implicit=False, seed=42):
        """
        Inicializa um grafo com n vértices.
        complete=True → cria todas as arestas possíveis (grafo completo).
        implicit=True → não armazena arestas, gera pesos sob demanda.
        """
        self.n = n
        self.complete = complete
        self.implicit = implicit
        random.seed(seed)

        if not implicit:
            # Lista de adjacência: {u: [(v, peso), ...]}
            self.adj = {i: [] for i in range(n)}
            if complete:
                for i in range(n):
                    for j in range(i + 1, n):
                        w = random.randint(1, 100)
                        self.add_edge(i, j, w)

    def add_edge(self, u, v, w):
        """Adiciona aresta não direcionada."""
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    def neighbors(self, u):
        """
        Retorna os vizinhos de um vértice.
        - Se o grafo é implícito, gera pesos de forma determinística.
        """
        if self.implicit:
            for v in range(self.n):
                if v != u:
                    w = (u * 31 + v * 17) % 100 + 1  # peso pseudo-aleatório
                    yield (v, w)
        else:
            yield from self.adj[u]
