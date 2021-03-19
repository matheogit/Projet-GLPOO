import datetime
from sqlalchemy import Column, String, UniqueConstraint, ForeignKey, Integer, DateTime, Enum
from sqlalchemy.orm import relationship

from model.mapping import Base, generate_id
from model.mapping.command_status_enum import CommandStatusEnum
from model.dao.dao_error_handler import dao_error_handler


class Command(Base):
    __tablename__ = 'command'

    id = Column(String(36), default=generate_id, primary_key=True)

    date = Column(DateTime(), default=datetime.datetime.utcnow, nullable=False)
    status = Column(Enum(CommandStatusEnum), nullable=True)  # TODO: update with Enum
    customer_id = Column(String(36), ForeignKey("customer.id"), nullable=True)

    articles = relationship("CommandItem")

    def __repr__(self):
        return "<Command of %s>" % self.customer.username

    @dao_error_handler
    def add_article(self, article, number):
        item = CommandItem(number=number)
        item.article = article
        self.articles.append(item)


class CommandItem(Base):
    """
    Association class between command and articles
    help relationship: https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html
    """
    __tablename__ = 'command_item'
    __table_args__ = (UniqueConstraint('command_id', 'article_id'),)

    command_id = Column(String(36), ForeignKey(Command.id), primary_key=True)
    article_id = Column(String(36), ForeignKey('article.id'), primary_key=True)
    number = Column(Integer, nullable=False)
    command = relationship("Command", back_populates="articles")
    article = relationship("Article")
