"""
moodle_runner.py
----------------
Executa os algoritmos de Dijkstra e heurística gulosa
nas instâncias grandes do Moodle (arquivos .txt).

Formato esperado do arquivo:
    n                     → número de vértices
    m                     → número de arestas
    u v w                 → aresta com peso w
    u v w
    ...

Autor: Pedro Henrique
"""

import csv
import time
from graph import Graph
from counter import Counter
from dijkstra import dijkstra
from greedy import greedy_path


def load_graph_from_file(path):
    """
    Lê um grafo no formato:
      n
      m
      u v w
      u v w
      ...
    """
    with open(path, "r") as f:
        n = int(f.readline().strip())  # número de vértices
        m = int(f.readline().strip())  # número de arestas
        G = Graph(n)

        for line in f:
            if not line.strip():
                continue  # ignora linhas vazias
            parts = line.split()
            if len(parts) == 3:
                u, v, w = parts
                G.add_edge(int(u), int(v), float(w))

    print(f"Grafo carregado com {n:,} vértices e {m:,} arestas.")
    return G


def run_on_moodle(file_path):
    """
    Executa Dijkstra e Heurística Gulosa em um arquivo de instância Moodle.
    Salva resultados no arquivo results/results_moodle.csv.
    """
    print(f"Carregando grafo do arquivo: {file_path}")
    G = load_graph_from_file(file_path)
    n = G.n
    start_node, end_node = 0, n - 1

    results = []

    for algo in ["dijkstra", "greedy"]:
        counter = Counter()
        print(f"\nExecutando {algo.upper()} para n = {n:,} vértices...")
        start_time = time.time()

        if algo == "dijkstra":
            dijkstra(G, start_node, counter)
        else:
            greedy_path(G, start_node, end_node, counter)

        elapsed = time.time() - start_time
        results.append((algo, n, counter.comparisons, elapsed))

        print(f"{algo.upper()} finalizado — Comparações: {counter.comparisons:,} | Tempo: {elapsed:.2f}s")

    # Salva resultados
    with open("results/results_moodle.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["algorithm", "n", "comparisons", "time"])
        writer.writerows(results)

    print("\nResultados salvos em results/results_moodle.csv")


if __name__ == "__main__":
    # Você pode alternar aqui qual instância do Moodle quer rodar:
    # run_on_moodle("data/moodle_10000.txt")
    run_on_moodle("data/moodle_1000000.txt")
