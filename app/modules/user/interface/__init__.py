from flask import Blueprint

userRoutes = Blueprint('user', __name__, url_prefix='/user', template_folder='../templates')
