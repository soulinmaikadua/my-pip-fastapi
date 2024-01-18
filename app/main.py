# app/main.py
from fastapi import FastAPI
from .routers import item, user

app = FastAPI()

# Include routers
app.include_router(item.router)
app.include_router(user.router)
