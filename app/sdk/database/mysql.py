import os
from flask import Flask
from app.sdk.logger import log

class MySQLDB:

    def __init__(self, app:Flask):
        log.info("Initializing MySQL DB")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASS")
        host = os.getenv("DB_HOST", "localhost")
        port = os.getenv("DB_PORT", "3306")
        db_name = os.getenv("DB_NAME")
        db_url = (
            f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}?charset=utf8mb4"
        )
        app.config["SQLALCHEMY_DATABASE_URI"] = db_url
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False







    def get_db(self):
        return self.db