from model.store import Store
from controller.user_builder import UserBuilder
from view.common import Common
from view.view import View
from exceptions import ResourceNotFound
from view.user_view_factory import UserViewFactory

class MainView(View):

    def __init__(self):
        super().__init__()
        self.listUserWindow = None
        self.setup()
    
    def __init__(self, store: Store):
        self._store = store
        self._common = Common()

    def show(self):
        is_member = self._common.query_yes_no("Are you already a member ?")
        if is_member:
            return self.connect()
        else:
            return self.subscribe()

    def connect(self):
        print("Connection")
        user_builder = UserBuilder(self._store)
        while True:
            username = self._common.ask_name(key_name="username")
            try:
                user = user_builder.get_user_by_username(username)
                break
            except ResourceNotFound:
                print("/!\\ User %s not exists" % username)
        UserViewFactory(user, self._store).show()

    def subscribe(self):
        # Show subscription formular
        user_builder = UserBuilder(self._store)
        print("Store user Subscription")

        while True:
            # while username found in database, ark username again
            username = self._common.ask_name(key_name="username")
            try:
                self._store.user().get_by_username(username)
                print("/!\\ User %s already exists" % username)
            except ResourceNotFound:
                break
        firstname = self._common.ask_name(key_name="firstname")
        lastname = self._common.ask_name(key_name="lastname")
        email = self._common.ask_email()
        password = self._common.ask_password()
        gender = self._common.ask_gender()
        age = self._common.ask_age()
        user = user_builder.create_user(username, firstname, lastname, email, password, gender, age)
        UserViewFactory(user, self._store).show()
