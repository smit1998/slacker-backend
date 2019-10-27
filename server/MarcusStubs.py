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
    input_token = generateToken(request.form.get('token'))
    channel_name = request.form.get('name')
    if (len(channel_name) > 20):
        raise ValueError(description = "invalid channel name")
    is_public = request.form.get('is_public')
    data['channels'].append({
        'channel_id': generateChannel_id(),
        'owner_members': input_token,
        'admin_members': input_token,
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
    input_token = generateToken(request.form.get('token'))
    input_message_id = request.form.get('message_id')
    flag_1 = False # Checks for permission to pin.
    for channel in data['channels']:
        for user in channel['owner_members']:
            if (user == input_token):
                flag_1 = True
        for user in channel['admin_members']:
            if (user == input_token):
                flag_1 = True
    if (flag_1 = False):
        raise AccessError('user is not admin or owner')
    flag_2 = False
    for message in data['message_info']:
        if (message['message_id'] == input_message_id):
            if (message['sender'] != input_token):
                raise AccessError('user is not sender')
            flag_2 = True
            del message
    if (flag_2 == False):
        raise ValueError('message does not exist')
    return sendSuccess({})

@app.route('/message/react', methods=['POST']) 
def message_react():
    data = getData()
    input_token = generateToken(request.form.get('token'))
    input_message_id = request.form.get('message_id')
    input_react_id = request.form.get('react_id')
    if (input_react_id != 1):
        raise ValueError('invalid react')
    flag_1 = False
    for message in data['message_info']:
        if (message['message_id'] == input_message_id):
            if (message['react_id'] == input_react_id):
                raise ValueError('message already has an active react')
            flag_1 = True
            message['react_id'] == input_react_id
    if (flag_1 == False):
        raise ValueError('message does not exist')
    return sendSuccess({})

@app.route('/message/unreact', methods=['POST'])
def message_unreact():
    data = getData()
    input_token = generateToken(request.form.get('token'))
    input_message_id = request.form.get('message_id')
    input_react_id = request.form.get('react_id')
    if (input_react_id != 0):
        raise ValueError('invalid react')
    flag_1 = False
    for message in data['message_info']:
        if (message['message_id'] == input_message_id):
            if (message['react_id'] == input_react_id):
                raise ValueError('message does not contain an active react')
            flag_1 = True
            message['react_id'] == input_react_id
    if (flag_1 == False):
        raise ValueError('message does not exist')
    return sendSuccess({})

@app.route('/message/pin', methods=['POST'])
def message_pin():
    data = getData()
    input_token = generateToken(request.form.get('token'))
    flag_1 = False # Checks for permission to pin.
    for channel in data['channels']:
        for user in channel['owner_members']:
            if (user == input_token):
                flag_1 = True
        for user in channel['admin_members']:
            if (user == input_token):
                flag_1 = True
    if (flag_1 = False):
        raise ValueError('user is not admin or owner')
    input_message_id = request.form.get('message_id')
    flag_2 = False # Checks if message exists.
    flag_3 = False # Checks if the user is a member of the channel that the message is within.
    for message in data['message_info']:
        if (message['message_id'] == input_message_id):
            for channel in data['channels']:
                if (channel['channel_id'] == message['channel_id']):
                    for user in channel['all_members']:
                        if (user == input_token):
                            flag_3 = True
            if (flag_3 == False):
                raise AccessError('user is not a member of the channel that the message is within')
            if (message['is_pinned'] == True):
                raise ValueError('message already pinned')
            flag_2 = True
            message['is_pinned'] == True
    if (flag_2 == False):
        raise ValueError('message does not exist')
    return sendSuccess({})

@app.route('/message/unpin', methods=['POST'])
def message_unpin():
    data = getData()
    input_token = generateToken(request.form.get('token'))
    flag_1 = False # Checks for permission to unpin.
    for channel in data['channels']:
        for user in channel['owner_members']:
            if (user == input_token):
                flag_1 = True
        for user in channel['admin_members']:
            if (user == input_token):
                flag_1 = True
    if (flag_1 = False):
        raise ValueError('user is not admin or owner')
    input_message_id = request.form.get('message_id')
    flag_2 = False # Checks if message exists.
    flag_3 = False # Checks if the user is a member of the channel that the message is within.
    for message in data['message_info']:
        if (message['message_id'] == input_message_id):
            for channel in data['channels']:
                if (channel['channel_id'] == message['channel_id']):
                    for user in channel['all_members']:
                        if (user == input_token):
                            flag_3 = True
            if (flag_3 == False):
                raise AccessError('user is not a member of the channel that the message is within')
            if (message['is_pinned'] == False):
                raise ValueError('message already unpinned')
            flag_2 = True
            message['is_pinned'] == False
    if (flag_2 == False):
        raise ValueError('message does not exist')
    return sendSuccess({})

@app.route('/message/edit', methods=['PUT'])
def message_edit():
    data = getData()
    input_token = generateToken(request.form.get('token'))
    input_message_id = request.form.get('message_id')
    input_message = request.form.get('message')
    flag_1 = False # Checks for permission to unpin.
    for channel in data['channels']:
        for user in channel['owner_members']:
            if (user == input_token):
                flag_1 = True
        for user in channel['admin_members']:
            if (user == input_token):
                flag_1 = True
    if (flag_1 = False):
        raise ValueError('user is not admin or owner')
    for i in data['message_info']:
        if (i['message_id'] == input_message_id):
            if (i['sender'] != input_token):
                raise AccessError('user did not send the message')
            i['message'] = input_message
    return sendSuccess