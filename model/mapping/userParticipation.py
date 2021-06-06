from model.mapping import Base, generate_id
from sqlalchemy import Column, String, UniqueConstraint

class UserParticipation(Base):
    __tablename__ = 'userparticipation'
    __table_args__ = (UniqueConstraint('user_id', 'party_id'),)

    id = Column(String(36), default=generate_id, primary_key=True)
    user_id = Column(String(36), nullable=False)
    party_id = Column(String(36), nullable=False)
    note = Column(String(1), nullable=False)

    def __repr__(self):
        return "<user(%s %s %s %s)>" % (self.id, self.user_id, self.party_id, self.note)
