
class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class ResourceNotFound(Error):
    pass


class InvalidData(Error):
    pass


class NotEnoughParties(Error):
    pass


class Conflict(Error):
    pass
