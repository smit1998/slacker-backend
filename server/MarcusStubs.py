from json import dumps
from flask import Flask, request
import re
#import jwt 
from werkzeug.exceptions import HTTPException
import copy 
import hashlib
import dateutil 
from flask_cors import CORS
#from dummy_error import AccessError
from datetime import timezone
import random 
import string

app = Flask(__name__) 

SECRET = 'comp1531 project'

data = {
    'user_info': [],
    'channels': [],
    'message_info': []
}

ch_id = 0

def defaultHandler(err):
    response = err.get_response()
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.description,
    })
    response.content_type = 'application/json'
    return response

APP = Flask(__name__)
APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)
CORS(APP)

def generateChannel_id():
    global ch_id
    ch_id += 1
    channel_id = channel_id
    return channel_id

def generateToken(u_id):
    global SECRET
    encoded = jwt.encode({'u_id': u_id}, SECRET, algorithm='HS256')
    return encoded.decode('utf-8')

def getData():
    global data
    return data

def channels_list(token):
    data = getData()
    input_token = generateToken(token)
    list_channels = {}
    for channel in data['channels']:
        for user in channel['all_members']:
            if (user == input_token):
                list_channels.append(channel)
    return list_channels

def channels_listall(token):
    data = getData()
    input_token = generateToken(token))
    list_all_channels = {}
    for channel in data['channels']:
        list_all_channels.append(channel)
    return list_all_channels

def channels_create(token, name, is_public):
    data = getData()
    input_token = generateToken(token)
    channel_name = name
    if (len(channel_name) > 20):
        raise ValueError(description = "invalid channel name")
    basic_info = getUserFromToken(inputToken)
    owner = {}
    admin = {}
    all_users = {}
    owner['u_id'] = basic_info['u_id']
    owner['name_first'] = basic_info['name_first']
    owner['name_last'] = basic_info['name_last']
    admin['u_id'] = basic_info['u_id']
    admin['name_first'] = basic_info['name_first']
    admin['name_last'] = basic_info['name_last']
    all_users['u_id'] = basic_info['u_id']
    all_users['name_first'] = basic_info['name_first']
    all_users['name_last'] = basic_info['name_last']
    data['channels'].append({
        'channel_id': generateChannel_id(),
        'owner_members': [owner],
        'admin_members': [admin],
        'all_members': [all_users],
        'name': channel_name,
        'is_public': is_public
    })
    return {
        'channel_id': data['channels'][-1]['channel_id']
    }

def message_remove(token, message_id):
    data = getData()
    input_token = token
    input_message_id = message_id
    flag_1 = False # Checks for permission to pin.
    for channel in data['channels']:
        for user in channel['owner_members']:
            if (user == input_token):
                flag_1 = True
        for user in channel['admin_members']:
            if (user == input_token):
                flag_1 = True
    if (flag_1 = False):
        raise AccessError('user is not admin or owner')
    flag_2 = False
    for message in data['message_info']:
        if (message['message_id'] == input_message_id):
            if (message['sender'] != input_token):
                raise AccessError('user is not sender')
            flag_2 = True
            del message
    if (flag_2 == False):
        raise ValueError('message does not exist')
    return ({})

def message_edit(token, message_id, message):
    data = getData()
    input_token = generateToken(token)
    input_message_id = message_id
    input_message = message
    flag_1 = False # Checks for permission to unpin.
    for channel in data['channels']:
        for user in channel['owner_members']:
            if (user == input_token):
                flag_1 = True
        for user in channel['admin_members']:
            if (user == input_token):
                flag_1 = True
    if (flag_1 = False):
        raise ValueError('user is not admin or owner')
    for i in data['message_info']:
        if (i['message_id'] == input_message_id):
            if (i['sender'] != input_token):
                raise AccessError('user did not send the message')
            i['message'] = input_message
    return ({})

def message_react(token, message_id, react_id):
    data = getData()
    input_token = generateToken(token)
    input_message_id = message_id
    input_react_id = react_id
    if (input_react_id != 1):
        raise ValueError('invalid react')
    flag_1 = False
    for message in data['message_info']:
        if (message['message_id'] == input_message_id):
            if (message['react_id'] == input_react_id):
                raise ValueError('message already has an active react')
            flag_1 = True
            message['react_id'] == input_react_id
    if (flag_1 == False):
        raise ValueError('message does not exist')
    return ({})

def message_unreact(token, message_id, react_id):
    data = getData()
    input_token = generateToken(token)
    input_message_id = message_id
    input_react_id = react_id
    if (input_react_id != 0):
        raise ValueError('invalid react')
    flag_1 = False
    for message in data['message_info']:
        if (message['message_id'] == input_message_id):
            if (message['react_id'] == input_react_id):
                raise ValueError('message does not contain an active react')
            flag_1 = True
            message['react_id'] == input_react_id
    if (flag_1 == False):
        raise ValueError('message does not exist')
    return ({})

def message_pin(token, message_id):
    data = getData()
    input_token = generateToken(token)
    flag_1 = False # Checks for permission to pin.
    for channel in data['channels']:
        for user in channel['owner_members']:
            if (user == input_token):
                flag_1 = True
        for user in channel['admin_members']:
            if (user == input_token):
                flag_1 = True
    if (flag_1 = False):
        raise ValueError('user is not admin or owner')
    input_message_id = message_id
    flag_2 = False # Checks if message exists.
    flag_3 = False # Checks if the user is a member of the channel that the message is within.
    for message in data['message_info']:
        if (message['message_id'] == input_message_id):
            for channel in data['channels']:
                if (channel['channel_id'] == message['channel_id']):
                    for user in channel['all_members']:
                        if (user == input_token):
                            flag_3 = True
            if (flag_3 == False):
                raise AccessError('user is not a member of the channel that the message is within')
            if (message['is_pinned'] == True):
                raise ValueError('message already pinned')
            flag_2 = True
            message['is_pinned'] == True
    if (flag_2 == False):
        raise ValueError('message does not exist')
    return ({})

def message_unpin(token, message_id):
    data = getData()
    input_token = generateToken(token)
    flag_1 = False # Checks for permission to unpin.
    for channel in data['channels']:
        for user in channel['owner_members']:
            if (user == input_token):
                flag_1 = True
        for user in channel['admin_members']:
            if (user == input_token):
                flag_1 = True
    if (flag_1 == False):
        raise ValueError('user is not admin or owner')
    input_message_id = message_id
    flag_2 = False # Checks if message exists.
    flag_3 = False # Checks if the user is a member of the channel that the message is within.
    for message in data['message_info']:
        if (message['message_id'] == input_message_id):
            for channel in data['channels']:
                if (channel['channel_id'] == message['channel_id']):
                    for user in channel['all_members']:
                        if (user == input_token):
                            flag_3 = True
            if (flag_3 == False):
                raise AccessError('user is not a member of the channel that the message is within')
            if (message['is_pinned'] == False):
                raise ValueError('message already unpinned')
            flag_2 = True
            message['is_pinned'] == False
    if (flag_2 == False):
        raise ValueError('message does not exist')
    return ({})

if __name__ == '__main__':
    APP.run(debug = True, port=4002)