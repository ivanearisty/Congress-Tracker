from fastapi import APIRouter, Depends, HTTPException, Header
from .schemas import UserCreate, UserLogin
import bcrypt
from firebase_admin import auth as firebase_auth
from Backend.config.config import FIREBASE_API_KEY, JWT_SECRET_KEY
import jwt
import datetime
import httpx

router = APIRouter()

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def verify_jwt_token(authorization: str = Header(...)):
    try:
        # remove bearer prefix if exists
        token = authorization.split(" ")[1] if " " in authorization else authorization
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
        return payload["user_id"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

#protected endpoint with JWT
@router.get("/protected")
async def protected_route(user_id: str = Depends(verify_jwt_token)):
    return {"message": f"Welcome, user {user_id}"}

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
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}",
                json={
                    "email": user.username,
                    "password": user.password,
                    "returnSecureToken": True
                }
            )
        #check for errors
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail = "Invalid username or password")

        #decode response to get user's idToken
        data = response.json()
        id_token = data.get("idToken")

        # create payload for JWT
        payload = {
            "user_id": data.get("localId"), #firebase user ID
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }

        # encode JWT
        token = jwt.encode(payload, JWT_SECRET_KEY, algorithm="HS256")


        return {"access_token": token, "token_type": "bearer", "id_token": id_token}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))