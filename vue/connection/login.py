from PySide6.QtWidgets import QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel
from vue.window import BasicWindow
from controller.user_builder import UserBuilder
from vue.menu import MenuWindow

class Login(BasicWindow):

    def __init__(self, homeWindow):
        super().__init__()
        self._store = homeWindow._store
        self.homeWindow = homeWindow
        self.show_vue = None
        self.window = None

        self.username = QLineEdit()
        self.password = QLineEdit()
        self.error = QLabel()

        self.window = None
        self.setStyleSheet("color: #000000;" "background-color: #B6CFDF;")
        self.setup()

    def setup(self):
        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        Layout = QFormLayout()
        # Add a label and a line edit to the form layout

        Layout.addRow("Utilisateur", self.username)

        Layout.addRow("Mot de passe", self.password)

        Layout.addRow(self.error)

        # Create a layout for the checkboxes
        ValidationLayout = QVBoxLayout()

        btn_login = QPushButton('Se connecter', self)
        btn_login.clicked.connect(self.loginpage)
        btn_login.resize(btn_login.sizeHint())
        btn_login.setStyleSheet("background-color: #B08AAD;")
        btn_login.move(90, 100)
        ValidationLayout.addWidget(btn_login)
        # Add some checkboxes to the layout
        btn_cancel = QPushButton('Quitter', self)
        btn_cancel.clicked.connect(self.quitEvent)
        btn_cancel.resize(btn_cancel.sizeHint())
        btn_cancel.setStyleSheet("background-color: #B08AAD;")
        btn_cancel.move(90, 100)
        ValidationLayout.addWidget(btn_cancel)
        # Nest the inner layouts into the outer layout
        outerLayout.addLayout(Layout)
        outerLayout.addLayout(ValidationLayout)
        # Set the window's main layout
        self.setWindowTitle('Connexion')
        self.setLayout(outerLayout)

    def loginpage(self):
        user_builder = UserBuilder(self._store)
        try:
            user = user_builder.get_user_by_username(self.username.text())
            if user.password == self.password.text():
                self.window = MenuWindow(user, self._store)
                self.window.show()
                self.homeWindow.close()
                self.close()
            else:
                self.error.setText("Mauvais mot de passe")
        except:
            self.error.setText("Utilisateur inexistant")