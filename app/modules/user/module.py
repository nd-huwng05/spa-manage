from app.modules.user.interface.router import userRoutes
from app.modules.user.service import service
from app.sdk import environment, config
from app.modules.user.repository import repository

class UserModule:
    __env : environment.Environment
    __globalConfig : config.Config
    __serviceUser : service.ServiceUser
    def __init__(self, globalConfig:config.Config, env:environment.Environment):
        self.__globalConfig = globalConfig
        self.__env = env
        self.__env.http.get_app().register_blueprint(userRoutes)



