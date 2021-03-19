from model.mapping import Base
import uuid


from sqlalchemy import Column, String, UniqueConstraint


class Member(Base):
    __tablename__ = 'members'
    __table_args__ = (UniqueConstraint('firstname', 'lastname'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)

    email = Column(String(256), nullable=False)
    type = Column(String(10), nullable=False)

    password = Column(String(256), nullable=False)

    gender = Column(String(50), nullable=False)
    age = Column(String(50), nullable=False)

    def __repr__(self):
        return "<Member(%s %s %s)>" % (self.firstname, self.lastname.upper(), self.type, self.email, self.gender, self.age)

    def to_dict(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "type": self.type,
            "password": self.password,
            "gender": self.gender,
            "age": self.age
        }
