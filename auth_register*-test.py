'''
import pytest 
import re

def auth_register(email,password,name_first,name_last): 
    
    





    #dictionarys = have no sence of order a clump of key value pairs (store data that 
    #makes sense to look up (kind of like structs)
    #userData = { 
     #'name' : 'sally', 
     #'age' : 18, 
     #'height' : '186cm',
   # }
    #userData['height'] = '187cm'
    #print(userData) 

#this tests if the email is already used by another user

        
        
        
'''        
from Error import AccessError       
import pytest 
import re 


  
def test_auth_register_valid_token():  
    register_details = auth_register('memes@gmail.com', 'dankpassword121', 'Cameron', 'Burrell')
    token = register_details['token']
    #user_id = register_details.get['u_id']
    assert validToken(token) == True
    #assert user_id == True
    
  

def test_auth_register_correctemail(): 
'''
    register_details = auth_register(('hello.com', 'stronkpassword123', 'John', 'Super')
    user_id = register_details.get['u_id']
    token = register_details['token']
    assert user_id == False
    assert validToken(token) == False
'''
    with pytest.raises(ValueError):
        auth_register('hello.com', 'stronkpassword123', 'John', 'Super')
    
    
def test_auth_register_emailused():
    auth_register('ankitrai326@gmail.com', '224232r4', 'Andy', 'Wei')
    with pytest.raises(ValueError):
        auth_register('ankitrai326@gmail.com', '224232r4', 'Andy', 'Wei')
   
def test_auth_register_password_length():
    '''
    register_details = auth_register('correctemail@gmail.com', '123', 'ShortN', 'Sweet')
    user_id = register_details.get['u_id']
    token = register_details['token']
    assert user_id == False
    assert validToken(token) == False
    '''
    with pytest.raises(ValueError):
        auth_register('correctemail@gmail.com', '123', 'ShortN', 'Sweet')
    
   

def test_auth_register_first_name(): 
'''
    register_details = auth_register('doyourfingershurt@hotmail.com', '324sf223', 'sdfsvsdbgsdvsvbnsdvnsdovosdnvodsnvosdnvodsvnsdvnsdvfwj', 'LongAssFirstName')
    user_id = register_details.get['u_id']
    token = register_details['token']
    assert user_id == False
    assert validToken(token) == False
'''
    with pytest.raises(ValueError):
        auth_register('doyourfingershurt@hotmail.com', '324sf223', 'sdfsvsdbgsdvsvbnsdvnsdovosdnvodsnvosdnvodsvnsdvnsdvfwj', 'LongAssFirstName')
    
   

def test_auth_register_last_name(): 
'''
    register_details = auth_register('donthateme@gmail.com', 'ihavegivenup232e', 'Joe', 'tehrhdbfsmohteojfblkdnfgojdvfjgbfgodbdljhpobfhfdjhpdrsdsvr') 
    user_id = register_details.get['u_id']
    token = register_details['token']
    assert user_id == False
    assert validToken(token) == False
'''
    with pytest.raises(ValueError):
        auth_register('donthateme@gmail.com', 'ihavegivenup232e', 'Joe', 'tehrhdbfsmohteojfblkdnfgojdvfjgbfgodbdljhpobfhfdjhpdrsdsvr') 
        
 
    
'''
def test_auth_passwordrest_request_registered_user():
    register_details_one = auth_register('memes@gmail.com', 'dankpassword121', 'Cameron', 'Burrell')
    user_id_one = register_details_one.get['u_id']
    assert user_id_one == True
    
    register_details_two = auth_register('random@gmail.com', 'dankpassword121', 'Cameron', 'Burrell')
    user_id_two = register_details_one.get['u_id']
    assert user_id_two = False
   
    auth_passwordreset_request('memes@gmail.com) 
   
    with pytest.raises(ValueError): 
        auth_passwordreset_request('random@gmail.com')
    
def test_auth_passwordreset_reset(): 
    '''

def test_channel_leave_channel_not_exist(): 
    register_details = auth_register('memes@gmail.com', 'dankpassword121', 'Cameron', 'Burrell')
    token = register_details['token']
    name = 'super room' 
    unexisiting_channel = 'dsvfswvdsgrenvkscn dsknfkewbvkabdwoghodn l' 
    channels_create_dict = channels_create(token, name, True)
    
    channelID = channels_create_dict['channel_id']
    
    channel_leave(token, channelID)
    channel_join(token, channelID)
    
    with pytest.raises(ValueError): 
        channel_leave(token, unexisiting_channel)

def test_channel_join_channel_not_exisit(): 
    register_details = auth_register('1337@gmail.com', '4253214', 'Yaba', 'Dabadoo')
    token = register_details['token']
    name = 'random channel' 
    unexisiting_channel= 'hi this channel does not exist'
    channels_create_dict = channels_create(token, name, True)
   
    channelID = channels_create_dict['channel_id']
    
    channel_join(token, channelID)
    channel_leave(token, channelID) 
    
    with pytest.raises(ValueError): 
        channel_join(token, unexisiting_channel)
        
        
def test_channel_join_private_channel_one(): 
    register_details = auth_register('auto@gmail.com', '123456', 'the', 'dude')
    token = register_details['token'] 
    user_id = register_details['u_id']
    name = 'admin room' 
    channels_create_dict = channels_create(token, name, False)
    
    channelID = channels_create_dict['channel_id']
    channel_removeowner(token, channelID, user_id)
    channel_leave(token, channelID)
    
    with pytest.raises(ValueError): 
        channel_join(token, channelID)
    
def test_channel_join_private_channel_two(): 
    register_details = auth_register('good@gmail.com', '1234567', 'happy', 'guy')
    token = register_details['token'] 
    user_id = register_details['u_id']
    name = 'secret room' 
    channels_create_dict = channels_create(token, name, False)
    
    channelID = channels_create_dict['channel_id']
    
    channel_removeowner(token, channelID, user_id)
    channel_leave(token, channelID)
    channel_invite(token, channelID, user_id) 
    channel_join(token, channelID)
    channel_leave(token, channelID) 
    
    with pytest.raises(ValueError):
        channel_join(token, channelID)

def test_channel_addowner_id_not_exist(): 
    register_details = auth_register('niceemail@gmail.com', '12345678', 'nice', 'person')
    token = register_details['token'] 
    user_id = register_details['u_id']
    name = 'god channel' 
    unexisiting_channel = 'does not exist' 
    channels_create_dict = channels_create(token, name, False)
    
    channelID = channels_create_dict['channel_id']
    
    channel_addowner(token, channelID, user_id)
    channel_removeowner(token, channelID, user_id) 
    
    with pytest.raises(ValueError): 
        channel_addowner(token, unexisiting_channel, user_id)

def test_channel_addowner_user_already_owner(): 
    u_id1, token1 = auth_register('nicenicenice@gmail.com', '12323452', 'good', 'smart')
    u_id2, token2 = auth_register('niceandcorrect@gmail.com', '12345454', 'hi', 'man') 
    channels_create_dict = channels_create(token1, 'My channel', False)
    channelID = channels_create_dict['channel_id'] 
    
    channel_addowner(token1, channelID, u_id2) 
    
    with pytest.raises(ValueError): 
        channel_addowner(token1, channelID, u_id1)

def test_channel_addowner_non_owners(): 
    u_id1, token1 = auth_register('great@gmail.com', '12323452', 'goodness', 'me')
    u_id2, token2 = auth_register('niceandcorrect1@gmail.com', '123454542', 'hello', 'guy') 
    channels_create_dict = channels_create(token1, 'My channel', False)
    channelID = channels_create_dict['channel_id'] 
    
    channel_addowner(token1, channelID, u_id2) 
    channel_removeowner(token1, channelID, u_id2)
    
    with pytest.raises(AccessError, match=r"*"):
        channel_addowner(token2, channelID, u_id2) #u_id2 does not have to power to make themselfs owner of the channel (assume the token

def test_channel_removeowner_id_not_exist(): 
    u_id1, token1 = auth_register('best@gmail.com', '123dsf8', 'correct', 'girl')
    u_id2, token2 = auth_register('niceandcorrect1@gmail.com', '123454542', 'hello', 'guy') 
    channels_create_dict = channels_create(token1, 'My channel', False)
    channelID = channels_create_dict['channel_id']
    name = 'god channel' 
    unexisiting_channel = 'random name that is not a channel' 
    channels_create_dict = channels_create(token1, name, False)
    
    channelID = channels_create_dict['channel_id']
    
    channel_addowner(token1, channelID, u_id2)
    channel_removeowner(token1, channelID, u_id2) 
    
    with pytest.raises(ValueError): 
        channel_addowner(token1, unexisiting_channel, u_id2)

def test
