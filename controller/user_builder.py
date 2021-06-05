from model.mapping.user import User
from model.store import Store
from controller.validation.user_validation import UserValidation


class UserBuilder:
    """
    user create
    """

    def __init__(self, store: Store):
        self._store = store

    def create_user(self, username: str, firstname: str, lastname: str, email: str, password: str, gender: str, age: str):

        # Save user in database
        user = User(username=username,
                            firstname=firstname,
                            lastname=lastname,
                            email=email,
                            password=password,
                            gender=gender,
                            age=age)
        UserValidation(user).validate()
        self._store.user().create(user)
        return user
