import os
import signal
from flask import Flask


class HTTP:
    __env : str
    __host : str
    __port : str
    __jwtSecretKey : str
    app : Flask

    def __init__(self):
        self.__host = os.getenv("SERVICE_HOST", "localhost")
        self.__port = os.getenv("PORT", "8080")
        self.__env = os.getenv("ENV", "local")

        self.__jwtSecretKey = os.getenv("JWT_SECRET_KEY")
        if not self.__jwtSecretKey:
            raise EnvironmentError("JWT_SECRET_KEY is required")

        self.app = Flask(__name__)
        self.app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024


    def get_app(self):
        return self.app

    def start(self):
        signal.signal(signal.SIGINT, self.__stop)

        print(f"Starting HTTP server on port {self.__port}...")

        with self.app.app_context():
            self.app.run(host=self.__host, port=int(self.__port))

    def __stop(self, *args):
        print("Gracefully shutting down Flask server...")
        exit(0)