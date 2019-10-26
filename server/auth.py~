from json import dumps
from flask import Flask, request
import re
import jwt 
from werkzeug.exceptions import HTTPException
import copy 
import hashlib
import dateutil 
from flask_cors import CORS
from dummy_error import AccessError


APP = Flask(__name__)

SECRET = 'comp1531 project'
 
data = {
    'user_info': [],
    'channel_info': [],
    'message_info': []
}

user_id = 0;
channel_id = 0
message_id = 0

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

def getData():
    global data
    return data

def sendSuccess(data):
    return dumps(data)

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

class ValueError(HTTPException):
    code = 400
    message = 'No message specified'

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

timer = None 

def timerStart():
    global timer
    timer = datetime.datetime.now()

def timerGoing():
    global timer
    return datetime.datetime.now()

    
@APP.route('/auth/register', methods=['POST'])
def user_register_server():
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    data = getData()
    email = request.form.get('email')
    if(not re.search(regex, email)):
        raise ValueError(description = "invalid email")
    password = request.form.get('password')
    if(len(password) < 6):
        raise ValueError(description = "invalid password")
    name_first = request.form.get('name_first')
    if(len(name_first) < 1 or len(name_first) > 50):
        raise ValueError(description = "invalid name_first")
    name_last = request.form.get('name_last')
    if(len(name_last) < 1 or len(name_last) > 50):
        raise ValueError(description = "invalid name_last")
    data['user_info'].append({
        'email': email,
        'password': hashPassword(password),
        'name_first': name_first,
        'name_last': name_last,
        'u_id': generateU_id(user_id),
        'token': generateToken(name_first)
    })
    return sendSuccess({
        'token': generateToken(name_first),
        'u_id': data['user_info'][-1]['u_id']
    })

# how to test email doesn't belong to user 
@APP.route('/auth/login', methods=['POST'])
def user_login_server():
    data = getData()
    email = request.form.get('email')
    password = hashPassword(request.form.get('password'))
    for user in data['user_info']:
        if (user['email'] == email and hashPassword(password) == hashPassword(user['password'])):
            newToken = generateToken(user['name_first'])
            user['token'] = newToken
            return sendSuccess({
                'token': newToken,
                'u_id': user['u_id']
            })
        else:
            raise ValueError(description = "Can't login in because of error message")


@APP.route('/auth/logout', methods=['POST'])
def user_logout_server():
    data = getData()
    inputToken = generateToken(request.form.get('name_first'))
    user = getUserFromToken(inputToken)
    if user['name_first'] is not None:
        del user['token']
        return sendSuccess({
            'is_success': True
        })
    return sendSuccess({
        'is_success': False
    })
    
@APP.route('/channel/invite', methods=['POST'])
def channel_invite():
    data = getData()
    inputToken = generateToken(request.form.get('token'))
    channel_id = request.form.get('channel_id')
    basic_info = getUserFromToken(inputToken)
    u_id = request.form.get('u_id')
    channel_id_integer = int(channel_id)
    u_id_integer = int(u_id)
    # consider the one AccessError
    flag_1 = False
    for channel in data['channel_info']:        
        if(basic_info['u_id'] == channel['token']):
         
            flag_1 = True
    if(flag_1 == False):
        raise AccessError(description = 'this authorised user is not in this channel')
    flag_2 = False
    # consider the u_id ValueError
    for user in data['user_info']:
        if(u_id_integer == user['u_id']):
            flag_2 = True
    if(flag_2 == False):
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
                    return sendSuccess({})
    raise ValueError("channel_id is invalid")
    
   
@APP.route('/channels/create', methods=['POST'])
def channels_create():
    data = getData()
    inputToken = generateToken(request.form.get('token'))
    channelName = request.form.get('name')
    if (len(channelName) > 20):
        raise ValueError(description = "invalid channel name")
    is_public = request.form.get('is_public')
    basic_info = getUserFromToken(inputToken)
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
        'name': channelName,
        'is_public': is_public,
        'token': basic_info['u_id']
    })
    return sendSuccess({
        'channel_id': data['channel_info'][-1]['channel_id']
    })


# how to check the AccessError ? ? ? ? ? am i right ? ? ? ? ?
@APP.route('/channel/details', methods=['GET'])
def channel_details_server():
    data = getData()
    inputToken = generateToken(request.args.get('token'))
    channel_id = request.args.get('channel_id')
    channel_id_integer = int(channel_id)
    flag_1 = False
    flag_2 = False
    
    # check if the channel ID is invalid
    for i in data['channel_info']:
        if(channel_id_integer == i['channel_id']):
            flag_1 = True
            return sendSuccess({
                'name': i['name'],
                'owner_members': i['owner_members'],
                'all_members': i['all_members']
             })
        # check if the user is not a member in this channel with channel_id
        for user in i['all_members']:
            stored_token = getUserFromToken(inputToken) 
            if(stored_token['name_first'] == user[1]):
                flag_2 = True
    if(flag_1 == False):
        raise ValueError('channel_id is invalid')
    if(flag_2 == False):
        raise AccessError('u_id is not in this channel')
   
           
@APP.route('/user/profile', methods=['GET'])
def user_profile_server():
    data = getData()
    token = generateToken(request.args.get('token'))
    u_id = request.args.get('u_id')
    u_id_integer = int(u_id)
    for i in data['user_info']:
        if(u_id_integer == i['u_id']):
            return sendSuccess({
                'email': i['email'],
                'name_first': i['name_first'],
                'name_last':  i['name_last'],
                'handle_str': 'win win win'
            })
    raise ValueError(description = "u_id is invalid")
    
    
@APP.route('/channel/messages', methods=['GET'])
def channel_messages_server():
    data = getData()
    token = generateToken(request.args.get('token'))
    channel_id = int(request.args.get('channel_id'))
    start = int(request.args.get('start'))
    flag_1 = False 
    flag_2 = False
    current_channel = {}
    # check if the channel_id doesn't exist        
    for i in data['channel_info']:
        if(channel_id == i['channel_id']):
            flag_1 = True
            current_channel = i
            current_channel['messages'].append(i['messages'])
        # check if the user is not a member in this channel with channel_id
        for user in i['all_members']:
            if(getUserFromToken(inputToken) == user):
                flag_2 = True
    if(flag_1 == False):
        raise ValueError('channel_id is invalid')
    if(flag_2 == False):
        raise AccessError('u_id is not in this channel')
    if(start > len(current_channel['messages'])):
        raise ValueError('start is greater than the total number of messages')
    return sendSuccess({
        'messages': current_channel['messages'],
        'start': start,
        'end' : start + 50
    })

@APP.route('/message/send', methods=['POST'])
def send_message_server():
    data = getData()
    inputToken = generateToken(request.form.get('token'))
    channel_id = int(request.form.get('channel_id'))
    message = request.form.get('message') 
    if(len(message) > 1000):
        raise ValueError('message is exceeding the maximum')
    for user in data['channel_info']:
        for i in user['all_members']:
            basic_info = getUserFromToken(inputToken)
            return_message_id = generateMessage_id(message_id)
            if(basic_info['u_id'] == i['u_id']):
                message_dict = {}
                flag = True
                message_dict['message_id'] = return_message_id
                message_dict['message'] = message
                data['message_info'].append(message_dict)
                return sendSuccess({
                    'message_id': return_message_id
                })
    raise AccessError(description = 'this user is not in this channel')
    
   
    
@APP.route('/message/sendlater', methods=['POST']
def sendlater_message_server():
    data = getData()
    inputToken = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    time_sent = datetime.datetime.now()
    if((time_sent - timer).total_seconds() < 0):
        raise ValueError('the time sent is a time in the past')
    if(len(message) > 1000):
        raise ValueError('message is more than 1000')
    flag = False
    for i in data['channel_info']:
        if(i['name'] == channel_id):
            flag = True
    if(flag == False):
        raise ValueError('the channel_id is invalid')
    return_message_id = 0
    flag = False
    for user in data['channel_info']:
        for i in user['all_members']:
            if(getUserFromToken(inputToken) == i):
                flag = True
                # question here : can you tell me the originality of message_id ? ? ? ?
                return_message_id = user['message_id']
    if(flag == False):
        raise AccessError('this user is not in this channel')
    return sendSuccess({
        'message_id': return_message_id
    })
    
   

if __name__ == '__main__':
    APP.run(debug = True, port=5000)


