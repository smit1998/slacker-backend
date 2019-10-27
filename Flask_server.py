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
    return dumps(channel_leave(token, channel_id))
    
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


