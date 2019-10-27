from json import dumps
from flask import Flask, request
from flask_mail import Mail, Message
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




SECRET = 'comp1531 project' 

data = {
    'user_info': [],
    'channel_all': [],
    'message_info': []
}
 
def findUser(user_id):
    for user in data['user_info']:
        if user['u_id'] == user_id:
            return user
    return None

def getData():
    global data
    return data
   
def sendSuccess(data):
    return dumps(data)

def generateToken(user_id):
    global SECRET
    encoded = jwt.encode({'user_id': user_id}, SECRET, algorithm='HS256')
    return encoded.decode('utf-8') # asdfasdfadsf

# return a dictionary 
def getUserFromToken(token):
    global SECRET
    decoded = jwt.decode(token, SECRET, algorithms=['HS256'])
    return findUser(decoded['user_id'])

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

APP.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'HASCdevteam@gmail.com',
    MAIL_PASSWORD = "Alltheboys"
)

@APP.route('/channel/leave', methods=['POST']) 
def channel_leave(): 
    data = getData()
    token = generateToken(request.form.get('token'))
    channelID = int(request.form.get('channel_id'))
    user = getUserFromToken(token) # returns a dictonary 
    flag_1 = False
    for channel in data['channel_info']:  
        if channel['channel_id'] == channelID: 
            flag_1 = True 
            for i in channel['all_members']:
                if (user['u_id'] == i['u_id']): 
                    del i
                
            for i in channel['owner_member']:
                if (user['u_id'] == i['u_id']):
                    del i
    if(flag_1 == False):
        raise ValueError(description = 'channel_id is invalid')
    return sendSuccess({})
''' 
@APP.route('/channel/join', methods=['POST'])
    def channel_join():
    data = getData()
    token = request.form.get('token')
    channelID = request.form.get('channel_id')
    user = getUserFromToken(token)
    flag_1 = False 
    flag_2 = False
    for channel in data['channel_all']: 
        if channel['channel_id'] == channelID: 
            flag_1 = True 
            if channel['is_public'] == True: 
                channel['all_members'].append(user)
            else: 
            
           
                for i in channel['owners']: 
                    if (user == channel[i]):
                     channel['all_members'].append(user)
            
           #need channel permissions 
    if (flag_1 == False): 
        raise ValueError('channel_id is invalid')
    if (flag_2 == False): 
        raise AccessError('cannot join channel as it is private') 
    return sendSucess({})

@APP.route('/channel/addowner', methods=['POST'])
def addowner(tken): 
    data = getData()
    token = generateToken(request.form.get('token'))
    channelID = int(request.form.get('channel_id'))
    user_basic_info = getUserFromToken(token)
    user_id = int(request.form.get('u_id'))
    flag_1 = False 
    flag_2 = False 
    flag_3 = False  
    for channel in data['channels']: 
        if channel['channel_id'] == channelID: 
            flag_1 = True
            for i in channel['owner_members']:
                if user_id == i['u_id']: 
                    flag_2 = True # already an owner 
                if user_basic_info['u_id'] == i['u_id']: 
                    flag_3 = True # if false the person giving making another person an owner is not an owner themselfs 
                if (flag_2 == False and flag_3 == True): 
                    channel['owners'].append(user_id)
    if(flag_1 == False): 
        raise ValueError('channel id is not a valid channel') 
    if(flag_2 == True): 
        raise ValueError('the user id you are making an owner is already and owner')
    if (flag_3 == False): 
        raise AccessError('the authorsied user is not an owner of the channel') 
    # permission ned channel permissions function 
    return sendSuccess({})

@APP.route('/channel/removeowner', methods=['POST']) 
def removeowner(): 
    data = getData()
    token = request.form.get('token')
    channelID = request.form.get('channel_id')
    user = getUserFromToken(token)
    user_id = request.form.get('u_id')
    flag_1 = False 
    flag_2 = False 
    flag_3 = False  
    for channel in data['channel_all']: 
        if channel['channel_id'] == channelID: 
            flag_1 = True
            for i in channel['owners']:    
                if user_id == channel[i]: 
                    flag_2 = True #user is an owner of the channel
                if user == channel[i]:
                    flag_3 = True # if false the person removing another person as an owner is not an owner themselves
                if (flag_2 == True and flag_3 == True): 
                    del channel[i] 
    if(flag_1 == False): 
        raise ValueError('channel id is not a valid channel) 
    if(flag_2 == False): 
        raise ValueError('user with the user id is not an owner of the channel')
    if (flag_3 == False): 
        raise AccessError('the authorsied user is not an owner of the channel') 
    # permission ned channel permissions function 
    return sendSuccess({})
    '''
@APP.route('/auth/passwordrest/request', methods=['POST']) 
def passwordreset_request():
    data = getData() 
    mail = Mail(APP)
    email = 'cameron.ha@hotmail.com'#request.form.get('email')
    flag = False
    code = int(random_code_generator(10))
    for user in data['user_info']: 
        user['email'].append(email)
        if user['email'] == email:
            flag = True
            user['reset_code'] = code #added to the data structure 
            first_name = user['first_name'] 
            try:
                msg = Message("Reset, Password Request Slackr",
                    sender="HASCdevteam@gmail.com",
                    recipients=email)
                msg.body = 'Hi' + first_name + 'You have requested for a change in your password, please use the code provided below to reset your account.\n' + code + '\n regards the slackr development, team.'
                mail.send(msg)
               # return 'Mail sent!'
           # except Exception as e:
               # return (str(e))
def random_code_generator(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

    
'''
@APP.route('/auth/passwordreset/reset', methods=['POST'])
def passwordreset_reset():
    data = getData()
    reset_code = request.form.get('reset_code')
    newpassword = request.form.get('password')
    flag = False 
    for user in data['user_info']: 
        if user['reset_code'] == reset_code: 
            flag = True 
            if (len(newpassword) < 6): 
                raise ValueError('password entered is less than 6 characters and not a valid ppassword')
            else: 
                user['password'] = hashPassword(newpassword) 
    if (flag == False): 
        raise ValueError('invalid reset code entered')
    return sendSuccess({})
    
def message_edit(token, message_id, message): 
    data = getData()
    token = generateToken(request.form.get('token'))
    user = getUserFromToken(token)
    message = request.form.get('message')
    message_id = int(request.form.get('message_id'))
    
    
    basic_info = getUserFromToken(token)
    message_id = generate
    for message in data['message_info']: 
        if(message[message_id] == input_message_id): 
            if
            message[message] = input_message

'''
if __name__ == '__main__':
    APP.run(debug = True, port=4002)
