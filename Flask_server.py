@APP.route('/auth/passwordreset/request', methods=['POST'])
def passwordreset_request():
    email = request.form.get('email')
    auth_passwordreset_request(email)
    return dumps({})

@APP.route('/auth/passwordreset/reset', methods=['POST'])
def passwordreset_reset():
    reset_code = request.form.get('reset_code')
    new_password= request.form.get('new_password')
    passwordreset_reset(reset_code, new_password)
    return dumps({})

@APP.route('/channel/leave', methods=['POST'])
def leave_channel():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    result = channel_leave(token, channel_id)
    return dumps(result)
    
@APP.route('/channel/join', methods=['POST'])
def join_channel():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    channel_join(token, channel_id)
    return dumps({})

@APP.route('/channel/addowner', methods=['POST'])
def addowner_channel():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    user_id = request.form.get('u_id')
    addowners(token, channel_id, user_id)
    return dumps({})

@APP.route('/channel/removeowner', methods=['POST'])
def removeowner_channel():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    user_id = request.form.get('u_id')
    removeowners(token, channel_id, user_id)
    return dumps({})

@APP.route('/channels/list', methods=['GET'])
def listChannels():
    token = request.args.get('token')
    result = channellist(token)
    return dumps(result)

@APP.route('/channels/listall', methods=['GET'])
def listallChannels():
    token = request.args.get('token')
    result = channellistall(token)
    return dumps(result)
  
@APP.route('/channels/create', methods=['POST'])
def create():
    token = request.form.get('token')
    name = request.form.get('name')
    is_public = request.form.get('is_public')
    result = channelcreate(token, name, is_public)
    return dumps(result)

@APP.route('/message/remove', methods=['DELETE'])
def removeMessage():
    token = request.args.get('token')
    message_id = request.args.get('message_id')
    message_remove(token, message_id)
    return dumps({})

@APP.route('/message/edit', methods=['PUT'])
def edit():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    message = request.form.get('message')
    message_edit(token, message_id, message)
    return dumps({})

@APP.route('/message/react', methods=['POST'])
def react():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    react_id = request.form.get('react_id')
    message_react(token, message_id, react_id)
    return dumps({})

@APP.route('/message/unreact', methods=['POST'])
def unreact():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    react_id = request.form.get('react_id')
    message_unreact(token, message_id, react_id)
    return dumps({})

@APP.route('/message/pinn', methods=['POST'])
def pin():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    message_pin(token, message_id)
    return dumps({})

@APP.route('/message/unpin', methods=['POST'])
def unpin():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    message_unpin(token, message_id)
    return dumps({})
