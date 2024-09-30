from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import  Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI


SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"
 

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


class Base(DeclarativeBase): pass


class Articles(Base):
    __tablename__ = "articles"
 
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text,)
    category = Column(String)
    



SessionLocal = sessionmaker(autoflush=False, bind=engine)