from typing import Union
from fastapi import FastAPI
from Backend.auth_module.routes import router as auth_router
import firebase_admin
from firebase_admin import credentials
from dotenv import load_dotenv
import os

# initialize firebase
cred = credentials.Certificate("Backend/config/congress-tracker-ff249-firebase-adminsdk-vcptd-58346d4a48.json")
firebase_admin.initialize_app(cred)

# load environment variables
load_dotenv()
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

app = FastAPI()

#include authentication routes
app.include_router(auth_router, prefix = "/auth_module")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

