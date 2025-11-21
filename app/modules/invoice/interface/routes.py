from flask import render_template, Blueprint, Flask, redirect
from sqlalchemy.sql.functions import current_user
from .controller import Controller


def register_routes(app:Flask, controller:Controller):
    invoice_routes = Blueprint('invoice', __name__, url_prefix='/invoice', template_folder='../templates')

    public_routes = Blueprint('public', __name__, url_prefix='/')
    private_routes = Blueprint('private', __name__, url_prefix='/')

    @private_routes.before_request
    def before_request():
        if not current_user.is_authenticated:
            return redirect('/login')
        return None

    invoice_routes.register_blueprint(public_routes)
    invoice_routes.register_blueprint(private_routes)

    # TO DO

    app.register_blueprint(invoice_routes)

