import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from app.sdk.log import log

class MySQLDB:
    _db : SQLAlchemy

    def __init__(self, app:Flask):
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASS")
        host = os.getenv("DB_HOST", "localhost")
        port = os.getenv("DB_PORT", "3306")
        db_name = os.getenv("DB_NAME")
        self.db_url = (
            f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}?charset=utf8mb4"
        )

        app.config["SQLALCHEMY_DATABASE_URI"] = self.db_url
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        self._db = SQLAlchemy(app)

    def get_db(self):
        return self._db