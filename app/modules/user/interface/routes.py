from flask import render_template, Blueprint, Flask, redirect
from sqlalchemy.sql.functions import current_user
from .controller import Controller


def register_routes(app:Flask, controller:Controller):
    user_routes = Blueprint('user', __name__, url_prefix='/user', template_folder='../templates')

    public_routes = Blueprint('public', __name__, url_prefix='/')
    private_routes = Blueprint('private', __name__, url_prefix='/')

    @private_routes.before_request
    def before_request():
        if not current_user.is_authenticated:
            return redirect('/login')
        return None

    user_routes.register_blueprint(public_routes)
    user_routes.register_blueprint(private_routes)

    public_routes.add_url_rule('/login', endpoint='login', view_func=controller.login)
    app.register_blueprint(user_routes)

