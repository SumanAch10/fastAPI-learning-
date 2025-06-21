from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class create_user(BaseModel):
    user_name:str
    email:str
    password:str
    confirm_password:str
    
class login_user(BaseModel):
    pass
