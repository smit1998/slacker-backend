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
def auth_login(email, password):
    pass
    
# when both of email and password are valid, return the valid token
def test_auth_login1():
    result = auth_login('ankitrai326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] = 23

# when the email is valid and password is invalid, print error message
def test_auth_login2():
    with.pytest.raises(ValueError):
        result = auth_login('ankitrai326@gmail.com', '2242')
        
# when the password is valid and email is invalid, print error message
def test_auth_login3(): 
    with.pytest.raises(ValueError):
        result = auth_login('1337memesgmail.com', '123243223') 
    
# when both of email and password are invalid, print error message
def test_auth_login4(): 
    with.pytest.raises(ValueError):
        result = auth_login('tisisatest.comgamil', '66666') 

# when both of email and password are valid, return the valid token
def test_auth_login5():
    result = auth_login('2199009762@qq.com', '123456789')
    assert result['token'] == 'right user'

# invalidating the authorized user 
def test_auth_logout1():
    auth_logout('easy easy easy')
    assert result == {}

# the token is invalide, nothing should be changed
def test_auth_logout2():
    auth_logout('really funny_123')
    assert result == {"email": 'ankitrai326@gmail.com', "password": '2242'}

# the token is invalide, nothing should be changed
def test_auth_logout3():
    auth_logout('what should i do')
    assert result == {'email': '1337memesgmail.com', 'password': '123243223'}

# the token is invalide, nothing should be changed
def test_auth_logout4():
    auth_logout('code1234code')
    assert result == {'email': 'tisisatest.comgamil', 'password': '66666'}

# invalidating the authorized user
def test_auth_logout5():
    auth_logout('right user')
    assert result == {}

# register failed because the email have already being used by others
def test_auth_register1():
    result = auth_register('AndyWei@gmail.com','314f42','Andrew','Wei')
    with.pytest.raises(ValueError):
        result = auth_register('bad_mail', '224232r4', 'Andy', 'Wei')
    assert result['token'] = 'team'
    
# register for a new user and return a new token
def test_auth_register2():
    result = auth_register('ededed12@gmail.com', '3453257B', 'Andy', 'Wei')
    with.pytest.raises(ValueError):
        auth_register('bad_mail', '224232r4', 'Andy', 'Wei')
    assert result['token'] == 'secret'
    
# show the details of current channel under the authorised user
def test_channel_details1():
    channel_id = channels_create('easy easy easy', 'a new channel', True)
    chann_id = channel_id['channel_id']
    result = channel_details('easy easy easy', chann_id)
    assert result == {'name': 'a new channel', 'owner_members': {['u_id': 1, 'name_first':'Andy', 'name_last': 'Wei']}, 
    'all_members': {['u_id': 1, 'name_first': 'Andy', 'name_last': 'Wei']}}

# when authorised user is not a member of this channel, print error message
def test_channel_details2():
    channel_id = channels_create('right user', 'a new channel', True)
    result = channel_id['channel_id']
    with.pytest.raises(ValueError):
        channel_details('hahaha', result)

# when channel doesn't exist, print error message
def test_channel_details3():
    channel_id = channels_create('right user', 'unknown group', True)
    result = channel_id['channel_id']
    with.pytest.raises(AccessError):
        channel_details('right user', result)

# add one user into the channel, and print the detail of this channel
def test_channel_details4():
    channel_id = channels_create('easy easy easy', 'a new channel', True) 
    u_id = channel_id['u_id']
    chann_id = channel_id['channel_id']
    channel_invite('easy easy easy', chann_id, u_id)
    result = channel_details('easy easy easy', chann_id)
    assert result == {'name': 'a new channel', 'owner_members': {['u_id': 1, 'name_first':'Andy', 'name_last': 'Wei']}, 
    'all_members': {['u_id': 1, 'name_first':'Andy', 'name_last': 'Wei'], ['u_id': 2, 'name_first':'Bill', 'name_last': 'Wei']} }
 
# failed to create a new private channel, because name is more than 20 characters long
def test_channels_create1():
    is_public = False
    with.pytest.raises(ValueError):
        channel_id = channel_create('right user', 'a new channel fanstic right right right right', False)
        
# return up to 50 messages between start and end under the authorized user
def test_channel_messages1():
    channel_id = channels_create('easy easy easy', 'a new channel', True)
    chann_id = channel_id['channel_id']
    messages = seach('easy easy easy', 'dummychoice')
    result = channel_messages('easy easy easy', chann_id, 1)
    assert result == {messages, 'start': 1, 'end': 50}
  
# valueError because of the start is greater than the total number of messages in the channel
def test_channel_messages2():
    channel_id = channels_create('easy easy easy', 'a new channel', True)
    chann_id = channel_id['channel_id']
    start = 10000 
    messages = seach('easy easy easy', 'dummychoice')
    if(start > len(message['messages']):
        with.pytest.raises(ValueError):
            channel_messages('easy easy easy', chann_id, start)    
       
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
    
# test message_send(......) function
def test_message_send1():
    token = 'easy easy easy'
    name = 'a new channel'
    channel_id = channels_create(token, name, True)
    qury_str = 'dummychoice'
    messages = search(token, query_str)
    message_send(token, channel_id, message)
    # i want to use function channel_messages(.....) to check the messages updated, but how ?

# test user_profile(....) function and return the valid user's information 
def test_user_profile1():
    token = 'easy easy easy' 
    u_id = 1
    information = user_profile(token, u_id)
    assert information == {'email': 'ankitrai326@gmail.com', 'name_first': 'Andy', 'name_last': 'Wei', 'handle_str': 'change'}
    
# when user is invalid, valueError would happen
def test_user_profile2():
    with.pytest.raises(ValueError):
        information = user_profile('easy easy easy', 34)
        
    
    
    
    
    
    
