from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.app import App


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        # Add tabs
        tabs = TabbedPanel(do_default_tab=False)
        tabs.add_widget(TabbedPanelHeader(text='Cursos'))
        tabs.add_widget(TabbedPanelHeader(text='Trilhas'))
        tabs.add_widget(TabbedPanelHeader(text='Comunidade'))
        tabs.add_widget(TabbedPanelHeader(text='Perguntas'))
        tabs.add_widget(TabbedPanelHeader(text='Artigos'))
        layout.add_widget(tabs)

        search_bar = TextInput(hint_text='Pesquisar...')
        layout.add_widget(search_bar)

        level_panel = BoxLayout(orientation='vertical')
        level_panel.add_widget(Label(text='Nível'))
        level_panel.add_widget(Button(text='Iniciante'))
        level_panel.add_widget(Button(text='Intermediário'))
        level_panel.add_widget(Button(text='Avançado'))
        layout.add_widget(level_panel)

        categories = GridLayout(cols=2)
        categories.add_widget(Label(text='Saúde'))
        categories.add_widget(Button(text='Saiba Mais'))
        categories.add_widget(Label(text='Gestão'))
        categories.add_widget(Button(text='Saiba Mais'))
        categories.add_widget(Label(text='Programação'))
        categories.add_widget(Button(text='Saiba Mais'))
        layout.add_widget(categories)

        self.add_widget(layout)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        #sm.add_widget(LoginScreen(name='login'))
        #sm.add_widget(RegisterScreen(name='register'))
        #sm.add_widget(ForgotPasswordScreen(name='forgot_password'))
        sm.add_widget(HomeScreen(name='home')) 
        return sm
    
if __name__ == "__main__":
    MyApp().run()