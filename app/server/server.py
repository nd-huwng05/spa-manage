from datetime import datetime
from app.sdk.enviroment import environment
from app.config import config
from flask_cors import CORS
from flask import render_template
from rich.console import Console
from rich.table import Table

class Server:
    env : environment.Environment
    config : config.Config

    def __init__(self):
        self.env = environment.Environment()
        self.config = config.get_global_config()
        self.set_up_middleware()
        self.set_up_health_check()

    def start(self):
        self.__print_all_routes()
        self.env.http.start()

    def set_up_middleware(self):
        app = self.env.http.get_app()

        @app.errorhandler(Exception)
        def handle_exception(e):
            return {"error": str(e)}, 500

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
            view_func=lambda: render_template(
                "index.html",
                status="ok",
                message="Service is healthy",
                timestamp=datetime.now().isoformat()
            ),
            methods=["GET"]
        )

    def __print_all_routes(self):
        console = Console()
        table = Table(title="Registered Routes")

        table.add_column("Methods", style="cyan", no_wrap=True)
        table.add_column("Path", style="green")
        table.add_column("Endpoint", style="magenta")

        for rule in self.env.http.get_app().url_map.iter_rules():
            methods = ",".join(sorted(rule.methods - {"HEAD", "OPTIONS"}))
            table.add_row(methods, rule.rule, rule.endpoint)

        console.print(table)