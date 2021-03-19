
from model.mapping.user import User
from controller.validation.validate import Validate


class UserValidation(Validate):
    """
    Check user fields are correct
    """

    def __init__(self, user: User):
        self._user = user

    def validate(self):
        self._validate_name(self._user.username)
        self._validate_name(self._user.firstname)
        self._validate_name(self._user.lastname)
        self._validate_email(self._user.email)
