from model.store import Store
from PySide6.QtWidgets import QLineEdit, QWidget, QGridLayout, QPushButton, QLabel
from vue.window import BasicWindow
from controller.user_builder import UserBuilder



class EditUserQt(BasicWindow):

    def __init__(self, party, store: Store):
        super().__init__()

        self.setStyleSheet("background-color: #B6CFDF")

        self._party = party
        self.window = QWidget()
        self._store = store

        self.setup()

    def setup(self):
        self.setWindowTitle('Info')

        btn_edit_party = QPushButton('Edit', self)
        btn_edit_party.clicked.connect(self.edit_party)
        self.id = self._party.id
        self.creator_id = self._party.creator_id
        self.name = QLineEdit()
        self.name.setText(self._party.name)
        self.price = QLineEdit()
        self.price.setText(str(self._party.price))
        self.location = QLineEdit()
        self.location.setText(self._party.location)
        self.date = QLineEdit()
        self.date.setText(self._party.date)
        self.theme = QLineEdit()
        self.theme.setText(self._party.theme)
        self.state = QLineEdit()
        self.state.setText(self._party.state)
        self.total_place = QLineEdit()
        self.total_place.setText(str(self._party.total_place))


        self.error = QLabel()

        nameText = QLabel('Nom : ' + self._party.name)
        priceText = QLabel('Prix : ' + str(self._party.price))
        locationText = QLabel('Lieux : ' + self._party.location)
        dateText = QLabel('Date : ' + self._party.date)
        themeText = QLabel('Theme : ' + self._party.theme)
        stateText = QLabel('Etat : ' + self._party.state)
        total_placeText = QLabel('Nombre de places : ' + str(self._party.total_place))


        layout = QGridLayout()
        layout.addWidget(nameText, 1, 1, 1, 1)
        layout.addWidget(self.name, 1, 2, 1, 1)
        layout.addWidget(dateText, 2, 1, 1, 1)
        layout.addWidget(self.date, 2, 2, 1, 1)
        layout.addWidget(locationText, 3, 1, 1, 1)
        layout.addWidget(self.location, 3, 2, 1, 1)
        layout.addWidget(priceText, 4, 1, 1, 1)
        layout.addWidget(self.price, 4, 2, 1, 1)
        layout.addWidget(themeText, 5, 1, 1, 1)
        layout.addWidget(self.theme, 5, 2, 1, 1)
        layout.addWidget(total_placeText, 6, 1, 1, 1)
        layout.addWidget(self.total_place, 6, 2, 1, 1)
        layout.addWidget(stateText, 7, 1, 1, 1)
        layout.addWidget(self.state, 7, 2, 1, 1)
        layout.addWidget(btn_edit_party, 8, 2, 1, 1)
        layout.setRowStretch(8, 1)

        self.setLayout(layout)
        self.show()

    def edit_party(self):
        try:
            user_builder = UserBuilder(self._store)
            if self.password.text() == "" and self.confirmpassword.text() == "":
                newpassword = self._user.password
                user_builder.create_user(self.id, self.username.text(), self.firstname.text(), self.lastname.text(),
                                         self.email.text(),
                                         newpassword, self.gender.text(), self.age.text())
                self.update_menu()
            elif self.password.text() == self.confirmpassword.text():
                newpassword = self.password.text()
                user_builder.create_user(self.id, self.username.text(), self.firstname.text(), self.lastname.text(),
                                         self.email.text(),
                                         newpassword, self.gender.text(), self.age.text())
                self.update_menu()
            else:
                self.error.setText("Mots de passes différents")
        except:
            self.error.setText("Informations non valides")

    def update_menu(self):
        from vue.menu import MenuWindow
        self._ancienMenu.close()
        self.party = MenuWindow(self._user, self._store)
        self.party.show()
        self.close()