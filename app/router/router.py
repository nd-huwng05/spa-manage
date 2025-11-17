from flask import Blueprint, render_template

interface = Blueprint('interface', __name__, url_prefix='/', template_folder='../templates')

@interface.route('/')
def home():
    return render_template("page/index.html")