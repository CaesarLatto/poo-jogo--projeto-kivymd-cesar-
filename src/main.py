# src/main.py

from core.jogador import Jogador
from core.jogada import Jogada
from jogos.jogo_da_velha import JogoDaVelha

def pedir_jogada(jogador, jogo): 
    while True:
        try:
            entrada = input(f"  Vez de {jogador} — linha coluna (ex: 1 2): ")
            partes = entrada.strip().split()
            if len(partes) != 2:
                raise ValueError
            linha, coluna = int(partes[0]), int(partes[1])
            jogada = Jogada(linha, coluna, jogador)
            if jogo.validar_jogada(jogada):
                return jogada
        except ValueError:
            print("  Digite dois números separados por espaço.")

def main():
    print("=== Jogo da Velha ===\n")
    nome1 = input("Nome  do jogador 1: ")
    nome2 = input("Nome do jogador 2: ")

    jogadores = [
        Jogador(nome1, "X"),
        Jogador(nome2, "O"),
    ]

    jogo = JogoDaVelha(jogadores)
    jogo.inicializar()

    while True:
        jogo.exibir()
        jogada = pedir_jogada(jogo.jogador_atual, jogo)
        jogo.aplicar_jogada(jogada)

        if jogo.verificar_fim():
            jogo.exibir()
            if jogo._vencedor:
                print(f" {jogo._vencedor.nome} venceu!\n")
            else:
                print(" Empate!\n")
            break

        jogo.avancar_turno()

if __name__ == "__main__":
    main()