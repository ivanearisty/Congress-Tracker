from typing import Union
from fastapi import FastAPI
from Backend.auth_module.routes import router as auth_router

app = FastAPI()

#include authentication routes
app.include_router(auth_router, prefix = "/auth_module")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

