from app.modules.user.interface import userRoutes
from flask import render_template

@userRoutes.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("page/login.html")
