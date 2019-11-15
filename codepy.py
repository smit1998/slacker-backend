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
from flask_mail import Mail, Message

class AccessError(HTTPException):
    code = 400 
    message = 'No message specified'
    

class ValueError(HTTPException):
    code = 400
    message = 'No message specified'

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

#---------------------------------------------
# question1: deal with the defaultHandler function
#---------------------------------------------

class ValueError(HTTPException):
    code = 400
    message = 'No message specified'

class AccessError(HTTPException):
    code = 400 
    message = 'No message specified'

#---------------------------------
# dry dry dry
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

def generateChannel_id(c_id):
    global channel_id
    channel_id = channel_id + 1
    c_id = channel_id
    return c_id
#-------------------------------- 

#------------------------------
#dry dry dry
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
#-------------------------------   
    
def getData():
    global data
    return data
 
# transform this token from bytes into string
def generateToken(u_id):
    global SECRET
    encoded = jwt.encode({'u_id': u_id}, SECRET, algorithm='HS256')
    return encoded.decode('utf-8') # asdfasdfadsf

# return a dictionary 
def getUserFromToken(token):
    global SECRET
    decoded = jwt.decode(token, SECRET, algorithms=['HS256'])
    return findUser(decoded['u_id'])

def hashPassword(password):
    return hashlib.sha256(password.encode()).hexdigest()

def findUser(inputName):
    for u in data['user_info']:
        if u['u_id'] == inputName:
            return u
    return None
    
def user_register(email, password, name_first, name_last):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    data = getData()
    global user_id
    # email is invalid 
    if(not re.search(regex, email)):
        raise ValueError(description = "invalid email")
    # password is invalid 
    if(len(password) < 6):
        raise ValueError(description = "invalid password")
    # name_first is invalid
    if(len(name_first) < 1 or len(name_first) > 50):
        raise ValueError(description = "invalid name_first")
    # name_last is invalid
    if(len(name_last) < 1 or len(name_last) > 50):
        raise ValueError(description = "invalid name_last")
    flag = False
    for i in data['user_info']:
        if(i['email'] == email):
            flag = True
    # email address is already been used by other users
    if(flag == True):
        raise ValueError(description = 'email address is already been used')
    # store the baisc infomation of the each user
    data['user_info'].append({
        'email': email,
        'password': hashPassword(password),
        'name_first': name_first,
        'name_last': name_last,
        'u_id': generateU_id(user_id),
        #'reset_code': reset_code,
        # question 2: what about we have two users' are both having same name_first, do they would create two different tokens ? ? ? 
        'token': generateToken(name_first),
        # question 3: the hand_str should be changed all the times, or just fixed. 
        'handle_str': 'TEAM WORK'
    })
    return {
        'token': generateToken(user_id),
        'u_id': data['user_info'][-1]['u_id']
    }


def user_login(email, password):
    data = getData()
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    # email is invalid
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
            newToken = generateToken(user['u_id'])
            user['token'] = newToken
            return {
                'token': newToken,
                'u_id': user['u_id']
            }
    # email typed is not belonging to user
    if(flag_1 == False):
        raise ValueError(description = "email entered is not belong to user")
    # password is invalid
    if(flag_2 == False):
        raise ValueError(description = "password is not correct")


def user_logout(token):
    data = getData()
    user = getUserFromToken(token)
    # invalidate the aothorised user
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
    flag_2 = False
    flag_3 = False
    # u_id is invalid
    for user in data['user_info']:
        if(u_id_integer == user['u_id']):
            flag_1 = True
    if(flag_1 == False):
        raise ValueError(description = "u_id we want to invite is invalid")
    # consider the channel_id ValueError
    #-----------------------------
    # question4: is that reasonable ? ? ? ? ? ?
    #------------------------------
    for channel in data['channel_info']:
        if(channel_id_integer == channel['channel_id']):
            flag_2 = True 
            for i in channel['all_members']:
                if(i['u_id'] == basic_info['u_id']):
                    flag_3 = True
                    # invite this user into this channel
                    all_users = {}
                    all_users['u_id'] = u_id_integer
                    all_users['name_first'] = user['name_first']
                    all_users['name_last'] = user['name_last']
                    channel['all_members'].append(all_users)
    if(flag_2 == False):
        raise ValueError(description = "the channel_id is invalid")
    if(flag_3 == False):
        raise AccessError(description = "the authorised user is not already a member of this channel")
    return {}
    
   
def channels_create(token, name, is_public):
    data = getData()
    if (len(name) > 20):
        raise ValueError(description = "invalid channel name")
    basic_info = getUserFromToken(token)
    
    owner = {}
    owner['u_id'] = basic_info['u_id']
    owner['name_first'] = basic_info['name_first']
    owner['name_last'] = basic_info['name_last']
    flag = False
    if is_public == 'True':      
        is_public = True
        flag = True
    if is_public == 'False':
        is_public = False
        flag = True
    
    if (flag == False): 
        raise ValueError(description = 'please set is_public to True or False with capital T/F')
    all_users = {}
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
    channel = None
    # check if the channel ID is invalid
    for i in data['channel_info']:
        if(channel_id_integer == i['channel_id']):
            flag_1 = True
            channel = i
        # check if the user is not a member in this channel with channel_id
            for user in i['all_members']:
                basic_info = getUserFromToken(token) 
                if(basic_info['u_id'] == user['u_id']):
                    flag_2 = True
    if(flag_1 == False):
        raise ValueError(description = 'channel_id is invalid')
    if(flag_2 == False):
        raise AccessError(description = 'u_id is not in this channel')
    return {
        'name': channel['name'],
        'owner_members': channel['owner_members'],
        'all_members': channel['all_members']
     }
           
def user_profile(token, u_id):
    data = getData()
    flag = False
    u_id_integer = int(u_id)
    for i in data['user_info']:
        if(u_id_integer == i['u_id']):
            flag = True
    # check the user is a invalid user
    if(flag == False):
        raise ValueError(description = "u_id is invalid")
    return {
        'email': i['email'],
        'reset_code': i['reset_code'],
        'name_first': i['name_first'],
        'name_last':  i['name_last'],
        'handle_str': i['handle_str']
    }

def channel_messages(token, channel_id, start):
    data = getData()
    channel_id = int(channel_id)
    start = int(start)
    basic_info = getUserFromToken(token)
    flag_1 = False
    flag_2 = False
    return_list = []
    # check if the channel_id doesn't exist        
    for i in data['channel_info']:
        if(channel_id == i['channel_id']):
            flag_1 = True
            # check if the user is not a member in this channel with channel_id
            for user in i['all_members']:
                if(basic_info['u_id'] == user['u_id']):
                    flag_2 = True
    if(flag_1 == False):
        raise ValueError(description = 'channel_id is invalid')
    if(flag_2 == False):
        raise AccessError(description = 'u_id is not in this channel')    
    if(start > len(data['message_info'])): 
        raise ValueError(description = 'start is greater than the total number of messages') 
    print(data['message_info'])
    ch_msgs = [msg for msg in data['message_info'] if msg['channel_id'] == channel_id]
    ch_msgs.sort(key=lambda msg: msg['time_created'])
    for ix, msg in enumerate(ch_msgs):
        
        # if the start is greater than the total length of messages
        #------------------------------
        # question5: messages is the list of dictonary, so how to get the total length of it ? ? ? ?
        # And btw, I just create a dictonary for each function, do we need to use recursion to store each infomation inside the outer list ? ? ? ?
        #------------------------------
 
        if(ix+1 >= start):
            return_list.append(msg)
    return {
        'messages': return_list,
        'start': start,
        'end' : start + 50
    }


def message_send(token, channel_id, message):
    data = getData()
    channel_id_integer = int(channel_id)
    # message is more than 1000 characters
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
                    message_dict['channel_id'] = channel_id_integer
                    data['message_info'].append(message_dict)
                    return {
                        'message_id': return_message_id
                    }
    # if user is not in this channel currently
    raise AccessError(description = 'this user is not in this channel')


def sendlater_message(token, channel_id, message, time_sent):
    data = getData()
    channel_id_integer = int(channel_id)
    time_sent_integer = int(time_sent)
    time_now = datetime.utcnow().replace(tzinfo=timezone.utc).timestamp()
    return_message_id = generateMessage_id(message_id)
    # if the time_sent is time in the past 
    if(time_sent_integer < time_now):
        raise ValueError(description = 'the time sent is a time in the past')
    # if message's length is more than 1000 
    if(len(message) > 1000):
        raise ValueError(description = 'message is more than 1000')
    flag = False
    for i in data['channel_info']:
        if(i['channel_id'] == channel_id_integer):
            flag = True
    # if the channel_id is invalid
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
    # the authorised user is not in this channel currently
    raise AccessError(description = 'this user is not current in this channel')
    

def user_profile_setname(token, name_first, name_last):
    data = getData()
    if (len(name_first) > 50 or len(name_last) < 1):
       raise ValueError("name_first is not between 1 and 50.")
    if (len(name_last) > 50 or len(name_last) < 1):
        raise ValueError("name_last is not between 1 and 50.")
    #change the first and last names
    basic_info = getUserFromToken(token)
    
    for user in data['user_info']:
        if (user['u_id'] == basic_info['u_id']):
            user['name_first'] = name_first
            user['name_last'] = name_last
    return {}


def user_profile_setemail(token, email):
    data = getData()
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(not re.search(regex, email)):
        raise ValueError(description = "invalid email")
    flag = False
    for i in data['user_info']:
        if(i['email'] == email):
            flag = True
    # email address is already been used by other users
    if(flag == True):
        raise ValueError(description = 'email address is already been used')
    
    basic_info = getUserFromToken(token)
    
    for users in data['user_info']:
            if(users['u_id'] == basic_info['u_id']):
                users['email'] = email
    return {}

def user_profile_sethandle(token, handle_str):
    data = getData()
    if (len(handle_str) < 3 or len(handle_str) > 20):
        raise ValueError("handle_str is invalid")
    for user in data['user_info']:
        if user['handle_str'] == handle_str:
            raise ValueError("Handle_str already in use")
    basic_info = getUserFromToken(token)
    for u in data['user_info']:
        if u['u_id'] == basic_info['u_id']:
            u['handle_str'] = handle_str

    return {}      

# return channels [channel_id, name]
def channels_list(token):
    data = getData()
    channels = []
    input_token = getUserFromToken(token)
    for channel in data['channel_info']:
        for user in channel['all_members']:
            if (user['u_id'] == input_token['u_id']):
                channels.append(int(channel['channel_id']))
                channels.append(channel['name'])
                print(channel['channel_id'])
                print(channel['name'])
    return {
        'channels': channels     
    }


def channel_leave(token,channel_id): 
    data = getData()
    basic_info = getUserFromToken(token)
    channel_id_integer = int(channel_id)
    #u_id_integer = int(u_id) returns a dictonary 
    flag_1 = False
    for channel in data['channel_info']:  
        if (channel_id_integer == channel['channel_id']): 
            flag_1 = True 
            found1 = None
            for i in channel['all_members']:
                if (basic_info['u_id'] == i['u_id']): 
                    found1 = i
            if found1 != None:
                channel['all_members'].remove(i)
    if(flag_1 == False):
        raise ValueError(description = 'channel_id that you are trying to leave from is invalid')
    return {}

def channel_join(token, channel_id):
    data = getData()
    basic_info = getUserFromToken(token)
    channel_id_integer = int(channel_id)
    flag_1 = False 
    flag_2 = False
    for channel in data['channel_info']: 
        if (channel_id_integer == channel['channel_id']): 
            flag_1 = True
            if (channel['is_public'] == True):
                all_users = {}
                all_users['u_id'] = basic_info['u_id']
                all_users['name_first'] = basic_info['name_first']
                all_users['name_last'] = basic_info['name_last']
                channel['all_members'].append(all_users)
    if (flag_1 == False): 
        raise ValueError(description = "channel_id is invalid")
    #if (flag_2 == True): 
        #raise AccessError(description = "cannot join channel as it is private") 
    return {}

def addowners_channel(token, channel_id, u_id):
    data = getData()
    basic_info = getUserFromToken(token)
    channel_id_integer = int(channel_id)
    u_id_integer = int(u_id)
    flag_1 = False 
    flag_2 = False 
    flag_3 = False
    flag_4 = False
    for user in data['user_info']:
        if(u_id_integer == user['u_id']):
            flag_1 = True
    if (flag_1 == False): 
        raise ValueError(description = "u_id we want to make owner is invalid")
        
    for channel in data['channel_info']:
        if (channel_id_integer == channel['channel_id']):
            flag_2 = True 
            for i in channel['owner_members']:
                if (i['u_id'] == u_id_integer): 
                    flag_3 = True
            for i in channel['owner_members']: 
                if (i['u_id'] == basic_info['u_id']): 
                    flag_4 = True
            for i in channel['owner_members']:
                if (i['u_id'] == basic_info['u_id'] and flag_3 == False):
                    owner = {} 
                    owner['u_id'] = u_id_integer
                    owner['name_first'] = user['name_first']
                    owner['name_last'] = user['name_last']
                    channel['owner_members'].append(owner)
                
    if (flag_2 == False): 
        raise ValueError(description = "channel id is not a valid channel") 
    if (flag_3 == True): 
        raise ValueError(description = "user is already an owner of the channel")
    if (flag_4 == False): 
        raise AccessError(description = "the authorsied user is not an owner of the channel") 
    return {}
    
def removeowners_channel(token, channel_id, u_id):
    data = getData()
    basic_info = getUserFromToken(token)
    channel_id_integer = int(channel_id)
    u_id_integer = int(u_id)
    flag_1 = False 
    flag_2 = False 
    flag_3 = False
    flag_4 = False
    for user in data['user_info']:
        if(u_id_integer == user['u_id']):
            flag_1 = True
    if (flag_1 == False): 
        raise ValueError(description = "u_id we want to remove as owner is invalid")
        
    for channel in data['channel_info']:
        if (channel_id_integer == channel['channel_id']):
            flag_2 = True 
            for i in channel['owner_members']:
                if (i['u_id'] == u_id_integer): 
                    flag_3 = True
            for i in channel['owner_members']: 
                if (i['u_id'] == basic_info['u_id']): 
                    flag_4 = True
            found = None
            for i in channel['owner_members']:
                if (i['u_id'] == basic_info['u_id'] and flag_3 == True):
                    found = i
                    
            if found != None:
                channel['owner_members'].remove(i)
                
    if (flag_2 == False): 
        raise ValueError(description = "channel id is not a valid channel") 
    if (flag_3 == False): 
        raise ValueError(description = "user is not an owner of the channel")
    if (flag_4 == False): 
        raise AccessError(description = "the authorsied user is not an owner of the channel") 
    return {}

def passwordreset_request(email, APP):
    data = getData() 
    mail = Mail(APP)
    flag = False
    code = '123'
    for user in data['user_info']:
        if (user['email'] == email):
            flag = True
            #user['reset_code'] = code #added to the data structure 
            first_name = user['name_first']            
            msg = Message("Reset, Password Request Slackr",
                sender= "HASCdevteam@gmail.com",
                recipients = [email])
            msg.body = 'Hi ' + first_name + '\n \n You have requested for a change in your password, please use the code provided below to reset your account.\n \n \n' + code + ' \n \n regards the slackr development, team.'
            mail.send(msg)
    return {}

def random_code_generator(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
