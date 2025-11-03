"""
counter.py
-----------
Define a classe Counter usada para contar comparações e operações.

Autor: Pedro Henrique
Data: 03-11-2025
"""

class Counter:
    def __init__(self):
        self.comparisons = 0

    def inc(self, n=1):
        """Incrementa o número de comparações."""
        self.comparisons += n

    def reset(self):
        """Zera o contador."""
        self.comparisons = 0
