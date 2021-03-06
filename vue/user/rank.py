from PySide6.QtWidgets import QListWidget, QGridLayout,  QVBoxLayout, QPushButton, QHBoxLayout
from vue.window import BasicWindow
from vue.user.party_info import PartyInfoQt


class PartyRank(BasicWindow):

    def __init__(self, party, store):
        super().__init__()

        self.setStyleSheet("background-color: #B6CFDF")
        self._store = store
        self._party = party
        self.infoPartyWindow = None
        self.layout = QHBoxLayout()

        self.listlayout = QGridLayout()
        self.listwidget = QListWidget()

        self.btn_info_party = QPushButton('Party info', self)

        self.rank_mapping = {}

        self.list()
        self.side_menu()
        self.setLayout(self.layout)



    def list(self):

        self.listwidget.clear()
        index = 0
        for i in range(100):
            self.listwidget.insertItem(index, str(i + 1) + " : name")
            self.rank_mapping[index] = i
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
        self.btn_info_party.setStyleSheet("background-color: #B08AAD")
        self.btn_info_party.clicked.connect(self.info_party)

        btn_quit = QPushButton('Close', self)
        btn_quit.clicked.connect(self.close)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.setStyleSheet("background-color: #B6CFDF")
        btn_quit.move(90, 100)

        buttonlayout = QVBoxLayout()
        buttonlayout.addWidget(self.btn_info_party)
        buttonlayout.addWidget(btn_quit)

        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Party rank')
        self.layout.addLayout(buttonlayout)

    def clicked(self):
        item = self.listwidget.currentItem()
        self.btn_info_party.setEnabled(True)

    def refresh(self):
        self.list()
        self.show()

    def info_party(self):
        if self.infoPartyWindow is None:
            self.infoPartyWindow = PartyInfoQt(self, self._party, self._store)
        self.infoPartyWindow.show()
