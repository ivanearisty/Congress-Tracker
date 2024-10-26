from fastapi import APIRouter, Depends, HTTPException
from .schemas import UserCreate, UserLogin
from pydantic import BaseModel
import bcrypt

router = APIRouter()

#temporary solution no Firebase
fake_users_db = {
    "testuser": {
        "username": "testuser",
        "hashed_password": bcrypt.hashpw("password123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    }
}

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

#register a new user
@router.post("/register")
async def register(user: UserCreate):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_pw = hash_password(user.password)
    fake_users_db[user.username] = {
        "username": user.username,
        "hashed_password": hashed_pw
    }
    return {"message": "User registered successfully"}

#login a user
@router.post("/login")
async def login_user(user: UserLogin):
    stored_user = fake_users_db.get(user.username)
    if not stored_user or not verify_password(user.password, stored_user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    #placeholder token
    return {"access_token": user.username, "token_type": "bearer"}