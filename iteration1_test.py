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
   
# when both of email and password are valid
def test_auth_login1():
    token = 'easy easy easy'
    result = auth_login('ankitrai326@gmail.com', '224232r4')
    assert result == {'token': 'easy easy easy'}

# when the email is valid and password is invalid
def test_auth_login2(): 
    token = 'really funny_123'
    result = auth_login('ankitrai326@gmail.com', '2242')
    with.pytest.raises(ValueError):
        print ("Invalid user")   
        
# when the password is valid and email is invalid
def test_auth_login3(): 
    token = 'what should i do ?'
    result = auth_login('1337memesgmail.com', '123243223') 
    with.pytest.raises(ValueError):
        print ("Invalid user")   
    
# when both of email and password are invalid
def test_auth_login4(): 
    token = 'code1234code'
    result = auth_login('tisisatest.comgamil', '66666')
    with.pytest.raises(ValueError):
        print ("Invalid user")   

def test_auth_login5():
    token = 'right user'
    result = auth_login('2199009762@qq.com', '123456789')
    assert result == {'token': 'easy easy easy'}

# invalidating the valide token
def test_auth_logout1():
    result = 'easy easy easy'
    auth_logout(result)
    assert result == {}

# the token is invalide, so does nothing
def test_auth_logout2():
    result = 'really funny_123'
    auth_logout(result)
    assert result == {"email": 'ankitrai326@gmail.com', "password": '2242'}

# the token is invalide, so does nothing 
def test_auth_logout3():
    result = 'what should i do ?'
    auth_logout(result)
    assert result == {'email': '1337memesgmail.com', 'password': '123243223'}

# the token is invalide, so does nothing 
def test_auth_logout4():
    result = 'code1234code'
    auth_logout(result)
    assert result == {'email': 'tisisatest.comgamil', 'password': '66666'}

def test_auth_logout5():
    result = 'right user'
    auth_logout(result)
    assert result == {}

def auth_register_test1():
    result = auth_register('ankitrai326@gmail.com', '224232r4', 'Andy', 'Wei'}
    assert result == {'token': 'easy easy easy'}
    
    
# the test of channel_details
def test_channel_details1():
    token = 'easy easy easy'
    name = "a new channel"
    channel_id = channels_create(token, name, True)
    result = channel_details(token, channel_id)
    assert result == {'name': 'a new channel', 'owner_members': 'Andy Wei', 'all_members': 'Andy Wei'}

def test_channel_details2():
    token = 'right user'
    name = 'a new channel' 
    channel_id = channels_create(token, name, True)
    result = channel_details(token, channel_id)
    with.pytest.raises(ValueError):
        print('Authorised user is not a member of this channel')
        
def test_channel_details3():
    token = 'right user'
    name = 'unknown group'
    channel_id = 66
    result = channel_details(token, channel_id)
    with.pytest.raises(ValueError):
        print('Channel_id is invalid')
        
 
def test
        
 
        
    
