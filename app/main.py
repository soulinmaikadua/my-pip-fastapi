# app/main.py
from fastapi import FastAPI
from .routers import user
from .database import engine

app = FastAPI()

# Include routers
# app.include_router(item.router)
app.include_router(user.router)


# Create tables in the database
from .models.user import Base
Base.metadata.create_all(bind=engine)