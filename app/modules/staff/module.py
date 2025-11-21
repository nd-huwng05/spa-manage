from .handler import handler
from .interface import controller
from .interface.routes import register_routes
from .repository import repository
from .service import service
from ...sdk.environment import environment
from ...sdk.config import config as base_config
from .config import config as module_config
from .interface import routes


class StaffModule:
    env : environment.Environment
    config : module_config.ModuleConfig

    def __init__(self, env:environment.Environment, global_config: base_config.Config):
        self.config = module_config.ModuleConfig()
        self.config.global_config = global_config
        self.env = env
        staff_repo = repository.Repository(self.env.http.db)
        staff_service = service.Service(repo=staff_repo)
        staff_handler = handler.Handler(svc=staff_service, cfgs=self.config)
        self.staff_controller = controller.Controller(h=staff_handler, cfgs=self.config)
        self.register_route()


    def register_route(self):
        return routes.register_routes(self.env.http.get_app(), self.staff_controller)




