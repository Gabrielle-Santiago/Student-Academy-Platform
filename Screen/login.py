from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.graphics import Rectangle, Line
import sqlite3

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        # Adicionar imagem de fundo
        with layout.canvas.before:
            self.background = Rectangle(source='TelaLogin.jpg', pos=layout.pos, size=layout.size)

        text_color = (1, 1, 1, 1)  # Cor do texto

        # Definir tamanho dos campos de e-mail e senha
        self.email_input = TextInput(hint_text="E-mail", multiline=False, background_color=(0, 0, 0, 0),size_hint=(None, None), size=(150, 50), font_size=15, foreground_color=text_color, pos_hint={'x': 0, 'y': 0.5})
        self.password_input = TextInput(hint_text="Senha", password=True, background_color=(0, 0, 0, 0), multiline=False, size_hint=(None, None), size=(150, 45), font_size=15, foreground_color=text_color, pos_hint={'x': 0, 'y': 0.4})

        # Adicionar os campos de e-mail e senha
        layout.add_widget(Label(text="Student Academy Platform", font_size=50, color=(1, 1, 1, 1), pos_hint={'x': 0.2, 'y': 0.7}))
        layout.add_widget(self.email_input)
        layout.add_widget(self.password_input)

        # Posicionar os botões "Registrar" e "Esqueci a senha" lado a lado acima do botão "Entrar"
        register_button = Button(text="Registrar", font_size=13, size_hint=(None, None), size=(40, 40), background_normal='', background_color=(0, 0, 0, 0), color=text_color, pos_hint={'x': 0.02, 'y': 0.35})
        register_button.bind(on_press=self.go_to_register)  # Alterada a função para ir para a tela de registro

        forgot_password_button = Button(text="Esqueci a senha",font_size=13, size_hint=(None, None), size=(150, 40), background_normal='', background_color=(0, 0, 0, 0), color=text_color, pos_hint={'x': 0.15, 'y': 0.35})
        forgot_password_button.bind(on_press=self.go_to_forgot_password)

        login_button = Button(text="Entrar", background_normal='', size_hint=(None, None), size=(90, 70), background_color=(0, 0, 0, 0), color=text_color, pos_hint={'x': 0.10, 'y': 0.2})
        login_button.bind(on_press=self.check_login)

        # Adicionar os botões ao FloatLayout
        layout.add_widget(register_button)
        layout.add_widget(forgot_password_button)
        layout.add_widget(login_button)
        self.add_widget(layout)
        layout.add_widget(Label(text="Student Academy Platform", font_size=36, color=(1, 1, 1, 1), font_name='IMG\BebasNeue-Regular.otf', pos_hint={'center_x': 0.5, 'y': 0.3}))

    def update_line(self, instance, value):
        instance.canvas.after.clear()
        with instance.canvas.after:
            Line(points=[instance.x, instance.y, instance.right, instance.y], width = 2)

    def on_size(self, *args):
        self.background.size = self.size
        self.background.pos = self.pos

    def check_login(self, instance):
        email = self.email_input.text.strip()
        password = self.password_input.text.strip()

        # Verificar se o email e a senha foram fornecidos
        if not email or not password:
            self.show_popup("Erro", "Por favor, insira o e-mail e a senha.")
            return

        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        # Verificar se o usuário existe no banco de dados
        cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = cursor.fetchone()

        # Fechar a conexão com o banco de dados
        conn.close()

        if user:
            print("Login bem-sucedido")
            self.parent.current = 'home'
        else:
            self.show_popup("Login Falhou", "Usuário ou senha incorretos.")

    def go_to_register(self, instance):
        self.parent.current = 'register'  # Alterado para ir para a tela de registro

    def go_to_forgot_password(self, instance):
        self.parent.current = 'forgot_password'

    def show_popup(self, title, content):
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(400, 200))
        popup.open()
