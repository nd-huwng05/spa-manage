from app.modules.user.repository.repository import UserRepository
from app.sdk import environment
from app.modules.user.config import config

class ServiceUser:
    __config: config.UserConfig
    __env : environment.Environment
    __UserRepo : UserRepository

    def __init__(self, env:environment.Environment, config:config.UserConfig):
        self.__env = env
        self.__config = config
        self.__UserRepo = UserRepository(self.__env)

