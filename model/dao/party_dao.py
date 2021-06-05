from model.dao.dao_error_handler import dao_error_handler

from sqlalchemy import or_
from model.mapping.party import Party
from model.dao.dao import DAO


class PartyDAO(DAO):
    """
    User Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    @dao_error_handler
    def get(self, id):
        return self._database_session.query(Party).filter_by(id=id).one()

    @dao_error_handler
    def get_by_name(self, name):
        return self._database_session.query(Party).filter_by(name=name).one()

    @dao_error_handler
    def get_all(self):
        return self._database_session.query(Party).order_by(Party.name).all()

    @dao_error_handler
    def search(self, string: str):
        return self._database_session.query(Party)\
            .filter(or_(Party.name.ilike("{}%".format(string)),
                        Party.description.ilike("{}%".format(string))))\
            .order_by(Party.name).all()
