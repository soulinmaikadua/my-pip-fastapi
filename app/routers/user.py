# app/routers/user.py
from fastapi import APIRouter
from ..models.user import User

router = APIRouter()

@router.get("/users/{user_id}")
def read_user(user_id: int, query_param: str = None):
    return {"user_id": user_id, "query_param": query_param}

@router.post("/users/")
def create_user(user: User):
    return {"user_name": user.username, "email": user.email}
