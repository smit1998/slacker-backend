import pytest 
import time
'''
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
    
def auth_logout(token):
    pass
    
def channel_invite(token, channel_id, u_id):
    pass
   
def channel_details(token, channel_id):
    pass

def channel_messages(token, channel_id. start):
    pass
    
def message_send(token, channel_id, message):
    pass

def message_sendlater(token, channel_id, message, time_sent):
    pass
    
def user_profile(token, u_id):
    pass
          
# when both of email and password are valid, return the valid token
def test_auth_login1():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 23

# when the email is valid and password is invalid, print error message
def test_auth_login2():
    with pytest.raises(ValueError):
        auth_login('andyWei326@gmail.com', '2242')
        
# when the password is valid and email is invalid, print error message
def test_auth_login3(): 
    with pytest.raises(ValueError):
        auth_login('1337memesgmail.com', '123243223') 
    
# when both of email and password are invalid, print error message
def test_auth_login4(): 
    with pytest.raises(ValueError):
        auth_login('tisisatest.comgamil', '66666') 

# when both of email and password are valid, return the valid token
def test_auth_login5():
    result = auth_login('2199009762@qq.com', '123456q789')
    assert result['token'] == 'right user'
    assert result['u_id'] == 66

# invalidating the authorized user 
def test_auth_logout1():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 23
    auth_logout('easy easy easy')
    assert result == {}

# the token is invalide, nothing should be changed
def test_auth_logout2():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 23
    auth_logout('really funny_123')
    assert result == {"u_id": 23, "token": 'easy easy easy'}

# the token is invalide, nothing should be changed
def test_auth_logout3():
    result = auth_login('2199009762@qq.com', '123456q789')
    assert result['token'] == 'right user'
    assert result['u_id'] == 66
    auth_logout('what should i do')
    assert result == {'u_id': 66, 'token': 'right user'}
        
# show the details of current channel under the authorised user, and also name is public
def test_channel_details1():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 23
    basic_info = user_profile('easy easy easy', 23)
    assert basic_info['name_first'] == 'Andy'
    assert basic_info['name_last'] == 'Wei'
    channel_id = channels_create('easy easy easy', 'a new channel', True)
    chann_id = channel_id['channel_id'] 
    result = channel_details('easy easy easy', chann_id)
    assert result == {'name': 'a new channel', 'owner_members': [{'u_id': 23, 'name_first': 'Andy', 'name_last': 'Wei'}], 
    'all_members': [{'u_id': 23, 'name_first': 'Andy', 'name_last': 'Wei'}]}

# show the details of current channel under the authorised user, and also name is private 
def test_channel_details2():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 23
    basic_info = user_profile('easy easy easy', 23)
    assert basic_info['name_first'] == 'Andy'
    assert basic_info['name_last'] == 'Wei'
    channel_id = channels_create('easy easy easy', 'a new channel', False)
    chann_id = channel_id['channel_id'] 
    result = channel_details('easy easy easy', chann_id)
    assert result == {'name': 'a new channel', 'owner_members': [{'u_id': 23, 'name_first': 'Andy', 'name_last': 'Wei'}], 
    'all_members': [{'u_id': 23, 'name_first': 'Andy', 'name_last': 'Wei'}]}

# when authorised user is not a member of this channel, just ValueError message
def test_channel_details3():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    result = auth_login('2199009762@qq.com', '123456q789')
    assert result['token'] == 'right user'
    channel_id = channels_create('right user' 'funny_channel', True)
    result = channel_id['channel_id']
    with pytest.raises(ValueError):
        channel_details('easy easy easy', result)

# when channel doesn't exist, print error message
def test_channel_details4():
    result = auth_login('2199009762@qq.com', '123456q789')
    assert result['token'] == 'right user'
    with pytest.raises(AccessError):
        channel_details('right user', 29)

# add one user into the channel, and print the detail of this channel
def test_channel_details5():
    result = auth_login('2199009762@qq.com', '123456q789')
    assert result['token'] == 'right user'
    assert result['u_id'] == 66
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 23
    channel_id = channels_create('easy easy easy', 'a new channel', True) 
    chann_id = channel_id['channel_id']
    channel_invite('right user', chann_id, 66)
    basic_info = user_profile('right user', 66)
    assert basic_info['name_first'] == 'Jack'
    assert basic_info['name_last'] == 'Ma'
    result = channel_details('easy easy easy', chann_id)
    assert result == {'name': 'a new channel', 'owner_members': [{'u_id': 23, 'name_first':'Andy', 'name_last': 'Wei']}, 
    'all_members': [{'u_id': 23, 'name_first':'Andy', 'name_last': 'Wei'}, {'u_id': 66, 'name_first':'Jack', 'name_last': 'Ma'}]}
        
# return up to 50 messages between start and end under the authorized user
def test_channel_messages1():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    channel_id = channels_create('easy easy easy', 'a new channel', True)
    chann_id = channel_id['channel_id']
    # question on the 'query_str' ? ? ? ?
    messages = search('easy easy easy', 'dummychoice')
    result = channel_messages('easy easy easy', chann_id, 0)
    assert result == {'messages': [messages], 'start': 0, 'end': 49}
  
# valueError because of the start is greater than the total number of messages in the channel
def test_channel_messages2():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    channel_id = channels_create('easy easy easy', 'a new channel', True)
    chann_id = channel_id['channel_id']
    start = 10000 
    message = search('easy easy easy', 'dummychoice')
    #if the start is greater than the total message ? ? ? ? 
    if(start > len(message['message']):
        with pytest.raises(ValueError):
            channel_messages('easy easy easy', chann_id, start)    
       
# valueError because of the channel doesn't exist
def test_channel_messages3():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    result = auth_login('2199009762@qq.com', '123456q789')
    assert result['token'] == 'right user'
    channel_id01 = channels_create('easy easy easy', 'a new channel', True)
    chann_id01 = channel_id01['channel_id']
    channel_id02 = channels_create('right user', 'another channel', True)
    chann_id02 = channel_id02['channel_id']
    with pytest.raises(ValueError):
        channel_messages('right user', chann_id01, 0)
 
# valueError because of the authorized user is not a number of this current channel
def test_channel_messages4():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    result = auth_login('2199009762@qq.com', '123456q789')
    assert result['token'] == 'right user'
    channel_id01 = channels_create('easy easy easy', 'a new channel', True)
    chann_id01 = channel_id01['channel_id']
    with pytest.raises(AccessError):
        channels_create('a right user', 'a new channel', True)
    
# when message is more than 1000 characters, just ValueError 
def test_message_send1():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    channel_id = channels_create('easy easy easy', 'a new channel', True)
    chann_id = channel_id['channel_id']
    messages = search('easy easy easy', 'dummychoice')
    message = messages['message']
    if(len(message) > 1000):
        with pytest.raises(ValueError):
            message_send('easy easy easy', chann_id, message)

# send the meessage to another private channel of name 
def test_message_send2():
    result = auth_login('andrewzhu@gmail.com', '66wz3#d')
    assert result['token'] == 'good job'
    channel_id = channels_create('good job', 'greate channel', False)
    chann_id = channel_id['channel_id']
    messages = search('good job', 'hahahahaha')
    message = messages['message']
    message_send('good job', chann_id, message)
    
# if the channel doesn't exist, just ValueError
def test_message_sendlater1():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    channel_id = channels_create('easy easy easy', 'a new channel', True)
    chann_id = channel_id['channel_id']
    today = datetime.datatime(2019,10,6,18,54,36,280121)
    messages = search('easy easy easy', 'dummychoice')
    message = messages['message']
    with pytest.raises(ValueError):
        message_sendlater('easy easy easy','wrong channel', message, today)

# if the message is more than 1000 characters, then just ValueError
def test_message_sendlater2():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    channel_id = channels_create('easy easy easy', 'a new channel', True)
    chann_id = channel_id['channel_id']
    today = datetime.datatime(2020,3,1,18,54,36,280121)
    messages = search('easy easy easy', 'dummychoice')
    message = messages['message']
    if(len(message) > 1000):
        with pytest.raises(ValueError):
            message_sendlater('easy easy easy', chann_id, message, today)
            
# if the time sent is a time in the past, need to be considered as a valueError
def test_message_sendlater3():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    channel_id = channels_create('easy easy easy', 'a new channel', True)
    chann_id = channel_id['channel_id']
    today = datetime.datatime(2018,3,1,18,54,36,280121)
    messages = search('easy easy easy', 'dummychoice')
    message = messages['message']
    with pytest.raises(ValueError):
            message_sendlater('easy easy easy', chann_id, message, today)

# test user_profile(....) function and return the valid user's information 
def test_user_profile1():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 23
    basic_info = user_profile('easy easy easy', 23)
    # what's the handle_str ? ? ? ?
    assert basic_info == {'email': 'andyWei326@gmail.com', 'name_first': 'Andy', 'name_last': 'Wei', 'handle_str': 'change'}
    
# when user is invalid, valueError would happen
def test_user_profile2():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 23
    with pytest.raises(ValueError):
        user_profile('easy easy easy', 34)
       

    
    
    
    
    
