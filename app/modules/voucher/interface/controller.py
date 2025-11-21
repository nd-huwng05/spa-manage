from ..handler import handler
from ..config import config
from flask import render_template

class Controller:
    def __init__(self, h:handler.Handler, cfgs: config.ModuleConfig):
        self.handler = h
        self.cfgs = cfgs

    def login(self):
        return render_template('page/login.html')
