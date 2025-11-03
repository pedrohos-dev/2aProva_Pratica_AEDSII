"""
experiments.py
---------------
Executa experimentos de desempenho com Dijkstra e heurística gulosa.

Autor: Pedro Henrique
Data: 03-11-2025
"""

import csv
import time
from tqdm import tqdm
from graph import Graph
from counter import Counter
from dijkstra import dijkstra
from greedy import greedy_path

def run_experiments():
    """
    Executa os experimentos variando o número de vértices (n).
    """
    results = []

    for n in tqdm([1000, 2000, 3000], desc="Rodando experimentos"):
        G = Graph(n, complete=True)
        start_node, end_node = 0, n - 1

        for algo in ["dijkstra", "greedy"]:
            counter = Counter()
            start_time = time.time()

            if algo == "dijkstra":
                dijkstra(G, start_node, counter)
            else:
                greedy_path(G, start_node, end_node, counter)

            elapsed = time.time() - start_time
            results.append((algo, n, counter.comparisons, elapsed))

    # Salva resultados
    with open("results/results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["algorithm", "n", "comparisons", "time"])
        writer.writerows(results)

    print("✅ Resultados salvos em results/results.csv")

if __name__ == "__main__":
    run_experiments()
