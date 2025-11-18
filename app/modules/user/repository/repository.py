from app.sdk import environment, mysql
from app.modules.user.config import config


class UserRepository:
    __env : environment.Environment
    __mySQLDB : mysql.MySQLDB
    __globalConfig : config.UserConfig

    def __init__(self, env:environment.Environment):
        self.__env = env
        self.__db = self.__env.mySQL.get_db()

