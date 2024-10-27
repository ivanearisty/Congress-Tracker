from fastapi import APIRouter, Depends, HTTPException
from .schemas import UserCreate, UserLogin
from pydantic import BaseModel
import bcrypt
from firebase_admin import auth as firebase_auth

router = APIRouter()

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

#register a new user
@router.post("/register")
async def register(user: UserCreate):
    try:
        # create use in firebase
        firebase_user = firebase_auth.create_user(
            email=user.username,
            password=user.password,
            display_name=user.username
        )
        return {"message": "User registered successfully", "uid": firebase_user.uid}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

#login a user
@router.post("/login")
async def login_user(user: UserLogin):
    try:
        # verify user exists in firebase
        firebase_user = firebase_auth.get_user_by_email(user.username)

        #client side SDKs not implemented yet, so just checking if user exists in firebase for now
        return {"access_token": firebase_user.uid, "token_type": "bearer"}
    except firebase_auth.UserNotFoundError:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))