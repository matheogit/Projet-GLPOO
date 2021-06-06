from model.store import Store
from PySide6.QtWidgets import QLineEdit, QWidget, QGridLayout,  QVBoxLayout, QPushButton, QHBoxLayout, QLabel
from vue.window import BasicWindow
from controller.user_builder import UserBuilder


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

        btn_edit_profile = QPushButton('Edit', self)
        btn_edit_profile.clicked.connect(self.edit_profile)

        self.username = QLineEdit()
        self.username.setText(self._user.username)
        self.lastname = QLineEdit()
        self.lastname.setText(self._user.lastname)
        self.firstname = QLineEdit()
        self.firstname.setText(self._user.firstname)
        self.age = QLineEdit()
        self.age.setText(self._user.age)
        self.email = QLineEdit()
        self.email.setText(self._user.email)
        self.gender = QLineEdit()
        self.gender.setText(self._user.gender)
        self.password = QLineEdit()
        self.confirmpassword = QLineEdit()

        self.error = QLabel()

        usernameText = QLabel('Pseudo : ' + self._user.username)
        nameText = QLabel('Nom : ' + self._user.lastname)
        surnameText = QLabel('Prenom : ' + self._user.firstname)
        ageText = QLabel('Age : ' + self._user.age)
        emailText = QLabel('E-mail : ' + self._user.email)
        genderText = QLabel('Genre : ' + self._user.gender)
        passwordText = QLabel('New Password : ')
        confirmpasswordText = QLabel('Confirm : ')
        layout = QGridLayout()
        layout.addWidget(usernameText, 1, 1, 1, 1)
        layout.addWidget(self.username, 1, 2, 1, 1)
        layout.addWidget(nameText, 2, 1, 1, 1)
        layout.addWidget(self.firstname, 2, 2, 1, 1)
        layout.addWidget(surnameText, 3, 1, 1, 1)
        layout.addWidget(self.lastname, 3, 2, 1, 1)
        layout.addWidget(ageText, 4, 1, 1, 1)
        layout.addWidget(self.age, 4, 2, 1, 1)
        layout.addWidget(emailText, 5, 1, 1, 1)
        layout.addWidget(self.email, 5, 2, 1, 1)
        layout.addWidget(genderText, 6, 1, 1, 1)
        layout.addWidget(self.gender, 6, 2, 1, 1)
        layout.addWidget(passwordText, 7, 1, 1, 1)
        layout.addWidget(self.password, 7, 2, 1, 1)
        layout.addWidget(confirmpasswordText, 8, 1, 1, 1)
        layout.addWidget(self.confirmpassword, 8, 2, 1, 1)
        layout.addWidget(self.error, 9, 2, 1, 1)
        layout.addWidget(btn_edit_profile, 10, 2, 1, 1)
        layout.setRowStretch(10, 1)

        self.setLayout(layout)
        self.show()

    def edit_profile(self):
        try:
            user_builder = UserBuilder(self._store)
            if self.password.text() == "" and self.confirmpassword.text() == "":
                newpassword = self._user.password
                user_builder.update_user(self.username.text(), self.firstname.text(), self.lastname.text(), self.email.text(),
                                         newpassword, self.gender.text(), self.age.text())
                self.close()
            elif self.password.text() == self.confirmpassword.text():
                newpassword = self.password.text()
                user_builder.update_user(self.username.text(), self.firstname.text(), self.lastname.text(), self.email.text(),
                                         newpassword, self.gender.text(), self.age.text())
                self.close()
            else:
                self.error.setText("Mots de passes différents")
        except:
            self.error.setText("Informations non valides")
