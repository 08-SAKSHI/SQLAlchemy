from datetime import datetime
import email
from email.mime import base
from email.policy import default
from enum import unique
import os
from click import echo
from requests import Session
import sqlalchemy 
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,Integer, String, DateTime,INTEGER,create_engine

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///"+os.path.join(BASE_DIR,'site.db')

Base = declarative_base()

engine= create_engine(connection_string, echo=True)

Session = sessionmaker()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(),primary_key= True)
    username= Column(String(25),nullable = False,unique=True)
    email= Column(String(80),nullable = False,unique=True)
    date_created =Column(DateTime(),default=datetime.utcnow)        
    
    def __repr__(self):
        return f"<User username = {self.username} email={self.email}"


new_user = User(id=1, username ="sakshi ",email="sakshi.@01")
print(new_user)