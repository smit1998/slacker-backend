from backend_functions import * 
from json import dumps
from flask import Flask, request


APP = Flask(__name__)

def defaultHandler(err):
    response = err.get_response()
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.debadscription,
    })
    response.content_type = 'application/json'
    return response

APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)
CORS(APP)

@APP.route('/auth/register', methods=['POST'])
def auth_register_server():
    email = request.form.get('email')
    password = request.form.get('password')
    name_first = request.form.get('name_first')
    name_last = request.form.get('name_last')
    result = user_register(email, password, name_first, name_last)
    return dumps(result)

@APP.route('/auth/login', methods=['POST'])
def auth_login_server():  
    email = request.form.get('email')
    password = request.form.get('password')
    result = user_login(email, password)
    return dumps(result)
    
@APP.route('/auth/logout', methods=['POST'])
def auth_logout_sever():
    token = request.form.get('token')
    result = user_logout(token)
    return dumps(result)
   
@APP.route('/channel/invite', methods=['POST'])
def channel_invite_server():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    u_id = request.form.get('u_id')
    result = channel_invite(token, channel_id, u_id)
    return dumps(result)
    
@APP.route('/channels/create', methods=['POST'])
def channels_create_server():
    token = request.form.get('token')
    name = request.form.get('name')
    is_public = request.form.get('is_public')
    result = channels_create(token, name, is_public)
    return dumps(result)

@APP.route('/channel/details', methods=['GET']) 
def channel_details_server():
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    result = channel_details(token, channel_id)
    return dumps(result)

@APP.route('/user/profile', methods=['GET'])
def user_profile_server():
    token = request.args.get('token')
    u_id = request.args.get('u_id')
    result =  user_profile(token, u_id)
    return dumps(result)
 
@APP.route('/channel/messages', methods=['GET'])
def channel_messages_server():
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    start = request.args.get('start')
    result = channel_messages(token, channel_id, start)
    return dumps(result)
    
@APP.route('/message/send', methods=['POST'])   
def message_send_server():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    result = message_send(token, channel_id, message)
    return dumps(result)

@APP.route('/message/sendlater', methods=['POST'])
def message_sendlater_server():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    time_sent = request.form.get('time_sent')
    result = message_sendlater(token, channel_id, message, time_sent)
    return dumps(result)

@APP.route('/auth/passwordreset/request', methods=['POST'])
def passwordreset_request():
    email = request.form.get('email')
    auth_passwordreset_request(email)
    return dumps({})

@APP.route('/auth/passwordreset/reset', methods=['POST'])
def passwordreset_reset():
    reset_code = request.form.get('reset_code')
    new_password= request.form.get('new_password')
    passwordreset_reset(reset_code, new_password)
    return dumps({})

@APP.route('/channel/leave', methods=['POST'])
def leave_channel():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    return dumps(channel_leave(token, channel_id))
    
@APP.route('/channel/join', methods=['POST'])
def join_channel():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    channel_join(token, channel_id)
    return dumps({})

@APP.route('/channel/addowner', methods=['POST'])
def addowner_channel():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    user_id = request.form.get('u_id')
    addowners(token, channel_id, user_id)
    return dumps({})

@APP.route('/channel/removeowner', methods=['POST'])
def removeowner_channel():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    user_id = request.form.get('u_id')
    removeowners(token, channel_id, user_id)
    return dumps({})

@APP.route('/channels/list', methods=['GET'])
def listChannels():
    token = request.args.get('token')
    return dumps(channellist(token))

@APP.route('/channels/listall', methods=['GET'])
def listallChannels():
    token = request.args.get('token')
    return dumps(channellistall(token))
  
@APP.route('/channels/create', methods=['POST'])
def create():
    token = request.form.get('token')
    name = request.form.get('name')
    is_public = request.form.get('is_public')
    return dumps(channelcreate(token, name, is_public))

@APP.route('/message/remove', methods=['DELETE'])
def removeMessage():
    token = request.args.get('token')
    message_id = request.args.get('message_id')
    message_remove(token, message_id)
    return dumps({})

@APP.route('/message/edit', methods=['PUT'])
def edit():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    message = request.form.get('message')
    message_edit(token, message_id, message)
    return dumps({})

@APP.route('/message/react', methods=['POST'])
def react():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    react_id = request.form.get('react_id')
    message_react(token, message_id, react_id)
    return dumps({})

@APP.route('/message/unreact', methods=['POST'])
def unreact():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    react_id = request.form.get('react_id')
    message_unreact(token, message_id, react_id)
    return dumps({})

@APP.route('/message/pinn', methods=['POST'])
def pin():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    message_pin(token, message_id)
    return dumps({})

@APP.route('/message/unpin', methods=['POST'])
def unpin():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    message_unpin(token, message_id)
    return dumps({})

if __name__ == '__main__':
    APP.run(debug = True, port=5000) 
