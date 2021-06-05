from PySide6.QtWidgets import QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QComboBox
from vue.window import BasicWindow
from vue.menu import MenuWindow
from controller.user_builder import UserBuilder
from model.store import Store

class Register(BasicWindow):

    def __init__(self, store: Store, show_vue: BasicWindow = None):
        #self._member_controller = member_controller
        super().__init__()
        self._store = store
        ##

        self.pseudo = QLineEdit()
        self.prenom = QLineEdit()
        self.nom = QLineEdit()
        self.email = QLineEdit()
        self.gender = QLineEdit()
        self.age = QLineEdit()

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

        Layout.addRow("Genre", self.gender)

        Layout.addRow("Age", self.age)

        Layout.addRow("Mot de passe", self.password)

        Layout.addRow("Mot de passe", self.checkpassword)

        # Create a layout for the checkboxes
        ValidationLayout = QVBoxLayout()

        btn_register = QPushButton('Créer le compte', self)
        btn_register.resize(btn_register.sizeHint())
        btn_register.move(90, 100)
        ValidationLayout.addWidget(btn_register)
        btn_register.clicked.connect(self.registerpage)
        # Add some checkboxes to the layout
        btn_cancel = QPushButton('Close', self)
        btn_cancel.resize(btn_cancel.sizeHint())
        btn_cancel.move(90, 100)
        ValidationLayout.addWidget(btn_cancel)
        btn_cancel.clicked.connect(self.quitEvent)

        # Nest the inner layouts into the outer layout
        outerLayout.addLayout(Layout)
        outerLayout.addLayout(ValidationLayout)
        # Set the window's main layout
        self.setLayout(outerLayout)

    def registerpage(self):
        user_builder = UserBuilder(self._store)
        if self.password.text() == self.checkpassword.text():
            user_builder.create_user(self.pseudo.text(), self.prenom.text(), self.nom.text(), self.email.text(), self.password.text(), self.gender.text(), self.age.text())
            self.close()
        else:
            print("ERROR")
        

