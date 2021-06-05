from PySide6.QtWidgets import QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QComboBox
from vue.window import BasicWindow
from vue.menu import MenuWindow

class Login(BasicWindow):

    def __init__(self):
        #self._member_controller = member_controller
        super().__init__()
        ##

        self.show_vue = None
        self.window = None

        self.username = QLineEdit()
        self.password = QLineEdit()

        self.window = None
        self.setup()

    def setup(self):
        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        Layout = QFormLayout()
        # Add a label and a line edit to the form layout

        Layout.addRow("Utilisateur", self.username)

        Layout.addRow("Mot de passe", self.password)

        # Create a layout for the checkboxes
        ValidationLayout = QVBoxLayout()

        btn_login = QPushButton('Se connecter', self)
        btn_login.clicked.connect(self.loginpage)
        btn_login.resize(btn_login.sizeHint())
        btn_login.move(90, 100)
        ValidationLayout.addWidget(btn_login)
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

    def loginpage(self):
        self.close()
        self.window = MenuWindow()
        self.window.show()


