from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Drug(Base):
    __tablename__ = 'drugs'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    active_ingredient = Column(Text)
    analogs = Column(Text)
    dosages = Column(Text)
    description = Column(Text)
    notes = Column(Text)