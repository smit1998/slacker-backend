from json import dumps
from flask import Flask, request
import re
import jwt 
import hashlib
import datatime 

APP = Flask(__name__)

# the difference between SECRET and secret  (on video 15.00 mins)
SECRET = 'comp1531 project'
 
data = {
    'user_info': [{}],
    'channel_info': [{}],
    'message_info': [{}]
}

def getData():
    global data
    return data

def sendSuccess(data):
    return dumps(data)

# do we need that ? ? ? ?
def sendError(message):
    return dumps({
        '_error' : message,
    })

def generateToken(name_first):
    global SECRET
    encoded = jwt.encode({'name_first': Andy}, SECRET, algorithm='HS256')
    return str(encoded)

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

def generateU_id(name_last):
    return name_last + 'z5183885'

timer = None 

def timerStart():
    global timer
    timer = datetime.datetime.now()

def timerGoing():
    global timer
    return datetime.datetime.now()

    
@APP.route('/auth/register', methods=['POST'])
def user_register():
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    data = getData()
    email = request.form.get('email')
    if(not re.search(regex, email)):
        raise ValueError("invalid email")
    password = request.form.get('password')
    if(len(password) < 6):
        raise ValueError("invalid password")
    name_first = request.form.get('name_first')
    if(len(name_first) < 1 or len(name_first) > 50):
        raise ValueError("invalid name_first")
    name_last = request.form.get('name_last')
    if(len(name_last) < 1 or len(name_first) > 50):
        raise ValueError("invalid name_last")
    data['user_info'].append({
        'email': email,
        'password': hashPassword(password),
        'name_first': name_first,
        'name_last': name_last
        # HOW TO RESET THE FLAG EFFECTIVELY ! ! ! ? ? ?
        'flag' : False
    })
    return sendSuccess({
        'token': generateToken(name_first),
        'u_id': generateU_id(name_last)
    })


@APP.route('/auth/login', methods=['POST'])
def user_login():
    data = getData()
    email = request.form.get('email')
    password = request.form.get('password')
    for user in data['user_info']:
        if(email == user['email'] and password == hashPassword(user['password'])): 
            newToken = generateToken(user['name_first'])
            user['token'].append(newToken)
            return sendSuccess({
                'token': newToken,
                'u_id': generateU_id(email)
            })
    raise ValueError("Can't login in because of error message")


@APP.route('/auth/logout', methods=['POST'])
def user_logout():
    data = getData()
    inputToken = request.form.get('token')
    user = getUserFromToken(inputToken)
    if user is not None:
        user['token'].remove(inputToken)
        return sendSuccess({
            'is_success': True
        })
    return sendSuccess({
        'is_success': False
    })
    
# HOW TO CHECK THE ACCESSERROR ? ? ? ? ? 
@APP.route('/channel/invite', methods=['POST'])
def channel_invite():
    data = getData()
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    u_id = request.form.get('u_id')
    # consider the one AccessError
    for channel in data['channel_info']:
        for i in channel['all_members']:
            if(getUserFromToken(token) == i):
                channel['flag'] = True
    if(channel['flag'] == False):
        raise AccessError('this authorised user is not in this channel')
    # reset the flag
    channel['flag'] = False
    # consider the u_id ValueError
    for user in data['user_info']:
        if(u_id == user['u_id']):
            user['flag'] = True
    if(user['flag'] == False):
        raise ValueError("u_id is invalid")
    # reset the flag
    user['flag'] = False
    # consider the channel_id ValueError
    for channel in data['channel_info']:
        if(channel_id == channel['name']):
            for i in channel['all_members']:
                if(getUserFromToken(token) == i):
                    channel['flag'] = True
    if(channel['flag'] == False):
        raise ValueError("channel_id is invalid")
    # reset the flag
    channel['flag'] = False
    # append a new user inside the channel
    # How do we locate this channel ? ? ? ? I just assume the channel_id is name of this channel.
    # is that right ?
    for i in data['channel_id']:
        if(channel_id == i['name']):
            i['all_members'].append(u_id)
    return sendSuccess({})
  
# how to check the AccessError ? ? ? ? ? am i right ? ? ? ? ?
@APP.route('/channel/details', methods=['GET'])
def channel_details():
    data = getData()
    inputToken = request.args.get('token')
    channel_id = request.args.get('channel_id')
    flag_1 = False
    flag_2 = False
    # check if the channel ID is invalid
    display_channel = {}
    for i in data['channel_id']:
        if(channel_id == i['name']):
            flag_1 = True
            display_channel['name'].append(channel_id)
            display_channel['owner_members'].append(i['owner_members'])
            display_channel['all_members'].append(i['all_members']) 
        # check if the user is not a member in this channel with channel_id
        for user in i['all_members']:
            if(getUserFromToken(inputToken) == user):
                flag_2 = True
    if(flag_1 == False):
        raise ValueError('channel_id is invalid')
    if(flag_2 == False):
        raise AccessError('u_id is not in this channel')
    return sendSuccess({
        'name': channel_id,
        'owner_members': display_channel['owner_members'],
        'all_members': display_channel['all_members']
    })
    
# do we need to check the token in this case ? ? ? ?            
@APP.route('/user/profile', methods=['GET'])
def user_profile_server():
    data = getData()
    token = request.args.get('token')
    u_id = request.args.get('u_id')
    flag = False
    user_display = {}
    for i in data['user_info']:
        if(u_id == i['u_id']):
            flag = True
            user_display['email'].append(i['email'])
            user_display['name_first'].append(i['name_first'])
            user_display['name_last'].append(i['name_last'])
            user_display['handle_str'].append('win win win')
    if(flag == False);
        raise ValueError("u_id is invalid")
    return sendSuccess({
        'email': user_display['email'],
        'name_first': user_display['name_first'],
        'name_last':  user_display['name_last'],
        'handle_str': user_display['handle_str']
    })
    
    
@APP.route('/channel/messages', methods=['GET'])
def channel_messages_server():
    data = getData()
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    start = request.args.get('start')
    flag_1 = False 
    flag_2 = False
    current_channel = {}
    # check if the channel_id doesn't exist        
    for i in data['channel_id']:
        if(channel_id == i['name']):
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
        raise ValueError=('start is greater than the total number of messages')
    return sendSuccess({
        'messages': current_channel['messages'],
        'start': start,
        'end' : start + 50
    })

@APP.route('/message/send', methods=['POST'])
def send_message_server():
    data = getData()
    inputToken = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message') 
    if(len(message) > 1000):
        raise ValueError('message is exceed the maximum')
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
    message_info['message_id'].append(return_message_id)
    message_info['messages'].append(message)
    return sendSuccess({
        'message_id': return_message_id
    })
    
@APP.route('message/sendlater', methods=['POST'])
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
    APP.run()


