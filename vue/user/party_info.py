from model.mapping.user import User
from model.store import Store
from PySide6.QtWidgets import QLineEdit, QWidget, QGridLayout,  QVBoxLayout, QPushButton, QHBoxLayout, QLabel
from vue.window import BasicWindow
from controller.user_builder import UserBuilder

class PartyInfoQt(BasicWindow):
    def __init__(self, party, store):
        super().__init__()

        self.setStyleSheet("background-color: #B08AAD")

        self._party = party
        self.window = QWidget()
        self._store = store

        self.setup()

    def setup(self):
        self.setWindowTitle('Info de la soirée')

        user_builder = UserBuilder(self._store)
        user  = user_builder.get_user(self._party.creator_id)
        username = user.username
        nameText = QLabel('nom : ' + self._party.name)
        dateText = QLabel('date : ' + self._party.date)
        locationText = QLabel('lieu : ' + self._party.location)
        creator_nameText = QLabel('créateur : ' + username)
        total_placeText = QLabel('Places totales : ' + str(self._party.total_place))
        themeText = QLabel('Theme : ' + self._party.theme)
        priceText = QLabel('Prix : ' + str(self._party.price)+'€') 
        gradeText = QLabel('Note : ' + self._party.grade)
        stateText = QLabel('Etat : ' + self._party.state)

        layout = QGridLayout()
        layout.addWidget(nameText, 1, 1, 1, 1)
        layout.addWidget(dateText, 2, 1, 1, 1)
        layout.addWidget(locationText, 3, 1, 1, 1)
        layout.addWidget(creator_nameText, 4, 1, 1, 1)
        layout.addWidget(total_placeText, 5, 1, 1, 1)        
        layout.addWidget(themeText, 6, 1, 1, 1)
        layout.addWidget(priceText, 7, 1, 1, 1)
        layout.addWidget(gradeText, 8, 1, 1, 1)
        layout.addWidget(stateText, 9, 1, 1, 1)
        
        layout.setRowStretch(9, 1)

        self.setLayout(layout)
        self.show() 