from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Boolean, Enum, DateTime
from app import db
import enum


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(db.Integer, primary_key=True, autoincrement=True)
    create_at = Column(db.DateTime, default=datetime.now)
    update_at = Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __str__(self):
        return self.name

class RoleAccount(enum.Enum):
    CUSTOMER = "customer"
    STAFF = "staff"
    ADMIN = "admin"

class AuthMethodEnum(enum.Enum):
    GOOGLE = "google"
    EMAIL = "email"
    LOCAL = "local"

class User(BaseModel):
    __tablename__ = 'user'
    username = Column(db.String(150), nullable=True, unique=True)
    password = Column(db.String(150), nullable=True)
    fullname = Column(db.String(50), nullable=True)
    avatar = Column(db.String(150), default="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.iconpacks.net%2Ffree-icon%2Fuser-3296.html&psig=AOvVaw0MB6GuXKx0e4UcyX_oVPrw&ust=1763675778600000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCLC4hLWa_5ADFQAAAAAdAAAAABAE")
    phone = Column(db.String(150), nullable=False)
    email = Column(db.String(150), nullable=False, unique=True)
    role = Column(Enum(RoleAccount), default=RoleAccount.CUSTOMER)

    staff = db.relationship('Staff', backref='user', lazy=True, uselist=False)

class UserAuthMethod(BaseModel):
    __tablename__ = 'user_auth_method'

    user_id = Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    provider = Column(Enum(AuthMethodEnum), nullable=False)
    provider_id = Column(db.String(150), nullable=False)
    last_login_at = Column(db.DateTime, nullable=False)


class Staff(BaseModel):
    __tablename__ = 'staff'
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=True)
    position = Column(String(50), nullable=True)
    hire_date = Column(DateTime, default=datetime.now)
    active = Column(Boolean, default=True)
