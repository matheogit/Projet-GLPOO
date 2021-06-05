from model.mapping import Base
import uuid


from sqlalchemy import Column, String, Integer, UniqueConstraint

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

    def __repr__(self):
        return "<Party(%s at %s the %s)>" % (self.name, self.location, self.date)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "date": self.date,
            "creator_id": self.creator_id,
            "total_place": self.total_place,
            "theme": self.theme,
            "price": self.price,
            "grade": self.grade,
            "state": self.state
        }
