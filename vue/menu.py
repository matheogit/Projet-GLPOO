from vue.window import BasicWindow
from PySide6.QtWidgets import QApplication, QVBoxLayout, QPushButton
from vue.user.show import Party
from vue.user.list import PartyList
from vue.user.rank import PartyRank


class MenuWindow(BasicWindow):

    def __init__(self):
        super().__init__()
        self.window = None

        self.setup()

    def setup(self):

        btn_my = QPushButton('Mes soirées', self)
        btn_my.clicked.connect(self.my_party)

        btn_list = QPushButton('Liste des soirées', self)
        btn_list.clicked.connect(self.list_party)

        btn_rank = QPushButton('Classement des soirées', self)
        btn_rank.clicked.connect(self.rank_party)

        btn_quit = QPushButton('Quitter', self)
        btn_quit.clicked.connect(QApplication.instance().quit)

        layout = QVBoxLayout()
        layout.addWidget(btn_my)
        layout.addWidget(btn_list)
        layout.addWidget(btn_rank)
        layout.addWidget(btn_quit)

        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Shop application Menu')
        self.setLayout(layout)
        self.show()


    def my_party(self):
        #if self.window is None:
        self.window = Party()
        self.window.show()

    def list_party(self):
        #if self.window is None:
        self.window = PartyList()
        self.window.show()

    def rank_party(self):
        #if self.window is None:
        self.window = PartyRank()
        self.window.show()

