"""
generate_tables.py
------------------
Converte resultados CSV em tabelas Markdown e LaTeX
para inclusão no relatório da Prova 02.

Autor: Pedro Henrique
"""

import pandas as pd
import os

def generate_tables():
    os.makedirs("results/tables", exist_ok=True)

    for fname in ["results_moodle_10k.csv", "results_moodle_1M.csv"]:
        path = f"results/{fname}"
        if not os.path.exists(path):
            print(f"Arquivo não encontrado: {path}")
            continue

        df = pd.read_csv(path)
        dataset = "10.000" if "10k" in fname else "1.000.000"

        # Tabela Markdown
        markdown_table = df.to_markdown(index=False)
        with open(f"results/tables/table_{dataset}.md", "w", encoding="utf-8") as f:
            f.write(f"### Resultados – Instância com {dataset} vértices\n\n")
            f.write(markdown_table)

        # Tabela LaTeX
        latex_table = df.to_latex(index=False, caption=f"Resultados – Instância com {dataset} vértices")
        with open(f"results/tables/table_{dataset}.tex", "w", encoding="utf-8") as f:
            f.write(latex_table)

        print(f"Tabelas geradas para {dataset} vértices")

    print("\nTodas as tabelas foram criadas em 'results/tables/'.")


if __name__ == "__main__":
    generate_tables()
