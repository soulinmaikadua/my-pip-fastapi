# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "postgres://tkaeaswb:XHTYs5BSzLXESRRScK5fArMk2RNFJau-@john.db.elephantsql.com/tkaeaswb"

engine = create_engine("postgres://tkaeaswb:XHTYs5BSzLXESRRScK5fArMk2RNFJau-@john.db.elephantsql.com/tkaeaswb")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
