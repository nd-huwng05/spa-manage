from flask_sqlalchemy import SQLAlchemy

class Repository:
    db : SQLAlchemy
    def __init__(self, db: SQLAlchemy):
        self.db = db



