from json import dumps
from flask import Flask

app = Flask(__name__) 

SECRET = 'comp1531 project'

data = {
    'user_info': [],
    'channel_info': [],
    'message_info': []
}

channel_id = 0

def generateChannel_id():
    global channel_id
    channel_id += 1
    return channel_id

def generateToken(name_first):
    global SECRET
    encoded = jwt.encode({'name_first': name_first}, SECRET, algorithm='HS256')
    return encoded.decode('utf-8')

def getData():
    global data
    return data

def channels_list(token):
    return channels

def channels_listall(token):
    return channels

@app.route('/channel/create', methods=['POST'])
def channels_create(token, name, is_public):
    data = getData()
    inputToken = generateToken(request.args.get('token'))
    channel_id = generateChannel_id()

    return channel_id

def message_remove(token, message_id):
    pass
    
def message_react(token, message_id, react_id):
    pass

def message_unreact(token, message_id, react_id):
    pass

def message_pin(token, message_id):
    pass

def message_unpin(token, message_id):
    pass