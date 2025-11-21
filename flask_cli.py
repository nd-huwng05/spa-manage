
from flask_migrate import Migrate
from app import app, db
from app.modules.user.repository.model import *

migrate = Migrate(app, db)
