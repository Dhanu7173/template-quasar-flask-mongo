from flask import Blueprint

main_bp = Blueprint('views',__name__)

from views.auth import bp as bp_auth

main_bp.register_blueprint(bp_auth, url_prefix='/api/auth')