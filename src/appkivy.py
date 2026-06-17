import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
sys.path.append(str(ROOT_DIR))

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen
from kivymd.color_definitions import colors

from core.jogada import Jogada
from core.jogador import Jogador
from jogos.jogo_da_velha import JogoDaVelha

KV_PATH = Path(__file__).with_name("app.kv")


class MenuScreen(MDScreen):
    pass


class ResultScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game = None

    def set_result(self, game, vencedor_nome=None):
        """Exibe o resultado do jogo."""
        self.game = game
        if game._vencedor:
            self.ids.result_message.text = f"🎉 {game._vencedor.nome} venceu! 🎉"
        else:
            self.ids.result_message.text = "Empate!"

    def voltar_menu(self):
        self.manager.current = "menu"


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
                    md_bg_color=(0.3, 0.7, 1, 1),
                )
                self.cell_buttons.append(button)
                grid.add_widget(button)

    def set_game(self, game):
        self.game = game
        self.game_over = False
        self.ids.label_result.text = ""
        self.ids.result_card.md_bg_color = (0.95, 0.3, 0.3, 0)  # Transparente inicialmente
        self._refresh_board()
        self.update_turn_label()

    def on_cell_press(self, row, col):
        if not self.game or self.game_over:
            return

        jogada = Jogada(row, col, self.game.jogador_atual)
        if not self.game.validar_jogada(jogada):
            self.ids.label_result.text = "❌ Jogada inválida. Escolha outra casa."
            self.ids.result_card.md_bg_color = (0.95, 0.3, 0.3, 0.9)
            return

        self.game.aplicar_jogada(jogada)
        self._refresh_board()

        if self.game.verificar_fim():
            self.game_over = True
            if self.game._vencedor:
                self.ids.label_result.text = f"🎉 {self.game._vencedor.nome} venceu!"
            else:
                self.ids.label_result.text = "🤝 Empate!"
            self.ids.result_card.md_bg_color = (0.2, 0.8, 0.6, 0.9)
            
            # Navega para tela de resultados após 2 segundos
            from kivy.clock import Clock
            Clock.schedule_once(lambda dt: self._show_result_screen(), 2)
            return

        self.game.avancar_turno()
        self.update_turn_label()
        self.ids.label_result.text = ""
        self.ids.result_card.md_bg_color = (0.95, 0.3, 0.3, 0)

    def _show_result_screen(self):
        """Navega para a tela de resultados."""
        result_screen = self.manager.get_screen("result")
        result_screen.set_result(self.game)
        self.manager.current = "result"

    def _refresh_board(self):
        if not self.game:
            return

        for row in range(3):
            for col in range(3):
                symbol = self.game._tabuleiro.get_casa(row, col)
                self.cell_buttons[row * 3 + col].text = symbol or ""
                # Alterar cor se está preenchido
                if symbol:
                    if symbol == "X":
                        self.cell_buttons[row * 3 + col].md_bg_color = (1, 0.3, 0.3, 1)
                    else:
                        self.cell_buttons[row * 3 + col].md_bg_color = (0.3, 0.8, 1, 1)
                else:
                    self.cell_buttons[row * 3 + col].md_bg_color = (0.3, 0.7, 1, 1)

    def update_turn_label(self):
        """Mostra de quem é a vez."""
        if self.game:
            self.ids.label_turno.text = (
                f"Turno: {self.game.jogador_atual.nome} "
                f"({self.game.jogador_atual.simbolo})"
            )

    def reset_board(self):
        if self.game:
            self.game.inicializar()
            self.game_over = False
            self.ids.label_result.text = ""
            self.ids.result_card.md_bg_color = (0.95, 0.3, 0.3, 0)
            self._refresh_board()
            self.update_turn_label()

    def voltar_menu(self):
        self.manager.current = "menu"


class JogoDaVelhaApp(MDApp):
    def build(self):
        # Configurar tema Material Design
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"
        
        return Builder.load_file(str(KV_PATH))

    def start_game(self):
        """Inicia um novo jogo com os nomes inseridos."""
        menu_screen = self.root.get_screen("menu")
        player1_name = menu_screen.ids.player1.text.strip() or "Jogador 1"
        player2_name = menu_screen.ids.player2.text.strip() or "Jogador 2"

        jogadores = [Jogador(player1_name, "X"), Jogador(player2_name, "O")]
        jogo = JogoDaVelha(jogadores)
        jogo.inicializar()

        board_screen = self.root.get_screen("board")
        board_screen.set_game(jogo)
        self.root.current = "board"

    def restart_game(self):
        """Reinicia o jogo com os mesmos jogadores."""
        board_screen = self.root.get_screen("board")
        if board_screen.game:
            board_screen.reset_board()
            self.root.current = "board"

    def go_to_menu(self):
        """Volta para o menu principal."""
        self.root.current = "menu"


if __name__ == "__main__":
    JogoDaVelhaApp().run()
