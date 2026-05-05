# src/core/jogo.py

from abc import ABC, abstractmethod   #importa elementos dos modulos

class JogoTabuleiro(ABC): #clase pra criar as abstratas
    def __init__(self, jogadores):
        self._jogadores = jogadores
        self._turno_atual = 0       # índice de quem é a vez
        self._encerrado = False

    @property
    def jogador_atual(self):
        return self._jogadores[self._turno_atual]


    def avancar_turno(self):
        # passa pro prox. jogador (volta ao 0 depois do ultimo) 
        self._turno_atual = (self._turno_atual + 1) % len(self._jogadores) 




    #  metodos que todo jogo deve implementar __
    @abstractmethod
    def inicializar(self):
         """Prepara o tabuleiro para começar."""
        pass


    @abstractmethod
    def validar_jogada(self, jogada):
        """Retorna True se a jogada eh permitida, False caso contrário."""
        pass

    @abstractmethod
    def aplicar_jogada(self, jogada):
        """Coloca a jogada no tabuleiro."""
        pass

    @abstractmethod
    def verificar_fim(self):
        """Retorna True se o jogo acabou (vitória ou empate)."""
        pass

    @abstractmethod
    def exibir(self):
        """Mostra o estado atual do tabuleiro no terminal."""
        pass

    #tem heranca em abc e abstractmethod 