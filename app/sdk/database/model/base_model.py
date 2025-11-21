from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Boolean, Enum, DateTime
from app import db

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)