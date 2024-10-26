from fastapi import APIRouter, Depends, HTTPException
from auth.schemas import UserCreate, UserLogin
from pydantic import BaseModel

router = APIRouter()

#temporary solution no Firebase
fake_users_db = {
    "testuser": {
        "username": "testuser",
        "hashed_password": "fakehashedpassword"
    }
}

#register a new user
@router.post("/register")
async def register(user: UserCreate):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    fake_users_db[user.username] = {
        "username": user.username,
        "hashed_password": user.password
    }
    return {"message": "User registered successfully"}

#login a user
@router.post("/login")
async def login_user(user: UserLogin):
    stored_user = fake_users_db.get(user.username)
    if not stored_user or stored_user["hashed_password"] != user.password:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    #placeholder token
    return {"access_token": user.username, "token_type": "bearer"}