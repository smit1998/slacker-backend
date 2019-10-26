from auth import * 
from json import dumps
from flask import Flask, request

APP = Flask(__name__)

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
    password = request.form.get('password'))
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
    

if __name__ == '__main__':
    APP.run(debug = True, port=4000) 
