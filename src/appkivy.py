from kivymd.app import Builder, MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.gridlayout import MDGridLayout

class MyApp(MDApp):
    def build(self):
        screen_manager = MDScreenManager()

        screen1 = MDScreen()
        layout1 = MDGridLayout(cols=1, padding=10, spacing=10)
        button1 = MDRaisedButton(text="Go to Screen 2")
        button1.bind(on_release=lambda x: setattr(screen_manager, 'current', 'screen2'))
        layout1.add_widget(button1)
        screen1.add_widget(layout1)

        screen2 = MDScreen()
        layout2 = MDGridLayout(cols=1, padding=10, spacing=10)
        button2 = MDRaisedButton(text="Go to Screen 1")
        button2.bind(on_release=lambda x: setattr(screen_manager, 'current', 'screen1'))
        layout2.add_widget(button2)
        screen2.add_widget(layout2)

        screen_manager.add_widget(screen1)
        screen_manager.add_widget(screen2)

        return Builder.load_file("app.kv")
    