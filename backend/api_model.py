from pydantic import BaseModel

class UsersModel(BaseModel):
    userId: int
    username: str
    password: str

class MessagesModel(BaseModel):
    messageId: int
    content: str
    userIdSender: int
    userIdReciever: int
    isRead: bool
    messageDate: str