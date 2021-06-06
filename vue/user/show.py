from PySide6.QtWidgets import QListWidget, QGridLayout,  QVBoxLayout, QPushButton, QHBoxLayout
from vue.user.add import AddUserQt
from vue.user.edit import EditUserQt
from vue.user.delete import DeleteUserQt
from vue.window import BasicWindow
from model.store import Store
from controller.party_controller import PartyController

class Party(BasicWindow):

    def __init__(self, user, store: Store):

        super().__init__()
        self._user = user
        self._store = store

        self.setStyleSheet("background-color: #B6CFDF")

        self._store = store
        self._user = user

        self.addPartyWindow = None
        self.editPartyWindow = None
        self.deletePartyWindow = None
        self.layout = QHBoxLayout()

        self.listlayout = QGridLayout()
        self.listwidget = QListWidget()

        self.btn_add_party = QPushButton('Create party', self)
        self.btn_edit_party = QPushButton('Edit party', self)
        self.btn_delete_party = QPushButton('Delete party', self)
        self.btn_add_party.setStyleSheet("background-color: #B08AAD")
        self.btn_delete_party.setStyleSheet("background-color: #B08AAD")
        self.btn_edit_party.setStyleSheet("background-color: #B08AAD")

        self.party_mapping = {}

        self.list()
        self.side_menu()
        self.setLayout(self.layout)

    def list(self):

        self.listwidget.clear()
        index = 0
        partycontroller = PartyController(self._store)
        partylist = partycontroller.get_parties_from_user(self._user)
        for party in partylist:
            self.listwidget.insertItem(index, "%s le %s Lieu : %s Thème : %s Coût : %s€" % (
                party.name,
                party.date,
                party.location,
                party.theme,
                party.price))
            self.party_mapping[index] = party
            index += 1

        self.listwidget.clicked.connect(self.clicked)
        self.listwidget.resize(self.listwidget.sizeHint())
        self.listwidget.move(0, 60)
        self.listlayout.addWidget(self.listwidget)
        self.layout.addLayout(self.listlayout)


    def side_menu(self):

        self.btn_add_party.resize(self.btn_add_party.sizeHint())
        self.btn_add_party.move(60, 20)
        self.btn_add_party.clicked.connect(self.add_party)

        self.btn_edit_party.resize(self.btn_edit_party.sizeHint())
        self.btn_edit_party.move(60, 40)
        self.btn_edit_party.setEnabled(False)
        self.btn_edit_party.clicked.connect(self.edit_party)

        self.btn_delete_party.resize(self.btn_delete_party.sizeHint())
        self.btn_delete_party.move(60, 60)
        self.btn_delete_party.setEnabled(False)
        self.btn_delete_party.clicked.connect(self.delete_party)

        btn_quit = QPushButton('Quitter', self)
        btn_quit.setStyleSheet("background-color: #B08AAD")
        btn_quit.clicked.connect(self.close)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(90, 100)

        buttonlayout = QVBoxLayout()
        buttonlayout.addWidget(self.btn_add_party)
        buttonlayout.addWidget(self.btn_edit_party)
        buttonlayout.addWidget(self.btn_delete_party)
        buttonlayout.addWidget(btn_quit)

        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('User menu')
        self.layout.addLayout(buttonlayout)

    def clicked(self):
        item = self.listwidget.currentItem()
        self.btn_edit_party.setEnabled(True)
        self.btn_delete_party.setEnabled(True)
        print(item.text())


    def add_party(self):
        if self.addPartyWindow is None:
            self.addPartyWindow = AddUserQt(self, self._user, self._store)
        self.addPartyWindow.show()

    def edit_party(self):
        if self.editPartyWindow is None:
            party = self.party_mapping[self.listwidget.currentRow()]
            self.editPartyWindow = EditUserQt(party, self._store)
        self.editPartyWindow.show()

    def delete_party(self):
        if self.deletePartyWindow is None:
            user = self.member_mapping[self.listwidget.currentRow()]
            self.deletePartyWindow = DeleteUserQt(self._member_controller, user['id'], self)
        self.deletePartyWindow.show()



