import os
import signal
from flask import Flask
from sqlalchemy.sql.expression import text
from flask_sqlalchemy import SQLAlchemy

from app.sdk.database.mysql import MySQLDB
from app.sdk.logger import log


class HTTP:
    env : str
    host : str
    port : str
    jwtSecretKey : str
    app : Flask
    db : SQLAlchemy

    def __init__(self):
        self.host = os.getenv("SERVICE_HOST", "localhost")
        self.port = os.getenv("PORT", "8080")
        self.env = os.getenv("ENV", "local")

        self.jwtSecretKey = os.getenv("JWT_SECRET_KEY")
        if not self.jwtSecretKey:
            raise EnvironmentError("JWT_SECRET_KEY is required")

        self.app = Flask(__name__)
        MySQLDB(self.app)
        self.db = SQLAlchemy(self.app)
        self.app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

        with self.app.app_context():
            self.test_connection()


    def get_app(self):
        return self.app

    def get_db(self):
        return self.db

    def start(self):
        signal.signal(signal.SIGINT, self.stop)

        log.info(f"Starting HTTP server on port {self.port}...")

        with self.app.app_context():
            self.app.run(host=self.host, port=int(self.port))

    def stop(self, *args):
        log.info("Gracefully shutting down Flask server...")
        exit(0)

    def test_connection(self):
        try:
            with self.db.engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            log.info("MySQL DB connection OK")
        except Exception as e:
            log.errorf("MySQL connection failed", e)