from flask import Flask, request
import re
import jwt 
import copy 
import hashlib
import dateutil 
from datetime import timezone
from datetime import datetime
from server.server import ValueError
from server.server import AccessError 

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

#---------------------------------
# dry dry dry
    
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
def resetUser_id():
    global user_id
    user_id = 0

def resetChannel_id():
    global channel_id 
    channel_id = 0

def resetMessage_id():
    global message_id
    message_id = 0
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
    data = getData()
    global SECRET
    decoded = jwt.decode(token, SECRET, algorithms=['HS256'])
    result = findUser(decoded['u_id'])
    return result

def hashPassword(password):
    return hashlib.sha256(password.encode()).hexdigest()

def findUser(u_id):
    data = getData()
    for u in data['user_info']:
        if u['u_id'] == u_id:
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
        'token': generateToken(user_id),
        'handle_str': 'TEAM WORK',
        'permission_id': 3
    })
    print("Registering", user_id , "in with token", generateToken(user_id))
    return {
        'u_id': data['user_info'][-1]['u_id'],
        'token': generateToken(user_id)
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
            print("Logging", user['u_id'] , "in with token", newToken)
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
    
def channels_create(token, name, is_public):
    data = getData()
    if (len(name) > 20):
        raise ValueError(description = "invalid channel name")
    basic_info = getUserFromToken(token)
    owner = []
    all_user = []
    owner.append({
        'u_id': basic_info['u_id'],
        'name_first': basic_info['name_first'],
        'name_last': basic_info['name_last']
    })
    flag = False
    if is_public == 'True' or is_public == 'true' or is_public == 'TRUE' or is_public == True:
        is_public = True
        flag = True
    if is_public == 'False' or is_public == 'false' or is_public == 'FALSE' or is_public == False:
        is_public = False
        flag = True
    data['user_info'][0]['permission_id'] = '1'
    if (flag == False): 
        raise ValueError(description = 'please set is_public to True or False')
    
    all_user.append({
        'u_id': basic_info['u_id'],
        'name_first': basic_info['name_first'],
        'name_last': basic_info['name_last']
    })
    data['channel_info'].append({
        'channel_id': generateChannel_id(channel_id),
        'owner_members': owner,
        'all_members': all_user,
        'name': name,
        'is_public': is_public,
        'token': basic_info['name_first'],
        'is_active': False,
        'time_finish': datetime.timestamp(datetime.now())
    })
    return {
        'channel_id': data['channel_info'][-1]['channel_id']
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
        raise ValueError("u_id we want to invite is invalid")

    for channel in data['channel_info']:
        if(channel_id_integer == channel['channel_id']):
            flag_2 = True 
            for i in channel['all_members']:
                if(i['u_id'] == basic_info['u_id']):
                    flag_3 = True
                    # invite this user into this channel
                    users_all = {}
                    users_all['u_id'] = u_id_integer
                    users_all['name_first'] = user['name_first']
                    users_all['name_last'] = user['name_last']
                    channel['all_members'].append(users_all)
    if(flag_2 == False):
        raise ValueError(description = "the channel_id is invalid")
    if(flag_3 == False):
        raise AccessError(description = "the authorised user is not already a member of this channel")
    return {}
    
   


def channel_details(token, channel_id):
    data = getData()
    channel_id_integer = int(channel_id)
    flag_1 = False
    flag_2 = False
    # check if the channel ID is invalid
    for i in data['channel_info']:
        if(channel_id_integer == i['channel_id']):
            flag_1 = True
            channel = i
        # check if the user is not a member in this channel with channel_id
            for user in i['all_members']:
                basic_info = getUserFromToken(token) 
                print(user)
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
        'u_id': i['u_id'],
        'email': i['email'],
        'name_first': i['name_first'],
        'name_last':  i['name_last'],
        'handle_str': i['handle_str'],
        'profile_img_url': 'https://marvelcinematicuniverse.fandom.com/wiki/Iron_Man?file=IronMan-EndgameProfile.jpg'
    }

def all_users(token):
    data = getData()
    basic_info = getUserFromToken(token)
    users = []
    users.append({
        'u_id': basic_info['u_id'],
        'email': basic_info['email'],
        'name_first': basic_info['name_first'],
        'name_last': basic_info['name_last'],
        'handle_str': basic_info['handle_str'],
        'profile_img_url': 'https://marvelcinematicuniverse.fandom.com/wiki/Iron_Man?file=IronMan-EndgameProfile.jpg'
    })
    return {
        'users': users
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
    ch_msgs = [msg for msg in data['message_info'] if msg['channel_id'] == channel_id]
    ch_msgs.sort(key=lambda msg: msg['time_created'])
    for ix, msg in enumerate(ch_msgs):
        if(ix+1 >= start):
            if msg['time_sent'] < datetime.timestamp(datetime.now()):
                return_list.append({
                    'u_id': msg['u_id'],
                    'message': msg['message'],
                    'time_created': msg['time_created'],
                    'is_unread': msg['is_unread']    
            })
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
                    message_dict['u_id'] = i['u_id']
                    message_dict['message'] = message
                    message_dict['time_created'] = datetime.timestamp(datetime.now())
                    message_dict['time_sent'] = datetime.timestamp(datetime.now())
                    message_dict['reacts'] = [{
                        'react_id': 1,
                        'u_ids': [],
                        'is_this_user_reacted': False
                    }]
                    message_dict['is_pinned'] = False
                    message_dict['channel_id'] = channel_id_integer
                    message_dict['is_unread'] = True
                    data['message_info'].append(message_dict)
                    return {
                        'message_id': return_message_id
                    }
    # if user is not in this channel currently
    raise AccessError('this user is not in this channel')

def sendlater_message(token, channel_id, message, time_sent):
    data = getData()
    channel_id_integer = int(channel_id)
    time_sent_integer = float(time_sent)
    time_now = datetime.utcnow().replace(tzinfo=timezone.utc).timestamp()
    return_message_id = generateMessage_id(message_id)
    # if the time_sent is time in the past 
    if(time_sent_integer < time_now):
        raise ValueError('the time sent is a time in the past')
    # if message's length is more than 1000 
    if(len(message) > 1000):
        raise ValueError('message is more than 1000')
    flag = False
    for i in data['channel_info']:
        if(i['channel_id'] == channel_id_integer):
            flag = True
    # if the channel_id is invalid
    if(flag == False):
        raise ValueError('the channel_id is invalid')
    for user in data['channel_info']:
        for i in user['all_members']:
            basic_info = getUserFromToken(token)
            if(basic_info['u_id'] == i['u_id']):
                message_dict = {}
                message_dict['message_id'] = return_message_id
                message_dict['message'] = message
                message_dict['time_created'] = datetime.timestamp(datetime.now())

                message_dict['time_sent'] = float(time_sent)/1000
                message_dict['react_id'] = 0
                message_dict['is_pinned'] = True
                message_dict['channel_id'] = channel_id_integer
                message_dict['is_unread'] = True
                message_dict['u_id'] = i['u_id']
                data['message_info'].append(message_dict)
                return {
                    'message_id': return_message_id
                } 
    # the authorised user is not in this channel currently
    raise AccessError('this user is not current in this channel')
    

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
    user_related_channel = []
    input_token = getUserFromToken(token)
    for channel in data['channel_info']:
        for user in channel['all_members']:
            if (user['u_id'] == input_token['u_id']):
                each_channel = {}
                each_channel['channel_id'] = channel['channel_id']
                each_channel['name'] = channel['name']
                user_related_channel.append(each_channel)
    return {
        'channels': user_related_channel  
    }

# return all channels
def channels_listall(token):
    data = getData()
    list_all_channels = []
    input_token = getUserFromToken(token)
    for channel in data['channel_info']:
        list_all_channels.append({
            'channel_id': channel['channel_id'],
            'name': channel['name']
        })
    return {
        'channels': list_all_channels
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
            
            for c in channel['owner_members']:
                if (basic_info['u_id'] == i['u_id']): 
                    found2 = c
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
                flag_2 = True
                all_users = {}
                all_users['u_id'] = basic_info['u_id']
                all_users['name_first'] = basic_info['name_first']
                all_users['name_last'] = basic_info['name_last']
                channel['all_members'].append(all_users)
            else:
                for user in data['user_info']:
                    if user['u_id'] == basic_info['u_id']:
                        if user['permission_id'] != 3:
                            flag_2 = True
                            all_users = {}
                            all_users['u_id'] = basic_info['u_id']
                            all_users['name_first'] = basic_info['name_first']
                            all_users['name_last'] = basic_info['name_last']
                            channel['all_members'].append(all_users)
    if (flag_1 == False): 
        raise ValueError(description = "channel_id is invalid")
    if (flag_2 == False): 
        raise AccessError(description = "cannot join channel as it is private") 
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

def message_remove(token, message_id):
    data = getData()
    input_message_id = int(message_id)
    basic_info = getUserFromToken(token)
    flag_1 = False # Checks for owner permission.
    flag_2 = False # Checks if message exists
    for msg in data['message_info']:
        if (msg['message_id'] == input_message_id):
            for channel in data['channel_info']:
                if (channel['channel_id']) == msg['channel_id']:  
                    for owner in channel['owner_members']:
                        if (owner['u_id'] == basic_info['u_id']):
                            flag_1 = True
            if (basic_info['permission_id'] != 3):
                flag_1 = True
            if (msg['u_id'] == basic_info['u_id']):
                flag_1 = True
            if (flag_1 == False):
                raise AccessError('user has insufficient permissions')
            flag_2 = True
            data['message_info'].remove(msg)
    if (flag_2 == False):
        raise ValueError('message does not exist')
    return {}

def message_edit(token, message_id, message):
    data = getData()
    input_message_id = int(message_id)
    basic_info = getUserFromToken(token)
    flag_1 = False # Checks for permission.
    flag_2 = False # Checks if its the authorized user.
    for i in data['message_info']:
        if (i['message_id'] == input_message_id):
            if (message == ""):
                data['message_info'].remove(i)
                return {}
            for channel in data['channel_info']:
                if (channel['channel_id']) == i['channel_id']:  
                    for owner in channel['owner_members']:
                        if (owner['u_id'] == basic_info['u_id']):
                            flag_1 = True
            if (basic_info['permission_id'] != 3):
                flag_1 = True
            if (i['u_id'] == basic_info['u_id']):
                flag_2 = True
            if (flag_1 == False):
                raise AccessError('user has insufficient permissions')
            if (flag_2 == False):
                raise AccessError('user is not authorized')    
            i['message'] = message
    return {}


def message_react(token, message_id, react_id):
    data = getData()
    basic_info = getUserFromToken(token)
    input_message_id = int(message_id)
    input_react_id = int(react_id)
    if (input_react_id != 1):
        ValueError('invalid react')
    flag_1 = False # Checks if the message exists.
    for msg in data['message_info']:
        for react in msg['reacts']:
            if (react['react_id'] == input_react_id):
                for u in react['u_ids']:
                    if (u == basic_info['u_id']):
                        raise ValueError('message has already been reacted to')
                react['u_ids'].append(basic_info['u_id'])
                if (msg['u_id'] == basic_info['u_id']):
                    react['is_this_user_reacted'] = True
                flag_1 = True
    if (flag_1 == False):
        raise ValueError('message does not exist')
    return {}

def message_unreact(token, message_id, react_id):
    data = getData()
    basic_info = getUserFromToken(token)
    input_message_id = int(message_id)
    input_react_id = int(react_id)
    if (input_react_id != 1):
        ValueError('invalid react')
    flag_1 = False # Checks if the message exists and has a react.
    flag_2 = False # Checks if the message has an active react.
    for msg in data['message_info']:
        for react in msg['reacts']:
            if (react['react_id'] == input_react_id):
                if (msg['u_id'] == basic_info['u_id']):
                    react['is_this_user_reacted'] = False
                for u in react['u_ids']:
                    if (u == basic_info['u_id']):
                        react['u_ids'].remove(basic_info['u_id'])
                        flag_2 = True
                flag_1 = True
    if (flag_1 == False):
        raise ValueError('message does not exist')
    if (flag_2 == False):
        raise ValueError('message does not have an active react')
    return {}

def message_pin(token, message_id):
    data = getData()
    input_message_id = int(message_id)
    basic_info = getUserFromToken(token)
    print(basic_info['u_id'])
    flag_1 = False # Checks for permission to pin.
    flag_2 = False # Checks if message exists.
    flag_3 = False # Checks if the user is a member of the channel that the message is within.
    for message in data['message_info']:
        if (message['message_id'] == input_message_id):
            for channel in data['channel_info']:
                if (channel['channel_id']) == message['channel_id']:  
                    for member in channel['all_members']:
                        print(member)
                        if (member['u_id'] == basic_info['u_id']):
                            flag_3 = True
            if (basic_info['permission_id'] != 3):
                flag_1 = True
            if (flag_3 == False):
                raise AccessError('user is not a member of the channel that the message is within')
            if (flag_1 == False):
                raise ValueError('user is not admin')
            if (message['is_pinned'] == True):
                raise ValueError('message already pinned')
            flag_2 = True
            message['is_pinned'] = True
    if (flag_2 == False):
        raise ValueError('message does not exist')
    return {}

def message_unpin(token, message_id):
    data = getData()
    input_message_id = int(message_id)
    basic_info = getUserFromToken(token)
    flag_1 = False # Checks for permission to unpin.
    flag_2 = False # Checks if message exists.
    flag_3 = False # Checks if the user is a member of the channel that the message is within.
    for message in data['message_info']:
        if (message['message_id'] == input_message_id):
            for channel in data['channel_info']:
                if (channel['channel_id']) == message['channel_id']:  
                    for owner in channel['owner_members']:
                        if (owner['u_id'] == basic_info['u_id']):
                            flag_1 = True
                    for member in channel['all_members']:
                        if (member['u_id'] == basic_info['u_id']):
                            flag_3 = True
            if (basic_info['permission_id'] != 3):
                flag_1 = True
            if (flag_1 == False):
                raise ValueError('user has insufficient permissions')
            if (flag_3 == False):
                raise AccessError('user is not a member of the channel that the message is within')
            if (message['is_pinned'] == False):
                raise ValueError('message already unpinned')
            flag_2 = True
            message['is_pinned'] = False
    if (flag_2 == False):
        raise ValueError('message does not exist')
    return {}

    
def search(token, q_str):
    messages_list = []

    channel_list = list(channels_list(token))

    for user in channel_list:
        for messages in user:
            if messages == q_str:
                messages_list.append(messages)

    return messages_list

def admin_userpermission_change(token, u_id, p_id):
    data = getData()
    if p_id != '1':
        if p_id != '2':
            if p_id != '3':
                raise ValueError(description = 'Not a valid permission')

    check_id = get_U_id(token)

    if u_id != check_id:
        raise ValueError(description = 'Not the correct user')
    
    for user in data['user_info']:
        if u_id == user['u_id']:
            if user['permission_id'] == '1' or user['permission_id'] == '2':
                user['permission_id'] = p_id
            else:
                raise ValueError(description = "User is not an authorised person to change permission")

    return {}

def admin_userpermission_change(token, u_id, permission_id):
    data = getData()
    owner_info = getUserFromToken(token)
    flag = 0
    for user in data['user_info']:
        if user['u_id'] == int(u_id) and flag == 1: 
            raise ValueError
        elif user['u_id'] == int(u_id) and flag == 0:
            flag = 1       
    if flag == 0:
        raise ValueError('Not a valid u_id')
    
    for user in data['user_info']:
        if user['u_id'] == int(u_id):
            if owner_info['permission_id'] == '1' or owner_info['permission_id'] == '2':
                user['permission_id'] = permission_id
            else:
                raise ValueError('User is not an authorised person to change permission')

    return {}


def user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end):
    data = getData()
    img = Image.open("img_url")
    height, width = img.size

    if (x_end - x_start) < width or (y_end - y_start) < height:
        raise ValueError('dimensions are within the boundries')

    user_info = getUserFromToken(token)
    
    for user in data['user_info']:
        if user['handle_str'] == user_info['handle_str']:
            if len(user['handle_str']) > 20:
                raise ValueError('user handle is more than 20 characters long')

    area = (x_start, y_start, x_end, y_end)
    img = img.crop(area)
    img.save("img_url")
    
    return dumps({})

def standup_start(token, channel_id, length):
    data = getData()
    basic_info = getUserFromToken(token)

    found = 0
    for channel in data['channel_info']:
        if channel['channel_id'] == (channel_id):
            if channel['is_active'] == True:
                found = 1
                raise ValueError ('There is an on going standup in this channel')
            else:
                found = 1

    if found == 0:
        raise ValueError('Not a valid channel_id for this user')

    if int(length) < 0:
        raise ValueError('Not a valid length for standUp')

    time_now = datetime.timestamp(datetime.now())
    finish_time = time_now + datetime.datetime.strptime(length)

    for ch in data['channel_info']:
        if ch['channel_id'] == channel_id:
            ch['is_active'] = True
            ch['time_finish'] = finish_time

    return {
        'finish_time': finish_time
    }

def standup_active(token, channel_id):
    data = getData()
    #channel_list = channels_list(token)

    active = False
    for channel in data['channel_info']:
        if channel['channel_id'] == channel_id:
            finish = channel['time_finish'] 
            if channel['is_active'] == True:
                active = True
    
    return {
        'active': active,
        'finish': channel['time_finish']
    }



