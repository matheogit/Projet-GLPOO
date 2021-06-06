from model.dao.admin_dao import AdminDAO
from model.dao.party_dao import PartyDAO
from model.dao.customer_dao import CustomerDAO
from model.dao.command_dao import CommandDAO
from model.dao.user_dao import UserDAO
from model.dao.userParticipation_dao import UserParticipationDAO

class Store:

    def __init__(self, db_session):
        self._db_session = db_session

    def admin(self):
        return AdminDAO(self._db_session)

    def party(self):
        return PartyDAO(self._db_session)

    def customer(self):
        return CustomerDAO(self._db_session)

    def command(self):
        return CommandDAO(self._db_session)

    def user(self):
        return UserDAO(self._db_session)

    def userParticipation(self):
        return UserParticipationDAO(self._db_session)