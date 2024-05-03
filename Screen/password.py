from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.utils import get_color_from_hex
from kivy.app import App

text_color = get_color_from_hex("#FFFFFF")

class ForgotPasswordScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=(30, 30, 30, 30))

        self.email_input = TextInput(hint_text="E-mail", multiline=False, background_color=(1, 1, 1, 0.8), size_hint=(None, None), size=(100, 40), font_size=18)
        recover_button = Button(text="Recuperar Senha", background_normal='', size_hint=(None, None), size=(100, 40), background_color=(0, 0, 0, 0), color=text_color)
        recover_button.bind(on_press=self.recover_password)
        back_button = Button(text="Voltar", size_hint=(None, None), size=(100, 40), background_normal='', background_color=(0, 0, 0, 0), color=text_color)
        back_button.bind(on_press=self.go_back_to_login)

        layout.add_widget(Label(text="Esqueci a Senha", font_size=36, color=(1, 1, 1, 1)))
        layout.add_widget(self.email_input)
        layout.add_widget(recover_button)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def recover_password(self, instance):
        # Por enquanto, vamos apenas exibir uma mensagem
        self.show_popup("Recuperar Senha", "Instruções de recuperação de senha enviadas para o seu e-mail.")

    def go_back_to_login(self, instance):
        self.parent.current = 'login'

    def show_popup(self, title, content):
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(400, 200))
        popup.open()

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        #sm.add_widget(LoginScreen(name='login'))
        #sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(ForgotPasswordScreen(name='forgot_password'))
        # sm.add_widget(HomeScreen(name='home')) 
        return sm
    
if __name__ == "__main__":
    MyApp().run()