from flask import Blueprint, jsonify, request, session
from rq import Queue
from worker import redis_conn

# local imports
from utils import requires_auth


q = Queue(connection=redis_conn, name='test-rq-worker')
bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@bp.get('/')
def default():
    if(session.get('user_id',None)):
        user_data = {}
        return jsonify(ok=True, user_data=user_data)
    return jsonify(ok=False)

@bp.post('/logout')
@requires_auth()
def logout():
    if(session.get('_id',None)):
        session.clear()
    return jsonify(ok=True)

@bp.post('/login')
def login():
    return jsonify(ok=True)
