# main.py

from fastapi import FastAPI
from uvicorn import run
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}

if __name__ == "__main__":
    run(app, host="127.0.0.1", port=8001, reload=True)