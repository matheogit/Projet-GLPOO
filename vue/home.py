from model.store import Store
from vue.window import BasicWindow
from PySide6.QtWidgets import QApplication, QVBoxLayout, QPushButton
from vue.connection.login import Login
from vue.connection.register import Register



class LoginWindow(BasicWindow):

    def __init__(self, store: Store):
        super().__init__()
        self.window = None
        self._store = store

        self.setup()

    def setup(self):

        btn_login = QPushButton('Se connecter', self)
        btn_login.clicked.connect(self.login)

        btn_register = QPushButton('Créer un compte', self)
        btn_register.clicked.connect(self.register)

        btn_quit = QPushButton('Quitter', self)
        btn_quit.clicked.connect(QApplication.instance().quit)

        layout = QVBoxLayout()
        layout.addWidget(btn_login)
        layout.addWidget(btn_register)
        layout.addWidget(btn_quit)

        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Page de connection')
        self.setLayout(layout)
        self.show()


    def login(self):
        #if self.window is None:
        self.window = Login(self._store)
        self.window.show()

    def register(self):
        #if self.window is None:
        self.window = Register(self._store)
        self.window.show()
