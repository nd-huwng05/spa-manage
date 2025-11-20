
from flask_migrate import Migrate
from app import srv
from app.modules.user.repository.model.user import User, Staff, UserAuthMethod

app = srv.env.http.get_app()
db = srv.env.http.db
migrate = Migrate(app, db)

__all__ = ["app"]

