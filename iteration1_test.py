'''
import pytest 
import re

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'     

def auth_login(email, password):
    token = " "
    assert type(token) == str
    if(re.search(regex, email)):
        try:
            pass
        except Exception:
            print("Got wrong e-mail")
    if(len(password) > 5):
        try:
            pass
        except Exception:
            print("Got wrong password")
    return token
    
def auth_logout(token):
    if(re.search(regex, token) and len(token) > 5):
        del(token)
        return token 
    return token 

def channel_details(token, channel_id):
'''    
   
# when both of email and password are valid, return the valid token
def test_auth_login1():
    token = 'easy easy easy'
    result = auth_login('ankitrai326@gmail.com', '224232r4')
    assert result == {'token': 'easy easy easy'}

# when the email is valid and password is invalid, print error message
def test_auth_login2(): 
    token = 'really funny_123'
    with.pytest.raises(ValueError):
        result = auth_login('ankitrai326@gmail.com', '2242')
        
# when the password is valid and email is invalid, print error message
def test_auth_login3(): 
    token = 'what should i do ?'
    with.pytest.raises(ValueError):
        result = auth_login('1337memesgmail.com', '123243223') 
    
# when both of email and password are invalid, print error message
def test_auth_login4(): 
    token = 'code1234code'
    with.pytest.raises(ValueError):
        result = auth_login('tisisatest.comgamil', '66666') 

# when both of email and password are valid, return the valid token
def test_auth_login5():
    token = 'right user'
    result = auth_login('2199009762@qq.com', '123456789')
    assert result == {'token': 'right user'}

# invalidating the authorized user 
def test_auth_logout1():
    result = 'easy easy easy'
    auth_logout(result)
    assert result == {}

# the token is invalide, nothing should be changed
def test_auth_logout2():
    result = 'really funny_123'
    auth_logout(result)
    assert result == {"email": 'ankitrai326@gmail.com', "password": '2242'}

# the token is invalide, nothing should be changed
def test_auth_logout3():
    result = 'what should i do ?'
    auth_logout(result)
    assert result == {'email': '1337memesgmail.com', 'password': '123243223'}

# the token is invalide, nothing should be changed
def test_auth_logout4():
    result = 'code1234code'
    auth_logout(result)
    assert result == {'email': 'tisisatest.comgamil', 'password': '66666'}

# invalidating the authorized user
def test_auth_logout5():
    result = 'right user'
    auth_logout(result)
    assert result == {}

# register failed because the email have already being used by others
def test_auth_register1():
    with.pytest.raises(ValueError):
        result = auth_register('ankitrai326@gmail.com', '224232r4', 'Andy', 'Wei')

# register for a new user and return a new token
def test_auth_register2():
    token = 'random'
    result = auth_register('ededed12@gmail.com', '3453257B', 'Andy', 'Wei')
    assert result == {'token': 'random'}
    
# show the details of current channel under the authorised user
def test_channel_details1():
    token = 'easy easy easy'
    name = "a new channel"
    channel_id = channels_create(token, name, True)
    result = channel_details(token, channel_id)
    assert result == {'name': 'a new channel', 'owner_members': {['u_id': 1, 'name_first':'Andy', 'name_last': 'Wei']}, 
    'all_members': {['u_id': 1, 'name_first': 'Andy', 'name_last': 'Wei']}}

# when authorised user is not a member of this channel, print error message
def test_channel_details2():
    token = 'right user'
    name = 'a new channel' 
    channel_id = channels_create(token, name, True)
    with.pytest.raises(ValueError):
        result = channel_details(token, channel_id)

# when channel doesn't exist, print error message
def test_channel_details3():
    token = 'right user'
    name = 'unknown group'
    channel_id = 66
    with.pytest.raises(AccessError):
       result = channel_details(token, channel_id)

# add one user into the channel, and print the detail of this channel
def test_channel_details4():
    token = 'easy easy easy'
    name = "a new channel"
    channel_id = channels_create(token, name, True) 
    u_id = 2
    channel_invite(token, channel_id, u_id)
    result = channel_details(token, channel_id)
    assert result == {'name': 'a new channel', 'owner_members': {['u_id': 1, 'name_first':'Andy', 'name_last': 'Wei']}, 
    'all_members':{['u_id': 1, 'name_first':'Andy', 'name_last': 'Wei'], ['u_id': 2, 'name_first':'Bill', 'name_last': 'Wei']} }
 
# failed to create a new private channel, because name is more than 20 characters long
def test_channels_create1():
    token = 'right user'
    name = 'a new channel fanstic right right right right'
    is_public = False
    with.pytest.raises(ValueError):
        channel_id = channel_create(token, name, False)
        
# return up to 50 messages between start and end under the authorized user
def test_channel_messages1():
    token = 'easy easy easy'
    name = 'a new channel'
    channel_id = channels_create(token, name, True)
    start = 1 
    query_str = 'dummychoice'
    messages = seach(token, query_str)
    result = channel_messages(token, channel_id, start)
    assert result == {messages, 'start': 1, 'end': 50}
  
# valueError because of the start is greater than the total number of messages in the channel
def test_channel_messages2():
    token = 'easy easy easy'
    name = 'a new channel'
    channel_id = channels_create(token, name, True)
    start = 10000 
    query_str = 'dummychoice'
    messages = seach(token, query_str)
    if(start > messages):
        with.pytest.raises(ValueError):
            result = channel_messages(token, channel_id, start)    
       
# valueError because of the channel doesn't exist
def test_channel_messages3():
    token = 'easy easy easy'
    start = 1
    channel_id = 4
    query_str = 'dummychoice'
    messages = seach(token, query_str)
    with.pytest.raises(ValueError):
        result = channel_messages(token, channel_id, start)
 
# valueError because of the authorized user is not a number of this current channel
def test_channel_messages4():
    token = 'right user'
    name = 'a new channel'
    start = 5
    with.pytest.raises(AccessError):
       channel_id = channels_create(token, name, True)
    
# 
    
    
    
    
