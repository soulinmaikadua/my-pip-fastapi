# app/routers/item.py
from fastapi import APIRouter
from ..models.item import Item

router = APIRouter()

@router.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}

@router.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_description": item.description}
