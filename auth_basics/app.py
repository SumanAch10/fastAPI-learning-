from fastapi import FastAPI,HTTPException,status
from user import create_user as Create_user,login_user as signIn_user
from typing import Optional

create_user = []
login_user = []

app = FastAPI()

@app.get("/")
def home_page():
    return {"Key":"Welcome to the homepage"}

@app.post("/create_user",status_code = status.HTTP_201_CREATED)
def register_user(user:Create_user):
    if user.password != user.confirm_password:
        raise HTTPException(status_code=400,detail="password donot match")
    
    for u in create_user:
        if u["email"] == user.email:
            raise HTTPException(status_code = 400,detail="email already exists")
    
    create_user.append(user.dict())
    return{"message":"user registered succesfully","user":f"{create_user}"}
    
@app.post("/login_user",status_code = status.HTTP_200_CREATED)
def signIn_user(user:signIn_user):
    for u in create_user:
        if u["email"] == user.email and u["password"] == user.password:
            return{"user":"Logged in succesfully"}
    raise HTTPException(status_code = 400,detail="user doesn't exist")

@app.get("/get_user",status_code = status.HTTP_201_CREATED)
def get_user():
    return create_user               