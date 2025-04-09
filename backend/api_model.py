from pydantic import BaseModel

class UsersModel(BaseModel):
    userId: int
    username: str
    password: str

class MessagesModel(BaseModel):
    messageId: int
    content: str
    userIdSender: int
    userIdReceiver: int
    isRead: bool
    messageDate: str