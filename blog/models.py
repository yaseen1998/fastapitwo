from database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    