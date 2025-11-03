# Prova 02 – Caminho Mínimo (Dijkstra e Greedy)

**Disciplina:** Algoritmos e Estruturas de Dados II  
**Instituição:** CEFET-MG  
**Aluno:** Pedro Henrique Oliveira Santos  
**Data:** Novembro de 2025  

---

## Descrição
Este projeto implementa e analisa o desempenho de dois algoritmos de caminho mínimo:

- **Dijkstra** — encontra o caminho mínimo exato entre vértices.  
- **Greedy (heurístico)** — busca aproximada com foco em eficiência.

O objetivo é comparar o **tempo de execução** e o **número de comparações** entre ambos em grafos grandes (10.000 e 1.000.000 vértices).

---

## Estrutura do Projeto

prova02/
├── src/
│ ├── dijkstra.py # Implementação do algoritmo de Dijkstra
│ ├── greedy.py # Implementação do algoritmo heurístico
│ ├── moodle_runner.py # Execução dos experimentos (fase 4)
│ ├── plot_moodle_duplo.py # Geração dos gráficos (fase 5)
│ ├── generate_tables.py # Criação das tabelas em Markdown/LaTeX (fase 6)
│ └── utils/ # Funções auxiliares (opcional)
│
├── results/
│ ├── results_moodle_10k.csv # Resultados - 10.000 vértices
│ ├── results_moodle_1M.csv # Resultados - 1.000.000 vértices
│ ├── comparisons_moodle_duplo_linear.png
│ ├── comparisons_moodle_duplo_log.png
│ ├── time_moodle_duplo_linear.png
│ └── time_moodle_duplo_log.png
│
├── requirements.txt
└── README.md

