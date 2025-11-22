from flask import Blueprint, render_template, send_from_directory

interface = Blueprint('interface', __name__, url_prefix='/', template_folder='../templates',
                      static_folder='../templates/assets', static_url_path='/assets')

@interface.route('/')
def home():
    return render_template("page/index.html")