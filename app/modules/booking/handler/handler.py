from ..config import config
from ..service import service


class Handler:
   def __init__(self, svc : service.Service, cfgs: config.ModuleConfig):
       self.svc = svc
       self.config = cfgs