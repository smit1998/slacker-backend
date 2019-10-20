from json import dumps
from flask import Flask, request
import re
import jwt 
import hashlib

APP = Flask(__name__)
       
SECRET = 'comp1531 project'
 
data = {
    'user_info': [{}],
    'channel_info': [{}]
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
                'token': newToken
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
  
# how to check the AccessError ? ? ? ? ? 
@APP.route('/channel/details', methods=['GET'])
def channel_details():
    data = getData()
    inputToken = request.args.get('token')
    channel_id = request.args.get('channel_id')
    flag = False
    for i in data['channel_id']:
        if(channel_id == i['name']):
            flag = True
    if(flag == False):
        raise ValueError('channel_id is invalid')  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    for user in data['user_info']:
        if(getUserFromToken(inputToken) == user['token'] and channel_id == user['channel_id']):
            
        raise AccessError("token is invalid")
    for i in data['channel_info']['channel_id']:
        if(channel_id == i):
            return sendSuccess({
                'name': channel_id
                'owner_members': data['channel_info']['channel_id']['owner_members']
                'all_member': data['channel_info']['channel_id']['all_members']
            })
    
            

@APP.route('/user/profile', methods=['GET'])
def user_profile():
    data = getData()
    token = request.args.get('token')
    u_id = request.args.get('u_id')
    if(not u_id == generateU_id(data['user_info']['email'])):
        raise ValueError("u_id is invalid")
    return sendSuccess({
        'email': data['user_info']['email'],
        'name_first': data['user_info']['name_first'],
        'name_last': data['user_info']['name_last'],
        'handle_str': 'who are you'
    })
    
@APP.route('/channel/messages', methods=['GET'])
def channel_messages():
    data = getData()
    token = request.args.get('token')
    if(not token == getUserFromToken(data['user_info']['token'])):
        raise AccessError('token is invalid')
    







if __name__ == '__main__':
    APP.run()


