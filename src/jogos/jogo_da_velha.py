# src/jogos/jogo_da_velha.py

from core.jogo import JogoTabuleiro
from core.tabuleiro import Tabuleiro

class JogoDaVelha(JogoTabuleiro):

    def inicializar(self):
        self._tabuleiro = Tabuleiro(3, 3)
        self._encerrado = False
        self._vencedor = None

    def validar_jogada(self, jogada):
        # a casa precisa existir E estar vazia
        if not self._tabuleiro.dentro_dos_limites(jogada.linha, jogada.coluna):
            print("  ✗ Posição fora do tabuleiro.")
            return False
        if not self._tabuleiro.casa_vazia(jogada.linha, jogada.coluna):
            print("  ✗ Essa casa já está ocupada.")
            return False
        return True

    def aplicar_jogada(self, jogada):
        self._tabuleiro.set_casa(jogada.linha, jogada.coluna, jogada.jogador.simbolo)

    def verificar_fim(self):
        simbolo = self.jogador_atual.simbolo
        t = self._tabuleiro

        # checa linhas e colunas
        for i in range(3):
            if all(t.get_casa(i, j) == simbolo for j in range(3)):
                self._vencedor = self.jogador_atual
                return True
            if all(t.get_casa(j, i) == simbolo for j in range(3)):
                self._vencedor = self.jogador_atual
                return True

        # checa diagonais
        if all(t.get_casa(i, i) == simbolo for i in range(3)):
            self._vencedor = self.jogador_atual
            return True
        if all(t.get_casa(i, 2 - i) == simbolo for i in range(3)):
            self._vencedor = self.jogador_atual
            return True

        # checa empate (nenhuma casa vazia)
        if all(not t.casa_vazia(i, j) for i in range(3) for j in range(3)):
            self._vencedor = None
            return True

        return False

    def exibir(self):
        t = self._tabuleiro
        print()
        print("    0   1   2")
        for i in range(3):
            linha = f"  {'  | '.join(t.get_casa(i, j) or '.' for j in range(3))}"
            print(f"{i} {linha}")
            if i < 2:
                print("   ---+---+---")
        print()