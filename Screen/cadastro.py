from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.graphics import Rectangle, Line
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
import sqlite3

class RegisterScreen(Screen):

    def register_user(self, instance):
        # Verificar se todos os campos estão preenchidos
        if not all(field.text.strip() for field in [self.name_input, self.last_name_input, self.email_input, self.password_input, self.repeat_password_input]):
            self.show_popup("Erro", "Todos os campos são obrigatórios.")
            return       

        # Verificar se as senhas coincidem
        if self.password_input.text != self.repeat_password_input.text:
            self.show_popup("Erro", "As senhas não coincidem.")
            return

        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect('BD/users.db')
        cursor = conn.cursor()

        # Verificar se o email já está cadastrado
        cursor.execute("SELECT * FROM users WHERE email=?", (self.email_input.text,))
        if cursor.fetchone():
            self.show_popup("Erro", "Este e-mail já está registrado.")
            conn.close()
            cursor.close()
            return

        # Inserir os detalhes do usuário no banco de dados
        cursor.execute("INSERT INTO users (name, last_name, email, password) VALUES (?, ?, ?, ?)",
                       (self.name_input.text, self.last_name_input.text, self.email_input.text, self.password_input.text))
        conn.commit()

        # Fechar a conexão com o banco de dados
        conn.close()
        cursor.close()

        # Após o registro, retornar à tela de login
        self.parent.current = 'login'

    def go_back_to_login(self, instance):
        self.parent.current = 'login'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        # Adicionar imagem de fundo
        with layout.canvas.before:
            self.background = Rectangle(source='IMG/Cadastro.png', pos=layout.pos, size=layout.size)

        text_color = (1, 1, 1, 1)  # Cor do texto

        # Campo de entrada para nome
        self.name_input = TextInput(hint_text="Seu nome", multiline=False, background_color=(0, 0, 0, 0), foreground_color=text_color, size_hint=(None, None), size=(150, 30))
        self.name_input.pos_hint = {'center_x': 0.1, 'center_y': 0.6}

        # Campo de entrada para sobrenome
        self.last_name_input = TextInput(hint_text="Seu sobrenome", multiline=False, background_color=(0, 0, 0, 0), foreground_color=text_color, size_hint=(None, None), size=(155, 80))
        self.last_name_input.pos_hint = {'center_x': 0.1, 'center_y': 0.4}

        # Campo de entrada para e-mail
        self.email_input = TextInput(hint_text="E-mail", multiline=False, background_color=(0, 0, 0, 0), foreground_color=text_color, size_hint=(None, None), size=(150,135))
        self.email_input.pos_hint = {'center_x': 0.1, 'center_y': 0.2}

        # Campo de entrada para senha
        self.password_input = TextInput(hint_text="Senha", password=True, multiline=False, background_color=(0, 0, 0, 0), foreground_color=text_color, size_hint=(None, None), size=(300, 40))
        self.password_input.pos_hint = {'center_x': 0.7, 'center_y': 0.6}

        # Campo de entrada para repetir a senha
        self.repeat_password_input = TextInput(hint_text="Repita a Senha", password=True, multiline=False, background_color=(0, 0, 0, 0), foreground_color=text_color, size_hint=(None, None), size=(300, 29))
        self.repeat_password_input.pos_hint = {'center_x': 0.7, 'center_y': 0.5}

        # Adicionar CheckBoxes para seleção de gênero
        self.gender_female = CheckBox(group='gender', size_hint=(None, None), size=(30, 30))
        self.gender_female.pos_hint = {'center_x': 0.77, 'center_y': 0.35}

        self.gender_male = CheckBox(group='gender', size_hint=(None, None), size=(30, 30))
        self.gender_male.pos_hint = {'center_x': 0.67, 'center_y': 0.35}

        self.gender_other = CheckBox(group='gender', size_hint=(None, None), size=(30, 30))
        self.gender_other.pos_hint = {'center_x': 0.57, 'center_y': 0.35}

        # Adicionar TextInput para outros gêneros
        self.other_gender_input = TextInput(hint_text="Outro (especifique)", multiline=False, background_color=(0, 0, 0, 0), opacity=0, foreground_color=text_color, size_hint=(None, None), size=(200, 30))
        self.other_gender_input.pos_hint = {'center_x': 0.5, 'center_y': 0.1}

        # Botão de registro
        self.register_button = Button(text="Registrar", background_normal='', size_hint=(None, None), size=(100, 50), background_color=(0, 0, 0, 0), color=text_color)
        self.register_button.bind(on_press=self.register_user)
        self.register_button.pos_hint = {'center_x': 0.61, 'center_y': 0.25}

        # Botão de voltar
        back_button = Button(text="Voltar", size_hint=(None, None), size=(100, 50), background_color=(0, 0, 0, 0))
        back_button.bind(on_press=self.go_back_to_login)
        back_button.pos_hint = {'center_x': 0.6, 'center_y': 0.05}

        # Adicionar widgets ao layout
        layout.add_widget(Label(text="Cadastre-se", font_size=36, color=(1, 1, 1, 1), size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.9}))
        layout.add_widget(self.name_input)
        layout.add_widget(self.last_name_input)
        layout.add_widget(self.email_input)
        layout.add_widget(self.password_input)
        layout.add_widget(self.repeat_password_input)
        layout.add_widget(self.gender_female)
        layout.add_widget(self.gender_male)
        layout.add_widget(self.gender_other)
        layout.add_widget(self.other_gender_input)
        layout.add_widget(self.register_button)
        layout.add_widget(back_button)

        self.add_widget(layout)

        # Atualizar o tamanho da imagem de fundo quando a janela for redimensionada
        self.bind(size=self._update_background_size)

    def _update_background_size(self, instance, value):
        self.background.size = instance.size
        
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        # sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        # sm.add_widget(ForgotPasswordScreen(name='forgot_password'))
        # sm.add_widget(HomeScreen(name='home')) 
        return sm
    
if __name__ == "__main__":
    MyApp().run()