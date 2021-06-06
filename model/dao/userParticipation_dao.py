from sqlalchemy import func
from model.dao.dao_error_handler import dao_error_handler
from model.mapping.userParticipation import UserParticipation
from model.dao.dao import DAO
from exceptions import ResourceNotFound

class UserParticipationDAO(DAO):
    """
    UserParticipation Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    @dao_error_handler
    def get(self, id):
        return self._database_session.query(UserParticipation).filter_by(id=id).one()

    @dao_error_handler
    def get_all(self):
        return self._database_session.query(UserParticipation).order_by(UserParticipation.party_id).all()

    @dao_error_handler
    def get_users_by_party_id(self, party_id: str):
        users = self._database_session.query(UserParticipation).filter(UserParticipation.party_id == party_id).order_by(UserParticipation.user_id).all()
        if users is None:
            raise ResourceNotFound()
        return users

    @dao_error_handler
    def get_parties_by_user_id(self, user_id: str):
        parties = self._database_session.query(UserParticipation).filter(UserParticipation.user_id == user_id).order_by(UserParticipation.party_id).all()
        if parties is None:
            raise ResourceNotFound()
        return parties