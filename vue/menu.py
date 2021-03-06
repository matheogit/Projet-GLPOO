from vue.window import BasicWindow
from PySide6.QtWidgets import QPushButton, QLabel, QGridLayout, QWidget
from vue.user.show import Party
from vue.user.list import PartyList
from vue.user.rank import PartyRank
from model.store import Store
from vue.user.userInfo import UserInfo

class MenuWindow(BasicWindow):

    def __init__(self, user, store: Store):
        super().__init__()
        self.window = QWidget()
        self._store = store
        self._user = user

        self.setup()

        self.setStyleSheet("background-color: #B08AAD;")

    def setup(self):

        self.setWindowTitle('Menu principal')

        btn_profil = QPushButton('Profil', self)
        btn_profil.clicked.connect(self.my_info)
        btn_profil.setStyleSheet("background-color: #B6CFDF;")
        
        textProfil = QLabel('Bonjour, ' + self._user.username)

        btn_my = QPushButton('Mes soirées', self)
        btn_my.clicked.connect(self.my_party)
        btn_my.setStyleSheet("background-color: #B6CFDF;")

        btn_list = QPushButton('Liste des soirées', self)
        btn_list.clicked.connect(self.list_party)
        btn_list.setStyleSheet("background-color: #B6CFDF;")

        btn_rank = QPushButton('Classement des soirées', self)
        btn_rank.clicked.connect(self.rank_party)
        btn_rank.setStyleSheet("background-color: #B6CFDF;")

        btn_quit = QPushButton('Déconnexion', self)
        btn_quit.clicked.connect(self.disconnect)
        btn_quit.setStyleSheet("background-color: #B6CFDF;")

        layout = QGridLayout()
        layout.addWidget(btn_profil, 0, 0, 1, 1)
        layout.addWidget(textProfil, 0, 3, 1, 1)
        layout.addWidget(btn_my, 1, 1, 1, 1)
        layout.addWidget(btn_list, 2, 1, 1, 1)
        layout.addWidget(btn_rank, 3, 1, 1, 1)
        layout.addWidget(btn_quit, 4, 1, 1, 1)
        layout.setRowStretch(4, 1)

        self.setGeometry(100, 100, 600, 600)
        self.setLayout(layout)
        self.show()


    def my_info(self):
        self.window = UserInfo(self._user, self._store, self)
        self.window.show()

    def my_party(self):
        # if self.window is None:
        self.window = Party(self._user, self._store)
        self.window.show()


    def list_party(self):
        # if self.window is None:
        self.window = PartyList(self._user, self._store)
        self.window.show()


    def rank_party(self):
        # if self.window is None:
        self.window = PartyRank(self._user, self._store)
        self.window.show()

    def disconnect(self):
        from vue.home import LoginWindow
        self.window = LoginWindow(self._store)
        self.window.show()
        self.close() 