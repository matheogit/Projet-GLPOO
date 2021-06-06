from PySide6.QtWidgets import QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QComboBox, QLabel
from vue.window import BasicWindow
from controller.user_builder import UserBuilder
from model.store import Store


class Register(BasicWindow):

    def __init__(self, store: Store):
        super().__init__()
        self._store = store

        self.setStyleSheet("background-color: #B08AAD;")


        self.pseudo = QLineEdit()
        self.prenom = QLineEdit()
        self.nom = QLineEdit()
        self.email = QLineEdit()
        self.gender = QComboBox()
        self.age = QLineEdit()
        self.error = QLabel()

        self.password = QLineEdit()
        self.checkpassword = QLineEdit()

        self.window = None
        self.setup()

    def setup(self):
        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        Layout = QFormLayout()
        # Add a label and a line edit to the form layout

        Layout.addRow("Pseudo", self.pseudo)

        Layout.addRow("Prénom", self.prenom)

        Layout.addRow("Nom", self.nom)

        Layout.addRow("Email", self.email)

        self.gender.addItem("Homme")

        self.gender.addItem("Femme")

        Layout.addRow("Genre", self.gender)

        Layout.addRow("Age", self.age)

        Layout.addRow("Mot de passe", self.password)

        Layout.addRow("Mot de passe", self.checkpassword)

        Layout.addRow(self.error)

        # Create a layout for the checkboxes
        ValidationLayout = QVBoxLayout()

        btn_register = QPushButton('Créer le compte', self)
        btn_register.resize(btn_register.sizeHint())
        btn_register.move(90, 100)
        btn_register.setStyleSheet("background-color: #B6CFDF;")
        ValidationLayout.addWidget(btn_register)
        btn_register.clicked.connect(self.registerpage)
        # Add some checkboxes to the layout
        btn_cancel = QPushButton('Fermer', self)
        btn_cancel.resize(btn_cancel.sizeHint())
        btn_cancel.move(90, 100)
        btn_cancel.setStyleSheet("background-color: #B6CFDF;")
        ValidationLayout.addWidget(btn_cancel)
        btn_cancel.clicked.connect(self.quitEvent)

        # Nest the inner layouts into the outer layout
        outerLayout.addLayout(Layout)
        outerLayout.addLayout(ValidationLayout)
        # Set the window's main layout
        self.setWindowTitle('Inscription')
        self.setLayout(outerLayout)

    def registerpage(self):
        user_builder = UserBuilder(self._store)
        if self.password.text() == self.checkpassword.text():
            try:
                if self.gender.currentText() == "Homme":
                    gender = "M"
                else:
                    gender = "W"
                user_builder.create_user(None, self.pseudo.text(), self.prenom.text(), self.nom.text(), self.email.text(), self.password.text(), gender, self.age.text())
                self.close()
            except:
                self.error.setText("Vous avez mal rempli les informations")
        else:
            self.error.setText("Les mots de passes ne sont pas identiques")