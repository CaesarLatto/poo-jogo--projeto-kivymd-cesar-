# tests/test_jogo_da_velha.py
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


import unittest
from core.jogador import Jogador
from core.jogada import Jogada
from jogos.jogo_da_velha import JogoDaVelha

def criar_jogo():
    """Cria um jogo limpo com dois jogadores. Reutilizado em vários testes."""
    jogadores = [Jogador("Cesar", "X"), Jogador("Bot", "O")]
    jogo = JogoDaVelha(jogadores)
    jogo.inicializar()
    return jogo


class TestValidacaoJogada(unittest.TestCase):

    def test_jogada_valida(self):
        jogo = criar_jogo()
        jogada = Jogada(0, 0, jogo.jogador_atual)
        self.assertTrue(jogo.validar_jogada(jogada))

    def test_jogada_fora_do_tabuleiro(self):
        jogo = criar_jogo()
        jogada = Jogada(5, 5, jogo.jogador_atual)
        self.assertFalse(jogo.validar_jogada(jogada))

    def test_jogada_em_casa_ocupada(self):
        jogo = criar_jogo()
        jogada = Jogada(1, 1, jogo.jogador_atual)
        jogo.aplicar_jogada(jogada)
        # tenta jogar na mesma casa de novo
        self.assertFalse(jogo.validar_jogada(jogada))


class TestDeteccaoVitoria(unittest.TestCase):

    def _jogar(self, jogo, posicoes):
        """Aplica uma lista de posições alternando jogadores."""
        for linha, coluna in posicoes:
            jogada = Jogada(linha, coluna, jogo.jogador_atual)
            jogo.aplicar_jogada(jogada)
            if not jogo.verificar_fim():
                jogo.avancar_turno()

    def test_vitoria_por_linha(self):
        jogo = criar_jogo()
        # X vence na linha 0: (0,0) (0,1) (0,2)
        # O joga nas linhas de baixo pra não interferir
        self._jogar(jogo, [(0,0), (1,0), (0,1), (1,1), (0,2)])
        self.assertTrue(jogo.verificar_fim())
        self.assertEqual(jogo._vencedor.simbolo, "X")

    def test_vitoria_por_coluna(self):
        jogo = criar_jogo()
        # X vence na coluna 0
        self._jogar(jogo, [(0,0), (0,1), (1,0), (1,1), (2,0)])
        self.assertTrue(jogo.verificar_fim())
        self.assertEqual(jogo._vencedor.simbolo, "X")

    def test_vitoria_por_diagonal(self):
        jogo = criar_jogo()
        # X vence na diagonal principal
        self._jogar(jogo, [(0,0), (0,1), (1,1), (0,2), (2,2)])
        self.assertTrue(jogo.verificar_fim())
        self.assertEqual(jogo._vencedor.simbolo, "X")

    def test_empate(self):
        jogo = criar_jogo()
        # preenche o tabuleiro sem ninguém vencer
        # X O X
        # X X O
        # O X O  → empate
        self._jogar(jogo, [
            (0,0), (0,1), (0,2),
            (1,1), (1,0), (1,2),
            (2,1), (2,0), (2,2),
        ])
        self.assertTrue(jogo.verificar_fim())
        self.assertIsNone(jogo._vencedor)


if __name__ == "__main__":
    unittest.main(verbosity=2)