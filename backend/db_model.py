from api_model import UsersModel, MessagesModel
from sqlalchemy import Column,String,Integer,Boolean,ForeignKey
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Users(Base):
    __tablename__ = "Users"

    userId  = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    password = Column(String)
    profilePic = Column(String, default="default.png")

class Messages(Base):
    __tablename__ = "Messages"

    messageId      = Column(Integer, primary_key=True, autoincrement=True)
    content        = Column(String)
    userIdSender   = Column(Integer)
    userIdReceiver = Column(Integer)
    isRead         = Column(Boolean)
    messageDate    = Column(String)
