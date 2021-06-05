from PySide6.QtWidgets import QListWidget, QGridLayout,  QVBoxLayout, QPushButton, QHBoxLayout
from vue.user.info import InfoUserQt
from vue.user.search import SearchUserQt
from vue.window import BasicWindow


class PartyList(BasicWindow):

    def __init__(self, user):
        super().__init__()

        self.user = user
        self.infoPartyWindow = None
        self.searchPartyWindow = None
        self.layout = QHBoxLayout()

        self.listlayout = QGridLayout()
        self.listwidget = QListWidget()

        self.btn_info_party = QPushButton('Party info', self)
        self.btn_search_party = QPushButton('Search party', self)

        self.member_mapping = {}

        self.list()
        self.side_menu()
        self.setLayout(self.layout)

    def list(self):

        self.listwidget.clear()
        index = 0
        for user in self._member_controller.list_members():
            self.listwidget.insertItem(index, "* %s %s (%s) - %s" % (
                member['firstname'],
                member['lastname'],
                member['email'],
                member['type']))
            self.member_mapping[index] = member
            index += 1

        self.listwidget.clicked.connect(self.clicked)
        self.listwidget.resize(self.listwidget.sizeHint())
        self.listwidget.move(0, 60)
        self.listlayout.addWidget(self.listwidget)
        self.layout.addLayout(self.listlayout)

    def side_menu(self):

        self.btn_info_party.resize(self.btn_info_party.sizeHint())
        self.btn_info_party.move(60, 20)
        self.btn_info_party.setEnabled(False)
        self.btn_info_party.clicked.connect(self.info_party)

        self.btn_search_party.resize(self.btn_search_party.sizeHint())
        self.btn_search_party.move(60, 80)
        self.btn_search_party.clicked.connect(self.search_party)

        btn_quit = QPushButton('Close', self)
        btn_quit.clicked.connect(self.close)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(90, 100)

        buttonlayout = QVBoxLayout()
        buttonlayout.addWidget(self.btn_info_party)
        buttonlayout.addWidget(self.btn_search_party)
        buttonlayout.addWidget(btn_quit)

        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Party list')
        self.layout.addLayout(buttonlayout)

    def clicked(self):
        item = self.listwidget.currentItem()
        self.btn_info_party.setEnabled(True)
        print(item.text())

    def refresh(self):
        self.list()
        self.show()

    def info_party(self):
        if self.infoPartyWindow is None:
            self.infoPartyWindow = InfoUserQt(self)
        self.infoPartyWindow.show()

    def search_party(self):
        if self.searchPartyWindow is None:
            self.searchPartyWindow = SearchUserQt(self._member_controller, self)
        self.searchPartyWindow.show()