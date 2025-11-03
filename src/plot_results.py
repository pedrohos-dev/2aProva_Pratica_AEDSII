"""
plot_results.py
----------------
Gera gráficos comparando Dijkstra e a heurística gulosa
com base nos resultados salvos em results/results.csv.

Autor: Pedro Henrique
"""

import pandas as pd
import matplotlib.pyplot as plt

def plot_results(csv_path="results/results.csv"):
    df = pd.read_csv(csv_path)

    # --- Comparações ---
    plt.figure(figsize=(8, 5))
    for algo in df["algorithm"].unique():
        subset = df[df["algorithm"] == algo]
        plt.plot(subset["n"], subset["comparisons"], marker="o", label=algo)

    plt.title("Número de comparações × Número de vértices")
    plt.xlabel("Número de vértices (n)")
    plt.ylabel("Comparações")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("results/comparisons.png")
    print("Gráfico de comparações salvo em results/comparisons.png")

    # --- Tempo ---
    plt.figure(figsize=(8, 5))
    for algo in df["algorithm"].unique():
        subset = df[df["algorithm"] == algo]
        plt.plot(subset["n"], subset["time"], marker="o", label=algo)

    plt.title("Tempo de execução × Número de vértices")
    plt.xlabel("Número de vértices (n)")
    plt.ylabel("Tempo (s)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("results/time.png")
    print("Gráfico de tempo salvo em results/time.png")

if __name__ == "__main__":
    plot_results()
