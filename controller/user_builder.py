from model.mapping.user import User
from model.store import Store
from controller.validation.user_validation import UserValidation

class UserBuilder:
    """
    user create
    """

    def __init__(self, store: Store):
        self._store = store

    def create_user(self, id: str, username: str, firstname: str, lastname: str, email: str, password: str, gender: str, age: str):
        
        # Save user in database
        user = User(id=id,
                    username=username,
                    firstname=firstname,
                    lastname=lastname,
                    email=email,
                    password=password,
                    gender=gender,
                    age=age)
        UserValidation(user).validate()
        if user.id is None:
            self._store.party().create(user)
        else:
            self._store.party().update(user)
        return user
    
        self._store.user().create(user)
        return user

    def get_user_by_username(self, username: str):
        user = self._store.user().get_by_username(username)
        return user

    def get_all_user(self):
        users = self._store.user().get_all()
        return users

    def get_user(self, id):
        user = self._store.user().get(id)
        return user
