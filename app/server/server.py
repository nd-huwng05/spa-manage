from datetime import datetime
from app.modules.user import module as user_module
from app.sdk.environment import environment
from app.config import config
from flask_cors import CORS
from flask import jsonify
from app.router import router as home
from rich.console import Console
from rich.table import Table

class Server:
    env : environment.Environment
    config : config.Config

    def __init__(self):
        self.env = environment.Environment()
        self.env.init()
        self.config = config.get_global_config()
        self.set_up_middleware()
        self.set_up_health_check()
        self.env.http.get_app().register_blueprint(home.interface)
        self.user_module = user_module.UserModule(self.env, self.config)

    def start(self):
        self.__print_all_routes()
        self.env.http.start()

    def set_up_middleware(self):
        app = self.env.http.get_app()

        CORS(app, resources={r"/*": {
            "origins": "*",
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Origin", "Content-Type", "Accept", "Authorization"],
            "supports_credentials": False,
        }})

    def set_up_health_check(self):
        app = self.env.http.get_app()
        app.add_url_rule(
            "/health",
            view_func=lambda: jsonify({
                "status": "ok",
                "message": "Service is healthy",
                "timestamp": datetime.now().isoformat()
            }),
            methods=["GET"]
        )

    def __print_all_routes(self):
        console = Console()
        table = Table(title="SPA BEAUTIFULLY ROUTES")

        table.add_column("Methods", style="cyan", no_wrap=True)
        table.add_column("Path", style="green")
        table.add_column("Endpoint", style="magenta")

        for rule in self.env.http.get_app().url_map.iter_rules():
            methods = ",".join(sorted(rule.methods - {"HEAD", "OPTIONS"}))
            table.add_row(methods, rule.rule, rule.endpoint)

        console.print(table)