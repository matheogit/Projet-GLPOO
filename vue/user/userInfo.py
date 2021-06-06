from model.store import Store
from PySide6.QtWidgets import QLineEdit, QWidget, QGridLayout,  QVBoxLayout, QPushButton, QHBoxLayout, QLabel
from vue.window import BasicWindow


class UserInfo(BasicWindow):

    def __init__(self, user, store: Store):
        super().__init__()

        self.setStyleSheet("background-color: #B6CFDF")

        self._user = user
        self.window = QWidget()
        self._store = store
        
        self.setup()

    def setup(self):
        self.setWindowTitle('Info')
        usernameText = QLabel('Pseudo : ' + self._user.username)
        nameText = QLabel('Nom : ' + self._user.lastname)
        surnameText = QLabel('Prenom : ' + self._user.firstname)
        
        ageText = QLabel('Age : ' + self._user.age)
        emailText = QLabel('E-mail : ' + self._user.email)
        genderText = QLabel('Genre : ' + self._user.gender)
        layout = QGridLayout()
        layout.addWidget(usernameText, 1, 1, 1, 1)
        layout.addWidget(nameText, 2, 1, 1, 1)
        layout.addWidget(surnameText, 3, 1, 1, 1)        
        layout.addWidget(ageText, 4, 1, 1, 1)
        layout.addWidget(emailText, 5, 1, 1, 1)
        layout.addWidget(genderText, 6, 1, 1, 1)
        layout.setRowStretch(6, 1)

        self.setLayout(layout)
        self.show()