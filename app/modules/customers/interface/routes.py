from flask import render_template, Blueprint, Flask, redirect
from sqlalchemy.sql.functions import current_user
from .controller import Controller


def register_routes(app:Flask, controller:Controller):
    customer_routes = Blueprint('customer', __name__, url_prefix='/customer', template_folder='../templates')

    public_routes = Blueprint('public', __name__, url_prefix='/')
    private_routes = Blueprint('private', __name__, url_prefix='/')

    @private_routes.before_request
    def before_request():
        if not current_user.is_authenticated:
            return redirect('/login')
        return None

    customer_routes.register_blueprint(public_routes)
    customer_routes.register_blueprint(private_routes)

    app.register_blueprint(customer_routes)

