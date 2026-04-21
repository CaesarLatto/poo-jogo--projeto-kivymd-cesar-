# src/core/jogada.py

class Jogada:
    def __init__(self, linha, coluna, jogador):
        self._linha = linha
        self._coluna = coluna
        self._jogador = jogador

    @property
    def linha(self):
        return self._linha

    @property
    def coluna(self):
        return self._coluna

    @property
    def jogador(self):
        return self._jogador