from PySide6.QtWidgets import QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QComboBox
from vue.window import BasicWindow
from controller.party_controller import PartyController
from model.mapping.user import User


class AddUserQt(BasicWindow):

    def __init__(self, store, show_vue: BasicWindow = None):
        #self._member_controller = member_controller
        super().__init__()
        self._store = store
        ##

        self.name = QLineEdit()
        self.place = QLineEdit()
        self.date = QLineEdit()
        self.nbPlace = QLineEdit()
        self.cost = QLineEdit()
        self.theme = QComboBox()

        self.show_vue = show_vue
        self.setup()

    def setup(self):
        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        Layout = QFormLayout()
        # Add a label and a line edit to the form layout

        Layout.addRow("Name", self.name)

        Layout.addRow("Lieu", self.place)

        Layout.addRow("Date", self.date)

        Layout.addRow("nbPlace", self.nbPlace)

        Layout.addRow("Cost", self.cost)

        self.theme.addItem("Halloween")
        self.theme.addItem("Noel")
        self.theme.addItem("Black and White")
        self.theme.addItem("Sexy")
        self.theme.addItem("None")

        Layout.addRow("Theme", self.theme)
        # Create a layout for the checkboxes
        ValidationLayout = QVBoxLayout()

        btn_add = QPushButton('Add Party', self)
        print(self._store.user.id)
        print(self._store.user().id)
        print("cc")
        btn_add.clicked.connect(self.addParty(self._store.user))
        btn_add.resize(btn_add.sizeHint())
        btn_add.move(90, 100)
        ValidationLayout.addWidget(btn_add)
        # Add some checkboxes to the layout
        btn_cancel = QPushButton('Close', self)
        btn_cancel.clicked.connect(self.quitEvent())
        btn_cancel.resize(btn_cancel.sizeHint())
        btn_cancel.move(90, 100)
        ValidationLayout.addWidget(btn_cancel)
        # Nest the inner layouts into the outer layout
        outerLayout.addLayout(Layout)
        outerLayout.addLayout(ValidationLayout)
        # Set the window's main layout
        self.setLayout(outerLayout)

    def addParty(self, user):
        party_controller = PartyController(self._store)
        # Show subscription formular
        #print(user)
        party_controller.set_creator_id(str(user.id))
        party_controller.set_date(str(self.date.text()))
        party_controller.set_location(str(self.place.text()))
        party_controller.set_name(str(self.name.text()))
        party_controller.set_theme(str(self.theme.currentText()))
        party_controller.set_total_place(str(self.nbPlace.text()))
        party_controller.set_price(str(self.cost.text()))
        party_controller.set_grade("N/A")
        party_controller.set_state("En cours")

        party_controller.register()

        self.close()

