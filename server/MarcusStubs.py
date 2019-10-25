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
    return

@app.route('/channel/listall', methods=['GET'])
def channels_listall():
    list_all_channels = {}
    for channel in data['channels']:
        list_all_channels.append(channel['channel_id'])
    return sendSuccess(allChannels)

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