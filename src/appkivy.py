import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
sys.path.append(str(ROOT_DIR))

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen

from core.jogada import Jogada
from core.jogador import Jogador
from jogos.jogo_da_velha import JogoDaVelha

KV_PATH = Path(__file__).with_name("app.kv")


class MenuScreen(MDScreen):
    pass


class BoardScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game = None
        self.cell_buttons = []
        self.game_over = False

    def on_kv_post(self, base_widget):
        if not self.cell_buttons:
            self._build_board_cells()

    def _build_board_cells(self):
        grid = self.ids.grid_tabuleiro
        grid.clear_widgets()
        self.cell_buttons = []

        for row in range(3):
            for col in range(3):
                button = MDRaisedButton(
                    text="",
                    on_release=lambda btn, r=row, c=col: self.on_cell_press(r, c),
                    size_hint=(1, 1),
                )
                self.cell_buttons.append(button)
                grid.add_widget(button)

    def set_game(self, game):
        self.game = game
        self.game_over = False
        self.ids.label_result.text = ""
        self._refresh_board()
        self.update_turn_label()

    def on_cell_press(self, row, col):
        if not self.game or self.game_over:
            return

        jogada = Jogada(row, col, self.game.jogador_atual)
        if not self.game.validar_jogada(jogada):
            self.ids.label_result.text = "Jogada inválida. Escolha outra casa."
            return

        self.game.aplicar_jogada(jogada)
        self._refresh_board()

        if self.game.verificar_fim():
            self.game_over = True
            if self.game._vencedor:
                self.ids.label_result.text = f"{self.game._vencedor.nome} venceu!"
            else:
                self.ids.label_result.text = "Empate!"
            return

        self.game.avancar_turno()
        self.update_turn_label()
        self.ids.label_result.text = ""

    def _refresh_board(self):
        if not self.game:
            return

        for row in range(3):
            for col in range(3):
                symbol = self.game._tabuleiro.get_casa(row, col)
                self.cell_buttons[row * 3 + col].text = symbol or ""

    def update_turn_label(self): #mostra o turno
        if self.game:
            self.ids.label_turno.text = (
                f"Turno do Jogador: {self.game.jogador_atual.nome} "
                f"({self.game.jogador_atual.simbolo})"
            )

            #preciso criar alguma coisa pra reiniciar o jogo
    def reset_board(self):
        if self.game:
            self.game.inicializar()
            self.game_over = False
            self.ids.label_result.text = ""
            self._refresh_board()
            self.update_turn_label()

    def voltar_menu(self):
        self.manager.current = "menu"

#ate q esse kivy n eh tao chato q nem o firebase
class JogoDaVelhaApp(MDApp):
    def build(self):
        return Builder.load_file(str(KV_PATH))

 # função do "iniciar jogo"
    def start_game(self): 
        menu_screen = self.root.get_screen("menu")
        player1_name = menu_screen.ids.player1.text.strip() or "Jogador 1"
        player2_name = menu_screen.ids.player2.text.strip() or "Jogador 2"

        jogadores = [Jogador(player1_name, "X"), Jogador(player2_name, "O")]
        jogo = JogoDaVelha(jogadores)
        jogo.inicializar()

        board_screen = self.root.get_screen("board")
        board_screen.set_game(jogo)
        self.root.current = "board"


if __name__ == "__main__":
    JogoDaVelhaApp().run()
    