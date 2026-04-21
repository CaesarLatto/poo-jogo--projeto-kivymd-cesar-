# src/core/tabuleiro.py

class Tabuleiro:
    def __init__(self, linhas, colunas):
        self._linhas = linhas
        self._colunas = colunas
        # grade começa toda vazia (None = vazio)
        self._grade = [[None] * colunas for _ in range(linhas)]

    def get_casa(self, linha, coluna):
        return self._grade[linha][coluna]

    def set_casa(self, linha, coluna, valor): 
        self._grade[linha][coluna] = valor

    def casa_vazia(self, linha, coluna):
        return self._grade[linha][coluna] is None

    def dentro_dos_limites(self, linha, coluna):
        return 0 <= linha < self._linhas and 0 <= coluna < self._colunas

    @property
    def linhas(self):
        return self._linhas

    @property
    def colunas(self):
        return self._colunas