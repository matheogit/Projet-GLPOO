import uuid

from model.mapping import Base
from sqlalchemy import Column, String, Integer,  UniqueConstraint

class Party(Base):
    __tablename__ = 'party'
    __table_args__ = (UniqueConstraint('name', 'location','date'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    name = Column(String(50), nullable=False)
    location = Column(String(50), nullable=False)
    date = Column(String(50), nullable=False)

    creator_id = Column(String(36), nullable=True)
    total_place = Column(Integer, nullable=True) 
    theme = Column(String(256), nullable=True)
    price = Column(Integer, nullable=True)    
    grade = Column(String(256), nullable=True)
    state = Column(String(10), nullable=False)
    note = Column(Integer, nullable=True)

    def __repr__(self):
        return "<Party(%s at %s the %s)>" % (self.name, self.location, self.date)
