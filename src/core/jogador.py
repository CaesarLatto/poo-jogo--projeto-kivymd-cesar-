# src/core/jogador.py

class Jogador:
    def __init__(self, nome, simbolo):
        self._nome = nome        # _ indica "não mexa nisso diretamente de fora"
        self._simbolo = simbolo

    @property
    def nome(self):
        return self._nome

    @property
    def simbolo(self):
        return self._simbolo

    def __str__(self):
        return f"{self._nome} ({self._simbolo})"
    