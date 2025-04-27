#region Imports
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from db_model import Base, Users, Messages
from api_model import UsersModel, MessagesModel, BaseModel

import bcrypt
import api_model
#endregion

#region FastAPI APP Setup
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or ["http://localhost:5000"] if you want to be specific
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#endregion

#region DB Connection
engine = create_engine("sqlite:///./Arkham_DB.db")
Base.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
#endregion

#region Bcrypt Setup
passSalt = bcrypt.gensalt()
def passencrypt (username: str, password: str):
    s = 1
def passcompare (username: str, password: str):
    isUser = get_users(username=username)

    if isUser == username:
        isUser
        bcrypt.checkpw

#endregion

#region Login Endpoints
@app.post("/login")
def login_user(username: str, password: str, db:Session=Depends(get_db)):

    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return {"success": False, "message": "Invalid username or password"}

    if bcrypt.checkpw(password.encode(), user.hashed_password.encode()):
        return {"success": True, "message": "Login successful", "user_id": user.id}
    return {"success": False, "message": "Invalid username or password"}

#endregion
#region User Endpoints

#Get All Users
@app.get("/users/")
async def get_users(db:Session=Depends(get_db)):

    results = db.query(Users).all()
    return results
    
#Get User by Username
@app.get("/users/{username}")
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
@app.post("/users/")
async def create_user(user: UsersModel, db:Session=Depends(get_db)):
    orm_user = Users(**user.model_dump())
    db.add(orm_user)
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
    messages = db.query(Messages).filter(Messages.userIdReceiver == user_id).all()
    return messages

#Get message by sender (To get the list of messages you sent)
@app.get("/messages/sent/{user_id}")
async def get_sent_messages(user_id: int, db: Session= Depends(get_db)):
    messages = db.query(Messages).filter(Messages.userIdSender == user_id).all()
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