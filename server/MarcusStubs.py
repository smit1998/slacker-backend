from json import dumps
from flask import Flask

app = Flask(__name__) 

SECRET = 'comp1531 project'

data = {
    'user_info': [],
    'channels': [],
    'message_info': []
}

ch_id = 0

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

def sendSuccess(data):
    return dumps(data)

@app.route('/channel/list', methods=['GET'])
def channels_list():
    data = getData()
    input_token = generateToken(request.args.get('token'))
    list_channels = {}
    for channel in data['channels']:
        for user in channel['all_members']:
            if (user == input_token):
                list_channels.append(channel)
    return sendSuccess(list_channels)

@app.route('/channel/listall', methods=['GET'])
def channels_listall():
    data = getData()
    input_token = generateToken(request.args.get('token'))
    list_all_channels = {}
    for channel in data['channels']:
        list_all_channels.append(channel)
    return sendSuccess(list_all_channels)

@app.route('/channel/create', methods=['POST'])
def channels_create():
    data = getData()
    input_token = generateToken(request.args.get('token'))
    channel_name = request.args.get('name')
    if (len(channel_name) > 20):
        raise ValueError(description = "invalid channel name")
    is_public = request.args.get('is_public')
    data['channels'].append({
        'channel_id': generateChannel_id(),
        'owner_members': input_token,
        'all_members': input_token,
        'name': channel_name,
        'is_public': True
    })
    return sendSuccess({
        'channel_id': data['channels'][-1]['channel_id']
    })

@app.route('/message/remove', methods=['DELETE'])
def message_remove():
    data = getData()
    input_token = generateToken(request.args.get('token'))
    input_message_id = request.args.get('message_id')
    for user in data['user_info']:
        if (user['permission'] == 'member'):
            raise AccessError('user is not admin or owner')
    flag_1 = False
    for message in data['message_info']:
        if (message['message_id'] == input_message_id):
            if (message['sender'] != input_token):
                raise AccessError('user is not sender')
            flag_1 = True
            del message
    if (flag_1 == False):
        raise ValueError('message does not exist')
    return sendSuccess({})

@app.route('/message/react', methods=['POST']) 
def message_react(token, message_id, react_id):
    data = getData()
    input_token = generateToken(request.args.get('token'))
    input_message_id = request.args.get('message_id')
    input_react_id = request.args.get('react_id')

@app.route('/message/unreact', methods=['POST'])
def message_unreact(token, message_id, react_id):
    pass

@app.route('/message/pin', methods=['POST'])
def message_pin(token, message_id):
    pass

@app.route('/message/unpin', methods=['POST'])
def message_unpin(token, message_id):
    pass