import os
from flask import Flask
from app.sdk.enviroment.http import http
from app.sdk.db.mysql import mysql
from app.sdk.base import base

class Environment:
    http : http.HTTP
    __env : str
    __serviceName : str
    mySQL : mysql.MySQLDB

    def __init__(self, **kwargs):
        err = base.load_env()
        if err:
            raise err
        self.http = http.HTTP()
        self.__env = os.getenv("ENV")
        self.__serviceName = os.getenv("SERVICE_NAME")
        self.mySQL = mysql.MySQLDB(self.__get_app())

    def __get_app(self) -> Flask:
        return self.http.get_app()