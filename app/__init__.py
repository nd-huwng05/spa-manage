from app.server import server
from flask_migrate import Migrate

srv = server.Server()
app = srv.env.http.get_app()
db = srv.env.http.get_db()
migrate = Migrate(app, db)
__all__ = ["app"]