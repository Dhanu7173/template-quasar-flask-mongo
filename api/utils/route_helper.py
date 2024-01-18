import flask, time, logging
from datetime import datetime
from werkzeug.exceptions import HTTPException
from functools import wraps

logger = logging.getLogger(__name__)

def exception_handler(error):
    logger.error("%s - ERROR - Exception occured" % str(datetime.utcnow()), exc_info=True)
    res = flask.jsonify(ok=False)
    res.status_code = 500
    if isinstance(error, HTTPException):
        res.status_code = error.code
    return res

def requires_auth(role=None):
    def wrapper(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if '_id' not in flask.session:
                return unauthorized_abort()
            else:
                if role is not None:
                    if isinstance(role, list):
                        flag = 0
                        for each in role:
                            if not flask.session['roles'] or each not in flask.session['roles']:
                                flag = 0
                            else:
                                flag = 1
                                break
                        if flag == 0:
                            return unauthorized_abort()
                    elif role not in flask.session['roles']:
                        return unauthorized_abort()
                return f(*args, **kwargs)

        return decorated

    return wrapper

def unauthorized_abort():
    return flask.abort(401)

