from sqlalchemy import Column, Date, Integer, String, Boolean
from .database import Base

# Define Model
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    due_date = Column(Date, nullable=True)

class User(Base):
    __tablename__ = "users"

    id =   Column(Integer, primary_key=True)
    username =  Column(String(50), nullable=False, unique=True)#最多 50 字元，必填且唯一
    password = Column(String(255), nullable=False)#最多 255 字元，必填
    email = Column(String(100), nullable=True, unique=True)#最多 100 字元，必填且唯一