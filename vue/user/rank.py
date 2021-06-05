from PySide6.QtWidgets import QListWidget, QGridLayout,  QVBoxLayout, QPushButton, QHBoxLayout
from vue.window import BasicWindow
from vue.user.info import InfoUserQt


class PartyRank(BasicWindow):

    def __init__(self):
        super().__init__()

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
        self.btn_info_party.clicked.connect(self.info_party)

        btn_quit = QPushButton('Close', self)
        btn_quit.clicked.connect(self.close)
        btn_quit.resize(btn_quit.sizeHint())
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
        print(item.text())

    def refresh(self):
        self.list()
        self.show()

    def info_party(self):
        if self.infoPartyWindow is None:
            self.infoPartyWindow = InfoUserQt(self)
        self.infoPartyWindow.show()
