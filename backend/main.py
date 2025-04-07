from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from db_model import Base, Users, Messages
from api_model import UsersModel, MessagesModel, BaseModel

import api_model

app = FastAPI()

engine = create_engine("sqlite:///./Arkham_DB.db")
Base.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

#region User Endpoints

#Get User by Username/All
@app.get("/users/")
async def get_users(username: str | None=None, db:Session=Depends(get_db)):
    if not username:
        results = db.query(Users).all()
        return results
    else:
        results = db.query(Users).filter(Users.username == username).one()
        return results

#Get User by userId
@app.get("/users/{userId}")
async def get_users_by_id(userId:int, db:Session=Depends(get_db)):
    results = db.query(Users).filter(Users.userId == userId).first()
    return results

#Create New User
@app.post("/drinks/")
async def create_user(user: UsersModel, db:Session=Depends(get_db)):
    orm_drink = Users(**user.model_dump())
    db.add(orm_drink)
    db.commit()

#Edit User

#Delete User

#endregion

#region Message Endpoints

#Get Message by Title/All

@app.get("/messages/")
async def get_messages(title: str | None=None, db:Session=Depends(get_db)):
    if not title:
        results = db.query(Messages).all()
        return results
    else:
        results = db.query(Messages).filter(Messages.title == title).first()
        return results
    
#Get message by reciever (THis is good for showing only messages meant for the currently active account)
@app.get("/messages/received/{user_id}")
async def get_received_messages(user_id: int, db: Session = Depends(get_db)):
    messages = db.query(Messages).filter(Messages.userIdReciever == user_id).all()
    return messages

#Get Message by messageId
@app.get("/messages/{messageId}")
async def get_messages_by_id(messageId: int | None=None, db:Session=Depends(get_db)):
    results = db.query(Messages).filter(Messages.messageId == messageId).first()
    return results

#Create New Message
@app.post("/messages/")
async def create_message(message: MessagesModel, db:Session=Depends(get_db)):
    orm_message = Messages(**message.model_dump())
    db.add(orm_message)
    db.commit()
#Edit Message

#Delete Message

#endregion