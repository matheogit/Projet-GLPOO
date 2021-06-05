from PySide6.QtWidgets import QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QComboBox
from vue.window import BasicWindow
from vue.menu import MenuWindow


class Register(BasicWindow):

    def __init__(self, show_vue: BasicWindow = None):
        #self._member_controller = member_controller
        super().__init__()
        ##

        self.name = QLineEdit()
        self.surname = QLineEdit()
        self.email = QLineEdit()
        self.age = QLineEdit()
        self.username = QLineEdit()
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

        Layout.addRow("Prénom", self.name)

        Layout.addRow("Nom", self.surname)

        Layout.addRow("Email", self.email)

        Layout.addRow("Age", self.age)

        Layout.addRow("Utilisateur", self.username)

        Layout.addRow("Mot de passe", self.password)

        Layout.addRow("Mot de passe", self.checkpassword)

        # Create a layout for the checkboxes
        ValidationLayout = QVBoxLayout()

        btn_register = QPushButton('Créer le compte', self)
        btn_register.clicked.connect(self.registerpage)
        btn_register.resize(btn_register.sizeHint())
        btn_register.move(90, 100)
        ValidationLayout.addWidget(btn_register)
        # Add some checkboxes to the layout
        btn_cancel = QPushButton('Close', self)
        btn_cancel.clicked.connect(self.quitEvent)
        btn_cancel.resize(btn_cancel.sizeHint())
        btn_cancel.move(90, 100)
        ValidationLayout.addWidget(btn_cancel)
        # Nest the inner layouts into the outer layout
        outerLayout.addLayout(Layout)
        outerLayout.addLayout(ValidationLayout)
        # Set the window's main layout
        self.setLayout(outerLayout)

    def registerpage(self):
        self.window = MenuWindow()
        self.window.show()

