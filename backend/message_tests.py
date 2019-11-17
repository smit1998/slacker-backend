import pytest
import backend.backend_functions as BF

# when message is more than 1000 characters, just ValueError 
def test_message_send_many_characters():
    BF.data['user_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    result = BF.channels_create(authRegisterDic['token'], 'good team', True)
    message = 'hello' * 1000 
    with pytest.raises(BF.ValueError):
        BF.message_send(authRegisterDic['token'], result['channel_id'], message)

# user sends message to the channel
def test_message_send_message_to_channel():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    result = BF.channels_create(authRegisterDic['token'], 'good team', True)
    message = 'how are you' 
    result = BF.message_send(authRegisterDic['token'], result['channel_id'], message)
    BF.resetMessage_id()
    assert result['message_id'] == 1

# test message_sendlater channel_id is invalid
def test_message_sendlater():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    message = 'how are you' 
    with pytest.raises(BF.ValueError):
        BF.sendlater_message(authRegisterDic['token'], 1, message, 4596999)
 
# time sent is a time in the past
def test_message_sendlater():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    result = BF.channels_create(authRegisterDic['token'], 'good team', True)
    message = 'how are you' 
    with pytest.raises(BF.ValueError):
        BF.sendlater_message(authRegisterDic['token'], result['channel_id'], message, 1242523)
        
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    messageDict = BF.message_send(token1, channelID, "Hello World")

    invalidReactID = -420
    with pytest.raises(BF.ValueError):
        BF.message_react(token1, messageDict['message_id'], invalidReactID)



def test_message_remove_valid():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    messageDict = BF.message_send(token1, channelID, "Hello World")
    BF.message_remove(token1, messageDict['message_id'])    

def test_message_remove_message_doesnt_exist():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    messageDict = BF.message_send(token1, channelID, "Hello World")

    BF.message_remove(token1, messageDict['message_id'])
    with pytest.raises(BF.ValueError):
        BF.message_remove(token1, messageDict['message_id'])

def test_message_remove_no_permission():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']
    authRegisterDict2 = BF.user_register('bot2@gmail.com', '123456', 'real', 'bot2')
    token2 = authRegisterDict2['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']
    BF.channel_join(token2, channelID)

    messageDict = BF.message_send(token1, channelID, "Hello World")

    with pytest.raises(BF.AccessError):
        BF.message_remove(token2, messageDict['message_id'])

def test_messages_edit_not_poster_of_message():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']
    authRegisterDict2 = BF.user_register('bot2@gmail.com', '123456', 'real', 'bot2')
    token2 = authRegisterDict2['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']
    BF.channel_join(token2, channelID)

    messageDict = BF.message_send(token1, channelID, "Hello World")
    
    with pytest.raises(BF.AccessError): 
        BF.message_edit(token2, messageDict['message_id'], 'changed message')

def test_messges_edit_not_owner(): 
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']
    authRegisterDict2 = BF.user_register('bot2@gmail.com', '123456', 'real', 'bot2')
    token2 = authRegisterDict2['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']
    BF.channel_join(token2, channelID)

    messageDict = BF.message_send(token2, channelID, "Hello World")
    
    with pytest.raises(BF.AccessError): 
        BF.message_edit(token2, messageDict['message_id'], 'changed message')
     
def test_messages_edit_not_slack_admin_or_owner(): 
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']
    authRegisterDict2 = BF.user_register('bot2@gmail.com', '123456', 'real', 'bot2')
    token2 = authRegisterDict2['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']
    BF.channel_join(token2, channelID)

    messageDict = BF.message_send(token2, channelID, "Hello World")
    
    with pytest.raises(BF.AccessError): 
        BF.message_edit(token2, messageDict['message_id'], 'changed message')

def test_message_react_invalid_message():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    random_message_id = 23

    with pytest.raises(BF.ValueError):
        BF.message_react(token1, random_message_id, 1)


def test_message_react_already_reacted():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    messageDict = BF.message_send(token1, channelID, "Hello World")

    BF.message_react(token1, messageDict['message_id'], 1)
    with pytest.raises(BF.ValueError):
        BF.message_react(token1, messageDict['message_id'], 1)

def test_message_unreact_invalid_message():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    random_message_id = 23

    with pytest.raises(BF.ValueError):
        BF.message_unreact(token1, random_message_id, 1)

def test_message_unreact_invalid_react():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    messageDict = BF.message_send(token1, channelID, "Hello World")

    invalidReactID = -420
    with pytest.raises(BF.ValueError):
        BF.message_unreact(token1, messageDict['message_id'], invalidReactID)

def test_message_unreact_no_active_react():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    messageDict = BF.message_send(token1, channelID, "Hello World")

    with pytest.raises(BF.ValueError):
        BF.message_unreact(token1, messageDict['message_id'], 1)

def test_message_pin_invalid_message():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    random_message_id = 23

    with pytest.raises(BF.ValueError):
        BF.message_pin(token1, random_message_id)

def test_message_pin_not_admin():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']
    authRegisterDict2 = BF.user_register('bot2@gmail.com', '123456', 'real', 'bot2')
    token2 = authRegisterDict2['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']
    BF.channel_join(token2, channelID)

    messageDict = BF.message_send(token1, channelID, "Hello World")

    with pytest.raises(BF.ValueError):
        BF.message_pin(token2, messageDict['message_id'])

def test_message_pin_not_member():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()

    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']
    authRegisterDict2 = BF.user_register('bot2@gmail.com', '1234567', 'real2', 'bot2')
    token2 = authRegisterDict2['token'] 
    assert token1 != token2

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', False)
    channelID = channelsCreateDict['channel_id']

    messageDict = BF.message_send(token1, channelID, "Hello World")

    with pytest.raises(BF.AccessError):
        BF.message_pin(token2, messageDict['message_id'])
        
        
def test_channels_join():
    BF.data['user_info'] = []
    BF.data['channel_info'] = [] 
    BF.resetUser_id()
    BF.resetChannel_id()
    authRegisterDic = BF.user_register('cameron.ha@hotmail.com', '1234567', 'cameron', 'burrell')
    authRegisterDic_2 = BF.user_register('cameron.11@hotmail.com.au', '1234567', 'c', 'b')
    result = BF.channels_create(authRegisterDic['token'], 'good team', 'True')
    with pytest.raises(BF.ValueError): 
        BF.channel_join(authRegisterDic['token'], 2)

'''
def test_channels_join_private():
    BF.data['user_info'] = []
    BF.data['channel_info'] = [] 
    BF.resetUser_id()
    BF.resetChannel_id()
    authRegisterDic = BF.user_register('cameron.ha@hotmail.com', '1234567', 'cameron', 'burrell')
    authRegisterDic_2 = BF.user_register('cameron.11@hotmail.com.au', '1234567', 'c', 'b')
    result = BF.channels_create(authRegisterDic['token'], 'good team', 'False')
    with pytest.raises(BF.AccessError): 
        BF.channel_join(authRegisterDic_2['token'], 1)

'''

def test_channels_join_non_admin():
    BF.data['user_info'] = []
    BF.data['channel_info'] = [] 
    authRegisterDic = BF.user_register('cameron.ha@hotmail.com', '1234567', 'cameron', 'burrell')
    authRegisterDic_2 = BF.user_register('cameron.11@hotmail.com.au', '1234567', 'c', 'b')
    result = BF.channels_create(authRegisterDic['token'], 'good team', 'False')
    BF.resetUser_id()
    BF.resetChannel_id()
    with pytest.raises(BF.ValueError): 
        BF.channel_join(authRegisterDic_2['token'], 1)

def test_channels_leave(): 
    BF.data['user_info'] = []
    BF.data['channel_info'] = [] 
    authRegisterDic = BF.user_register('cameron.ha@hotmail.com', '1234567', 'cameron', 'burrell')
    authRegisterDic_2 = BF.user_register('cameron.11@hotmail.com.au', '1234567', 'c', 'b')
    result = BF.channels_create(authRegisterDic['token'], 'good team', 'True')
    BF.resetUser_id()
    BF.resetChannel_id()
    with pytest.raises(BF.ValueError): 
        BF.channel_leave(authRegisterDic['token'], 2)

def test_channels_addowner_channel_id_invalid(): 
    BF.data['user_info'] = []
    BF.data['channel_info'] = [] 
    authRegisterDic = BF.user_register('cameron.ha@hotmail.com', '1234567', 'cameron', 'burrell')
    authRegisterDic_2 = BF.user_register('cameron.11@hotmail.com.au', '1234567', 'c', 'b')
    result = BF.channels_create(authRegisterDic['token'], 'good team', 'True')
    BF.resetUser_id()
    BF.resetChannel_id()
    with pytest.raises(BF.ValueError): 
        BF.addowners_channel(authRegisterDic['token'], 2, authRegisterDic_2['u_id'])

def test_channels_addowner_alreadyowner(): 
    BF.data['user_info'] = []
    BF.data['channel_info'] = [] 
    authRegisterDic = BF.user_register('cameron.ha@hotmail.com', '1234567', 'cameron', 'burrell')
    authRegisterDic_2 = BF.user_register('cameron.11@hotmail.com.au', '1234567', 'c', 'b')
    result = BF.channels_create(authRegisterDic['token'], 'good team', 'True')
    BF.addowners_channel(authRegisterDic['token'], 1, authRegisterDic_2['u_id'])
    BF.resetUser_id()
    BF.resetChannel_id()
    with pytest.raises(BF.ValueError): 
        BF.addowners_channel(authRegisterDic['token'], 1, authRegisterDic_2['u_id'])

def test_channels_addowner_id_not_owner(): 
    BF.data['user_info'] = []
    BF.data['channel_info'] = [] 
    authRegisterDic = BF.user_register('cameron.ha@hotmail.com', '1234567', 'cameron', 'burrell')
    authRegisterDic_2 = BF.user_register('cameron.11@hotmail.com.au', '1234567', 'c', 'b')
    result = BF.channels_create(authRegisterDic['token'], 'good team', 'True')
    BF.resetUser_id()
    BF.resetChannel_id()
    with pytest.raises(BF.AccessError): 
        BF.addowners_channel(authRegisterDic_2['token'], 1, authRegisterDic_2['u_id'])
        
def test_channels_removeowner_invalid_channel_id(): 
    BF.data['user_info'] = []
    BF.data['channel_info'] = [] 
    authRegisterDic = BF.user_register('cameron.ha@hotmail.com', '1234567', 'cameron', 'burrell')
    authRegisterDic_2 = BF.user_register('cameron.11@hotmail.com.au', '1234567', 'c', 'b')
    result = BF.channels_create(authRegisterDic['token'], 'good team', 'True')
    BF.resetUser_id()
    BF.resetChannel_id()
    with pytest.raises(BF.ValueError): 
        BF.removeowners_channel(authRegisterDic['token'], 2, authRegisterDic_2['u_id'])
        
def test_channels_removeowner_user_non_owner(): 
    BF.data['user_info'] = []
    BF.data['channel_info'] = [] 
    authRegisterDic = BF.user_register('cameron.ha@hotmail.com', '1234567', 'cameron', 'burrell')
    authRegisterDic_2 = BF.user_register('cameron.11@hotmail.com.au', '1234567', 'c', 'b')
    result = BF.channels_create(authRegisterDic['token'], 'good team', 'True')
    BF.addowners_channel(authRegisterDic['token'], 1, authRegisterDic_2['u_id'])
    BF.removeowners_channel(authRegisterDic['token'], 1, authRegisterDic_2['u_id'])
    BF.resetUser_id()
    BF.resetChannel_id()
    with pytest.raises(BF.ValueError): 
        BF.removeowners_channel(authRegisterDic['token'], 1, authRegisterDic_2['u_id'])
    
        
