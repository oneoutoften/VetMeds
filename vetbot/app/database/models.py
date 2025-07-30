from app.database.connection import Base
from sqlalchemy import Column, Integer, String, Text

class Drug(Base):
    __tablename__ = 'drugs'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    active_ingredients = Column(Text)
    analogs = Column(Text)
    dosages = Column(Text)
    description = Column(Text)
    notes = Column(Text)