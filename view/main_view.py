from model.store import Store
from controller.customer_builder import CustomerBuilder
from view.common import Common
from view.view import View
from exceptions import ResourceNotFound
from view.user_view_factory import UserViewFactory
from PySide6.QtWidgets import QApplication, QVBoxLayout, QPushButton
from view.window import BasicWindow


class MainView(BasicWindow):

    def __init__(self):
        super().__init__()
        self.listUserWindow = None

        self.setup()

    def setup(self):
        btn_list = QPushButton('plz', self)
        btn_list.resize(btn_list.sizeHint())
        btn_list.move(0, 0)
        btn_list.clicked.connect(QApplication.instance().quit)

        btn_quit = QPushButton('Quit', self)
        btn_quit.clicked.connect(QApplication.instance().quit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(90, 100)

        layout = QVBoxLayout()
        layout.addWidget(btn_list)
        layout.addWidget(btn_quit)

        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle('Shop application Menu')
        self.setLayout(layout)
        self.show()

    def show(self):
        '''is_member = self._common.query_yes_no("Are you already a member ?")
        if is_member:
            return self.connect()
        else:
            return self.subscribe()'''

    def connect(self):
        print("Connection")
        while True:
            username = self._common.ask_name(key_name="username")
            try:
                print(self._store.user().get_all())
                user = self._store.user().get_by_username(username)
                break
            except ResourceNotFound:
                print("/!\\ Customer %s not exists" % username)
        UserViewFactory(user, self._store).show()

    def subscribe(self):
        # Show subscription formular
        customer_builder = CustomerBuilder(self._store)
        print("Store user Subscription")
        print()

        while True:
            # while username found in database, ark username again
            username = self._common.ask_name(key_name="username")
            try:
                self._store.user().get_by_username(username)
                print("/!\\ Customer %s already exists" % username)
            except ResourceNotFound:
                break
        firstname = self._common.ask_name(key_name="firstname")
        lastname = self._common.ask_name(key_name="lastname")
        email = self._common.ask_email()
        user = customer_builder.create_user(username, firstname, lastname, email)
        UserViewFactory(user, self._store).show()
