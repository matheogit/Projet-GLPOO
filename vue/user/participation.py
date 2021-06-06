from PySide6.QtWidgets import QListWidget, QGridLayout,  QVBoxLayout, QPushButton, QHBoxLayout
from vue.user.party_info import PartyInfoQt
from vue.user.search import SearchUserQt
from vue.window import BasicWindow
from model.store import Store
from controller.party_controller import PartyController


class Participation(BasicWindow):

    def __init__(self, user, store: Store):
        super().__init__()

        self._user = user
        self._store = store
        self.infoPartyWindow = None
        self.searchPartyWindow = None
        self.partycontroller = PartyController(self._store)
        self.layout = QHBoxLayout()

        self.listlayout = QGridLayout()
        self.listwidget = QListWidget()
        self.setStyleSheet("background-color: #B6CFDF")

        self.btn_unregister = QPushButton('Se désinscrire', self)
        self.btn_note = QPushButton('Noter', self)

        self.party_mapping = {}

        self.list_1()
        self.side_menu_1()
        self.list_2()
        self.side_menu_2()
        self.setLayout(self.layout)

    def list_1(self):
        self.listwidget.clear()
        index = 0

        self.partylist = self.partycontroller.get_all_parties()
        for party in self.partylist:
            self.listwidget.insertItem(index, "Soirée: %s date: %s lieu: %s thème: %s prix: %s euros" % (
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

    def side_menu_1(self):

        self.btn_info_party.resize(self.btn_info_party.sizeHint())
        self.btn_info_party.move(60, 20)
        self.btn_info_party.setEnabled(False)
        self.btn_info_party.clicked.connect(self.info_party)
        self.btn_info_party.setStyleSheet("background-color: #B08AAD")

        self.btn_participate_party.resize(self.btn_participate_party.sizeHint())
        self.btn_participate_party.move(60, 40)
        self.btn_participate_party.setEnabled(False)
        self.btn_participate_party.clicked.connect(self.participate_party)
        self.btn_participate_party.setStyleSheet("background-color: #B08AAD")

        self.btn_search_party.resize(self.btn_search_party.sizeHint())
        self.btn_search_party.move(60, 80)
        self.btn_search_party.clicked.connect(self.search_party)
        self.btn_search_party.setStyleSheet("background-color: #B08AAD")

        btn_quit = QPushButton('Close', self)
        btn_quit.clicked.connect(self.close)
        btn_quit.setStyleSheet("background-color: #B08AAD")
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(90, 100)

        buttonlayout = QVBoxLayout()
        buttonlayout.addWidget(self.btn_info_party)
        buttonlayout.addWidget(self.btn_participate_party)
        buttonlayout.addWidget(self.btn_search_party)
        buttonlayout.addWidget(btn_quit)

        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Party list')
        self.layout.addLayout(buttonlayout)

    def list_2(self):
        self.listwidget.clear()
        index = 0

        self.partylist = self.partycontroller.get_all_parties()
        for party in self.partylist:
            self.listwidget.insertItem(index, "Soirée: %s date: %s lieu: %s thème: %s prix: %s euros" % (
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

    def side_menu_2(self):

        self.btn_info_party.resize(self.btn_info_party.sizeHint())
        self.btn_info_party.move(60, 20)
        self.btn_info_party.setEnabled(False)
        self.btn_info_party.clicked.connect(self.info_party)
        self.btn_info_party.setStyleSheet("background-color: #B08AAD")

        self.btn_participate_party.resize(self.btn_participate_party.sizeHint())
        self.btn_participate_party.move(60, 40)
        self.btn_participate_party.setEnabled(False)
        self.btn_participate_party.clicked.connect(self.participate_party)
        self.btn_participate_party.setStyleSheet("background-color: #B08AAD")

        self.btn_search_party.resize(self.btn_search_party.sizeHint())
        self.btn_search_party.move(60, 80)
        self.btn_search_party.clicked.connect(self.search_party)
        self.btn_search_party.setStyleSheet("background-color: #B08AAD")

        btn_quit = QPushButton('Close', self)
        btn_quit.clicked.connect(self.close)
        btn_quit.setStyleSheet("background-color: #B08AAD")
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(90, 100)

        buttonlayout = QVBoxLayout()
        buttonlayout.addWidget(self.btn_info_party)
        buttonlayout.addWidget(self.btn_participate_party)
        buttonlayout.addWidget(self.btn_search_party)
        buttonlayout.addWidget(btn_quit)

        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Party list')
        self.layout.addLayout(buttonlayout)

    def clicked(self):
        self.btn_info_party.setEnabled(True)
        #Test si la personne peut participer ou participe déjà
        rowParty = self.listwidget.currentRow()
        test = self.partycontroller.is_user_participate(self._user, self.partylist[rowParty])
        if test:
            self.btn_participate_party.setText('Vous participez déjà')
            self.btn_participate_party.setEnabled(False)
        else:
            self.btn_participate_party.setEnabled(True)
            self.btn_participate_party.setText('Participer')

    def refresh(self):
        self.list()
        self.show()

    def info_party(self):
        tmp = self.listwidget.currentRow()
        party = self.partylist[tmp]
        self.infoPartyWindow = PartyInfoQt(party, self._store)
        self.infoPartyWindow.show()

    def participate_party(self):
        rowParty = self.listwidget.currentRow()
        self.partycontroller.participate_to_party(self._user, self.partylist[rowParty], '')
        self.btn_participate_party.setText('Vous participez déjà')
        self.btn_participate_party.setEnabled(False)

    def search_party(self):
        if self.searchPartyWindow is None:
            self.searchPartyWindow = SearchUserQt(self._member_controller, self)
        self.searchPartyWindow.show()