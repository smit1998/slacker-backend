from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
from flask_cors import CORS
from json import dumps


def defaultHandler(err):
    response = err.get_response()
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.debadscription,
    })
    response.content_type = 'application/json'
    return response

app = Flask(__name__)
app.config['TRAP_HTTP_EXCEPTIONS'] = True
app.register_error_handler(Exception, defaultHandler)
CORS(app)

class AccessError(HTTPException):
    code = 400
    message = 'No message specified'

