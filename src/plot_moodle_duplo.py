"""
plot_moodle_duplo.py
--------------------
Gera gráficos comparando Dijkstra e Greedy nas instâncias do Moodle
para 10.000 e 1.000.000 vértices, em escalas linear e logarítmica.

Autor: Pedro Henrique
"""

import pandas as pd
import matplotlib.pyplot as plt
import os


def plot_moodle_results():
    # Garante que a pasta results existe
    os.makedirs("results", exist_ok=True)

    # --- Leitura dos arquivos ---
    df_10k = pd.read_csv("results/results_moodle_10k.csv")
    df_1M = pd.read_csv("results/results_moodle_1M.csv")

    # Adiciona rótulo identificando o dataset
    df_10k["dataset"] = "10.000 vértices"
    df_1M["dataset"] = "1.000.000 vértices"

    # Combina os dois dataframes
    df_all = pd.concat([df_10k, df_1M], ignore_index=True)

    # --------------------------------------------------------------------
    # 🔹 GRÁFICOS DE COMPARAÇÕES
    # --------------------------------------------------------------------
    def plot_comparisons(scale: str):
        plt.figure(figsize=(8, 5))
        for dataset, subset in df_all.groupby("dataset"):
            plt.plot(
                subset["algorithm"],
                subset["comparisons"],
                marker="o",
                linewidth=2,
                label=dataset,
            )
            for x, y in zip(subset["algorithm"], subset["comparisons"]):
                plt.text(
                    x,
                    y,
                    f"{int(y):,}".replace(",", "."),
                    ha="center",
                    va="bottom",
                    fontsize=9,
                )

        plt.title(f"Número de Comparações – Dijkstra vs Greedy ({scale.capitalize()})")
        plt.ylabel("Comparações" + (" (escala log)" if scale == "log" else ""))
        if scale == "log":
            plt.yscale("log")
            plt.grid(True, linestyle="--", alpha=0.6, which="both")
        else:
            plt.grid(True, linestyle="--", alpha=0.6)
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"results/comparisons_moodle_duplo_{scale}.png")
        print(f"📊 Gráfico salvo: results/comparisons_moodle_duplo_{scale}.png")

    # --------------------------------------------------------------------
    # 🔹 GRÁFICOS DE TEMPO
    # --------------------------------------------------------------------
    def plot_time(scale: str):
        plt.figure(figsize=(8, 5))
        for dataset, subset in df_all.groupby("dataset"):
            plt.plot(
                subset["algorithm"],
                subset["time"],
                marker="o",
                linewidth=2,
                label=dataset,
            )
            for x, y in zip(subset["algorithm"], subset["time"]):
                plt.text(x, y, f"{y:.3f}s", ha="center", va="bottom", fontsize=9)

        plt.title(f"Tempo de Execução – Dijkstra vs Greedy ({scale.capitalize()})")
        plt.ylabel("Tempo (segundos)" + (" (escala log)" if scale == "log" else ""))
        if scale == "log":
            plt.yscale("log")
            plt.grid(True, linestyle="--", alpha=0.6, which="both")
        else:
            plt.grid(True, linestyle="--", alpha=0.6)
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"results/time_moodle_duplo_{scale}.png")
        print(f"Gráfico salvo: results/time_moodle_duplo_{scale}.png")

    # Gera ambos (linear e log)
    for scale in ["linear", "log"]:
        plot_comparisons(scale)
        plot_time(scale)

    plt.show()
    print("\nGráficos lineares e logarítmicos gerados com sucesso!")


if __name__ == "__main__":
    plot_moodle_results()
