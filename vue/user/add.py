from PySide6.QtWidgets import QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QComboBox
from vue.window import BasicWindow


class AddUserQt(BasicWindow):

    def __init__(self, show_vue: BasicWindow = None):
        #self._member_controller = member_controller
        super().__init__()
        ##

        self.name = QLineEdit()
        self.date = QLineEdit()
        self.place = QLineEdit()
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

        Layout.addRow("Date", self.date)

        Layout.addRow("Place", self.place)

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
        btn_add.clicked.connect(self.addParty)
        btn_add.resize(btn_add.sizeHint())
        btn_add.move(90, 100)
        ValidationLayout.addWidget(btn_add)
        # Add some checkboxes to the layout
        btn_cancel = QPushButton('Close', self)
        btn_cancel.clicked.connect(self.quitEvent)
        btn_cancel.resize(btn_cancel.sizeHint())
        btn_cancel.move(90, 100)
        ValidationLayout.addWidget(btn_cancel)
        # Nest the inner layouts into the outer layout
        outerLayout.addLayout(Layout)
        outerLayout.addLayout(ValidationLayout)
        # Set the window's main layout
        self.setLayout(outerLayout)

    def addParty(self):
        # Show subscription formular
        data = {'Name': self.name.text(),
                'Date': self.date.text(),
                'Place': self.place.text(),
                'Cost': self.cost.text(),
                'Theme': self.theme.currentText()}
        print(data)
        '''self._member_controller.create_member(data)

        members = self._member_controller.list_members()

        print("Members: ")
        for member in members:
            print("* %s %s (%s) - %s" % (
                member['firstname'].capitalize(),
                member['lastname'].capitalize(),
                member['email'],
                member['type']))'''
        if self.show_vue is not None:
            self.show_vue.refresh()
        self.close()

