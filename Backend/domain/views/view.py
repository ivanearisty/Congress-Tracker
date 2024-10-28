from typing import Dict
from fastapi import FastAPI, APIRouter, HTTPException
from domain.controllers.follow import FollowController, FollowType

app = FastAPI()
follow_router = APIRouter()


@follow_router.post("/follow")
async def follow(data: Dict[str, int]):
    follower_id = data.get("follower_id")
    followee_id = data.get("followee_id")

    if not follower_id or not followee_id:
        raise HTTPException(status_code=400, detail="Invalid follower or followee ID")

    result, status_code = FollowController.follow(follower_id, followee_id, follow_type=FollowType.BILL)
    return {"message": result}, status_code


@follow_router.post("/unfollow")
async def unfollow(data: Dict[str, int]):
    follower_id = data.get("follower_id")
    followee_id = data.get("followee_id")

    if not follower_id or not followee_id:
        raise HTTPException(status_code=400, detail="Invalid follower or followee ID")

    result, status_code = FollowController.unfollow(follower_id, followee_id, follow_type=FollowType.BILL)
    return {"message": result}, status_code


# 把 follow_router 加入 FastAPI 應用程式
app.include_router(follow_router, prefix="/api")
