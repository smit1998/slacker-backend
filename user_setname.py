import pytest
import re
from json import dumps
from flask import Flask

APP = Flask(__name__)

#need to complete this funcition
def get_U_id(token):    
    return u_id


@APP.route('/user/profile/setname', methods = ['PUT'])
def user_profile_setname():
    
    token = request.form.get('token')
    first = request.form.get('name_first')
    last = request.form.get('name_last')

    if token == None:
        raise ValueError("NULL token")

           
    if len(first) > 50:
       raise ValueError("name_first greater than 50 characters.")
    if len(first) < 1:
        raise ValueError("name_first is less than 1 character.")
    if len(last) > 50:
        raise ValueError("name_last greater than 50 characters.")
    if len(last) < 1:
        raise ValueError("name_last less than 1 character.")
    
    #change the first and last names
    # how to get the u_id with the token
    #need to change this
    
    user_id = get_U_id(token)

    for user in data['user_info']:
        if user['u_id'] == user_id:
            user['name_first'] = first
            user['name_last'] = last
    
    return dumps({ })


############################################################################################
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
      
# Define a function for 
# for validating an Email 
def check(email):  
  
    # pass the regualar expression 
    # and the string in search() method 
    if(re.search(regex,email)):  
        return True  
          
    else:  
        return False

@APP.route('/user/profile/setemail', methods = ['PUT'])
def user_profile_setemail():

    token = request.form.get('token')
    new_email = request.form.get('email')
    
    if check(new_email) == False:
        raise ValueError("not a valid email address")
    
    #token stuff left to do

    for user in data['user_info']:
        if user['email'] == new_email:
            raise ValueError("Email address already being used")

    user_id = get_U_id(token):
    
    for users in data['user_info']:
            if users['u_id'] == user_id:
                users['email'] = new_email

    return dumps({ })

##############################################################################################################################################

@APP.route('/user/profile/sethandle', methods = ['PUT'])
def user_profile_sethandle(token, handle_str):
    token = request.form.get('token')
    new_handle_str = request.form.get('handle_str')

    user_id = get_U_id(token)

    if len(new_handle_str) < 3 or len(new_handle_str) > 20:
        raise ValueError
    
    for user in data['user_info']:
        if user['handle_str'] == new_handle_str:
            raise ValueError("Handle_str already in use")

    for u in data['user_info']:
        if u['u_id'] == user_id::
            u['handle_str'] = new_handle_str

    return dumps({ })         

##############################################################################################################################################

def search(token, query_str):
    

##############################################################################################################################################
@APP.route('/admin/userpermission/change', methods = ['POST'])
def admin_userpermission_change():

    token = request.form.get('token')
    u_id = request.form.get('u_id')
    p_id = request.form.get('permission')

    if p_id != 'owner':
        if p_id != 'admin':
            if p_id != 'member':
                raise ValueError("permission_id is not a valid permission value")
            
    for user in data['user_info']:
        if u_id == user['u_id']:
            user['permission'] = p_id
    
    return dumps({ })
    
    



