from flask import Flask, request
import re
import jwt 
from werkzeug.exceptions import HTTPException
import copy 
import hashlib
import dateutil 
from flask_cors import CORS
from datetime import timezone
from datetime import datetime


SECRET = 'comp1531 project'
 
data = {
    'user_info': [],
    'channel_info': [],
    'message_info': []
}

messages_list = []
user_id = 0
channel_id = 0
message_id = 0
react_id = 0

def defaultHandler(err):
    response = err.get_response()
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.debadscription,
    })
    response.content_type = 'application/json'
    return response

APP = Flask(__name__)
APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)
CORS(APP)

class ValueError(HTTPException):
    code = 400
    message = 'No message specified'

class AccessError(HTTPException):
    code = 400 
    message = 'No message specified'

def generateReact_id(r_id):
    global react_id 
    react_id = react_id + 1
    r_id = react_id 
    return r_id
    
def generateMessage_id(m_id):
    global message_id 
    message_id = message_id + 1
    m_id = message_id
    return m_id     
       
def generateU_id(u_id):
    global user_id
    user_id = user_id + 1
    u_id = user_id
    return u_id 

def resetUser_id(u_id):
    global user_id
    u_id = 0 
    user_id = u_id

def resetChannel_id(c_id):
    global channel_id 
    c_id = 0
    channel_id = c_id 

def resetMessage_id(m_id):
    global message_id
    m_id = 0
    message_id = m_id
    
def getData():
    global data
    return data
    
def generateChannel_id(c_id):
    global channel_id
    channel_id = channel_id + 1
    c_id = channel_id
    return c_id
    
# transform this token from bytes into string
def generateToken(name_first):
    global SECRET
    encoded = jwt.encode({'name_first': name_first}, SECRET, algorithm='HS256')
    return encoded.decode('utf-8') # asdfasdfadsf

# return a dictionary 
def getUserFromToken(token):
    global SECRET
    decoded = jwt.decode(token, SECRET, algorithms=['HS256'])
    return findUser(decoded['name_first'])

def hashPassword(password):
    return hashlib.sha256(password.encode()).hexdigest()

def findUser(inputName):
    for u in data['user_info']:
        if u['name_first'] == inputName:
            return u
    return None
    
def user_register(email, password, name_first, name_last):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    data = getData()
    if(not re.search(regex, email)):
        raise ValueError(description = "invalid email")
    if(len(password) < 6):
        raise ValueError(description = "invalid password")
    if(len(name_first) < 1 or len(name_first) > 50):
        raise ValueError(description = "invalid name_first")
    if(len(name_last) < 1 or len(name_last) > 50):
        raise ValueError(description = "invalid name_last")
    flag = False
    for i in data['user_info']:
        if(i['email'] == email):
            flag = True
    if(flag == True):
        raise ValueError(description = 'email address is already been used')
    data['user_info'].append({
        'email': email,
        'password': hashPassword(password),
        'name_first': name_first,
        'name_last': name_last,
        'u_id': generateU_id(user_id),
        'token': generateToken(name_first),
        'handle_str': 'TEAM WORK'
    })
    return {
        'token': generateToken(name_first),
        'u_id': data['user_info'][-1]['u_id']
    }


def user_login(email, password):
    data = getData()
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(not re.search(regex, email)):
        raise ValueError(description = "invalid email")
    flag_1 = False 
    flag_2 = False
    for user in data['user_info']:
        if(user['email'] == email): 
            flag_1 = True
        if(hashPassword(password) == user['password']):
            flag_2 = True
        if(flag_2 == True and flag_1 == True):
            newToken = generateToken(user['name_first'])
            user['token'] = newToken
            return {
                'token': newToken,
                'u_id': user['u_id']
            }
    if(flag_1 == False):
        raise ValueError(description = "email entered is not belong to user")
    if(flag_2 == False):
        raise ValueError(description = "password is not correct")


def user_logout(token):
    data = getData()
    user = getUserFromToken(token)
    print(user)
    if user['name_first'] is not None:
        del user['token']
        return {
            'is_success': True
        }
    return {
        'is_success': False
    }
    

def channel_invite(token, channel_id, u_id):
    data = getData()
    basic_info = getUserFromToken(token)
    channel_id_integer = int(channel_id)
    u_id_integer = int(u_id)
    flag_1 = False
    # u_id is invalid
    for user in data['user_info']:
        if(u_id_integer == user['u_id']):
            flag_1 = True
    if(flag_1 == False):
        raise ValueError(description = "u_id we want to invite is invalid")
    # consider the channel_id ValueError
    for channel in data['channel_info']:
        if(channel_id_integer == channel['channel_id']):
            for user in data['user_info']:
                if(user['u_id'] == u_id_integer):
                    # invite this user into this channel
                    all_users = {}
                    all_users['u_id'] = u_id_integer
                    all_users['name_first'] = user['name_first']
                    all_users['name_last'] = user['name_last']
                    channel['all_members'].append(all_users)
                    return {}
    raise ValueError(description = "channel_id is invalid")
    
   
def channels_create(token, name, is_public):
    data = getData()
    if (len(name) > 20):
        raise ValueError(description = "invalid channel name")
    basic_info = getUserFromToken(token)
    owner = {}
    all_users = {}
    owner['u_id'] = basic_info['u_id']
    owner['name_first'] = basic_info['name_first']
    owner['name_last'] = basic_info['name_last']
    all_users['u_id'] = basic_info['u_id']
    all_users['name_first'] = basic_info['name_first']
    all_users['name_last'] = basic_info['name_last']
    data['channel_info'].append({
        'channel_id': generateChannel_id(channel_id),
        'owner_members': [owner],
        'all_members': [all_users],
        'name': name,
        'is_public': is_public,
        'token': basic_info['name_first']
    })
    return {
        'channel_id': data['channel_info'][-1]['channel_id']
    }


def channel_details(token, channel_id):
    data = getData()
    channel_id_integer = int(channel_id)
    flag_1 = False
    flag_2 = False
    # check if the channel ID is invalid
    for i in data['channel_info']:
        if(channel_id_integer == i['channel_id']):
            flag_1 = True
            return {
                'name': i['name'],
                'owner_members': i['owner_members'],
                'all_members': i['all_members']
            }
        # check if the user is not a member in this channel with channel_id
        for user in i['all_members']:
            basic_info = getUserFromToken(token) 
            if(basic_info['u_id'] == user['u_id']):
                flag_2 = True
    if(flag_1 == False):
        raise ValueError(description = 'channel_id is invalid')
    if(flag_2 == False):
        raise ValueError(description = 'u_id is not in this channel')
   
           
def user_profile(token, u_id):
    data = getData()
    u_id_integer = int(u_id)
    for i in data['user_info']:
        if(u_id_integer == i['u_id']):
            return {
                'email': i['email'],
                'name_first': i['name_first'],
                'name_last':  i['name_last'],
                'handle_str': i['handle_str']
            }
    raise ValueError(description = "u_id is invalid")
    
   
def channel_messages(token, channel_id, start):
    data = getData()
    channel_id_integer = int(channel_id)
    start_integer = int(start)
    basic_info = getUserFromToken(token)
    flag_1 = False
    flag_2 = False
    current_channel = {}
    # check if the channel_id doesn't exist        
    for i in data['channel_info']:
        if(channel_id_integer == i['channel_id']):
            flag_1 = True
            # check if the user is not a member in this channel with channel_id
            for user in ['all_members']:
                if(basic_info['u_id'] == user['u_id']):
                    flag_2 = True
                    current_channel['u_id'] = basic_info['u_id']
    if(flag_1 == False):
        raise ValueError(description = 'channel_id is invalid')
    if(flag_2 == False):
        raise AccessError(description = 'u_id is not in this channel')    
    for mess in data['message_info']:
        if(start_integer > len(mess['message'])): 
            raise ValueError(description = 'start is greater than the total number of messages') 
        current_channel['message'] = mess['message']
        current_channel['message_id'] = mess['message_id']
        current_channel['react_id'] = mess['react_id']
        current_channel['time_created'] = mess['time_created']
        current_channel['is_pinned'] = mess['is_pinned']
    return {
        'messages': [current_channel],
        'start': start,
        'end' : start + 50
    }


def message_send(token, channel_id, message):
    data = getData()
    channel_id_integer = int(channel_id)
    if(len(message) > 1000):
        raise ValueError(description = 'message is exceeding the maximum')
    for user in data['channel_info']:
        if(channel_id_integer == user['channel_id']):
            for i in user['all_members']:
                basic_info = getUserFromToken(token)
                return_message_id = generateMessage_id(message_id)
                if(basic_info['u_id'] == i['u_id']):
                    message_dict = {}
                    message_dict['message_id'] = return_message_id
                    message_dict['messages'] = message
                    message_dict['time_created'] = datetime.utcnow().replace(tzinfo=timezone.utc).timestamp()
                    message_dict['react_id'] = generateReact_id(react_id)
                    message_dict['is_pinned'] = True
                    data['message_info'].append(message_dict)
                    return {
                        'message_id': return_message_id
                    }
    raise AccessError(description = 'this user is not in this channel')


def sendlater_message(token, channel_id, message, time_sent):
    data = getData()
    channel_id_integer = int(channel_id)
    time_sent_integer = int(time_sent)
    time_now = datetime.utcnow().replace(tzinfo=timezone.utc).timestamp()
    return_message_id = generateMessage_id(message_id)
    if(time_sent_integer < time_now):
        raise ValueError(description = 'the time sent is a time in the past')
    if(len(message) > 1000):
        raise ValueError(description = 'message is more than 1000')
    flag = False
    for i in data['channel_info']:
        if(i['channel_id'] == channel_id_integer):
            flag = True
    if(flag == False):
        raise ValueError(description = 'the channel_id is invalid')
    for user in data['channel_info']:
        for i in user['all_members']:
            basic_info = getUserFromToken(token)
            if(basic_info['u_id'] == i['u_id']):
                message_dict = {}
                message_dict['message_id'] = return_message_id
                message_dict['messages'] = message
                message_dict['time_created'] = datetime.utcnow().replace(tzinfo=timezone.utc).timestamp()
                message_dict['react_id'] = generateReact_id(react_id)
                message_dict['is_pinned'] = True
                data['message_info'].append(message_dict)
                return {
                    'message_id': return_message_id
                } 
    raise AccessError(description = 'this user is not current in this channel')
