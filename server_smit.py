@APP.route('/user/profile/setname', methods = ['PUT'])
def user_profile_setname():
    token = request.form.get('token')
    first = request.form.get('name_first')
    last = request.form.get('name_last')

    result = user_profile_setname(token, first, last)
    return dumps({})

@APP.route('/user/profile/setemail', methods = ['PUT'])
def user_profile_setemail():

    token = request.form.get('token')
    new_email = request.form.get('email')

    store_results = user_profile_setemail(token, new_email)

    return dumps({})

@APP.route('/user/profile/sethandle', methods = ['PUT'])
def user_profile_sethandle(token, handle_str):
    
    token = request.form.get('token')
    new_handle_str = request.form.get('handle_str')
    
    results = user_profile_sethandle(token, new_handle_str)
    return dumps({})

@APP.route('/search', methods = ['GET'])
def search():
    token = request.form.get('token')
    q_str = request.form.get('query_str')

    search_results = search(token, q_str)

    return dumps({})

@APP.route('/admin/userpermission/change', methods = ['POST'])
def admin_userpermission_change():
    
    token = request.form.get('token')
    u_id = request.form.get('u_id')
    p_id = request.form.get('permission')

    permission_results = admin_userpermission_change(token, u_id, p_id)

    return dumps({})

    