from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')

@auth_blueprint.route('/auth/')
def auth():
    return "authentication success"
