import re
from exceptions import InvalidData


# Interface validation
class Validate:
    """
    Base class used to validate data in objects.
    """

    def validate(self):
        raise NotImplementedError()

    def _validate_name(self, value: str):
        name_pattern = "^[\S-]{1,50}$"
        self._validate_regex(value, name_pattern)

    def _validate_email(self, value):
        email_pattern = "^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
        self._validate_regex(value, email_pattern)

    def _validate_password(self, value):
        password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$"
        self._validate_regex(value, password_pattern)

    def _validate_gender(self, value):
        gender_pattern = "^[M|W]$"
        self._validate_regex(value, gender_pattern)

    def _validate_age(self, value):
        age_pattern = "^[0-9]{1,3}$"
        self._validate_regex(value, age_pattern)

    def _validate_regex(self, value: str, regex: str):
        pattern = re.compile(regex)
        if isinstance(value, str) and not re.match(pattern, value):
            raise InvalidData("Invalid value: %s" % value)
