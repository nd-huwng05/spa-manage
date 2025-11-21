import os
from flask import Flask
from .http import http
from ..jwt import jwt
from ..base import base

class Environment:
    http : http.HTTP
    env : str
    serviceName : str
    jwt : jwt.JWTConfig

    def __init__(self,  **kwargs):
        err = base.load_env()
        if err:
            raise err
        self.serviceName = os.getenv("SERVICE_NAME")

    def init(self, **kwargs):
        self.http = http.HTTP()
        self.env = os.getenv("ENV")
        self.jwt = jwt.JWTConfig(self.__get_app())

    def __get_app(self) -> Flask:
        return self.http.get_app()