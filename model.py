from sqlalchemy import Column, Integer, String, DateTime, Text, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class HINDALCO(Base):
    __tablename__ = 'HINDALCO'
    datetime = Column(DateTime(), primary_key=True)
    close = Column(Float())
    high = Column(Float())
    low = Column(Float())
    open = Column(Float())
    volume = Column(Integer())
    instrument = Column(String(100))