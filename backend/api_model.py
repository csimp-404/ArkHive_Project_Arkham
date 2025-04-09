from pydantic import BaseModel
from typing import Optional


class UsersModel(BaseModel):
    userId: int
    username: str
    password: str

class MessagesModel(BaseModel):
    messageId: Optional[int] = None
    content: str
    userIdSender: int
    userIdReceiver: int
    isRead: bool
    messageDate: str